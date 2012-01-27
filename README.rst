===============
django-countdown
===============

Simple implementation of countdown page.
Using jQuery Countdown plugin v1.0
* http://www.littlewebthings.com/projects/countdown/


Installation
====================


settings.py::

    # settings.py
    # ============

    INSTALLED_APPS = (
        ...
        'countdown',
        ...
    )
    MIDDLEWARE_CLASSES = (
        ...
        'countdown.middleware.CountdownMiddleware',
    )

    COUNTDOWN_TARGET_DATE = datetime.datetime(2011, 11, 1, 11, 11, 11, 111111)


COUNTDOWN_TARGET_DATE is python datetime object which represents the countdown target date.


:author: Dzmitry Dzemidzenka
:date: 2012/01/27
