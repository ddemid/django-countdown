from datetime import datetime
from django.shortcuts  import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse



class CountdownMiddleware(object):
    def process_response(self, request, response):

        if settings.COUNTDOWN_TARGET_DATE > datetime.now():
            
            # Allow to login in admin part
            # Allow access to all authentificated users
            if request.path_info.startswith(reverse('admin:index')) or \
                                    request.user.is_authenticated():
                return response
            
            
            td = settings.COUNTDOWN_TARGET_DATE - datetime.now()
            return render_to_response("countdown/countdown.html", {
                    'countdown_sec': td.seconds % 60,
                    'countdown_min': (td.seconds / 60) % 60 ,
                    'countdown_hour': (td.seconds / (60*60) % 24 ),
                    'countdown_day': (td.days),
                    }, context_instance=RequestContext(request))
        else:
            return response