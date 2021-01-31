
from django.conf import settings

class SessionMiddleware:

    def process_request( self, request ):
        engine  = import_module( settings.SESSION_ENGINE)
        session_key = request.COOKIES.get( settings.SESSION_COOKIE_NAME, None )
        request.session = engine.SessionStore( session_key )