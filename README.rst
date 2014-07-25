===============
django-countdown (Support django v 1.5 and above)
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

    import datetime
    COUNTDOWN_TARGET_DATE = datetime.datetime(2015, 01, 01, 00, 00, 00, 000000)


COUNTDOWN_TARGET_DATE is python datetime object which represents the countdown target date.


:author: Dzmitry Dzemidzenka | Kuldeep Rishi
:date: 2012/01/27 | 2014/03/19 (Support for Django 1.5 added)
