#!/usr/bin/env python

from setuptools import setup, find_packages
import countdown

setup(
    name='django-countdown',
    description='Easy to setup countdown for your django site.',
    #long_description=open('README.rst').read(),
    packages=['countdown', ],
    author='Dzmitry Dzemidzenka, Kuldeep Rishi',
    author_email='ddemidenko@gmail.com, kuldeepkrishi@gmail.com',
    url='https://github.com/ddemid/django-countdown',
    version=countdown.__version__,
	package_data={'countdown': ['templates/countdown/*html', 'static/countdown/css/*.css', 'static/countdown/js/*.js', 'static/countdown/images/*.*']},
	zip_safe=False,
)
