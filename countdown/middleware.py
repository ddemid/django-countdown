from datetime import datetime
from django.conf import settings
from django.views.generic.simple import direct_to_template


class CountdownMiddleware(object):
    def process_response(self, request, response):

        if settings.COUNTDOWN_TARGET_DATE > datetime.now():
            td = settings.COUNTDOWN_TARGET_DATE - datetime.now()
            return direct_to_template(request, "countdown/countdown.html", {
                    'countdown_sec': td.seconds % 60,
                    'countdown_min': (td.seconds / 60) % 60 ,
                    'countdown_hour': (td.seconds / (60*60) % 24 ),
                    'countdown_day': (td.days),



                    })
        else:
            return response