import time
from importlib import import_module
from django.conf import settings
from django.contrib.sessions.backends.base import UpdateError
from django.core.exceptions import SuspiciousOperation
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import http_date

class SessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response   =   get_response
        engine  =   import_module( settings.SESSION_ENGINE)
        self.SessionStore   =   engine.SessionStore
        