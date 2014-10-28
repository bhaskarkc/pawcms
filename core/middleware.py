from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings


class SelectiveSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        if request.path_info[0:5] in settings.DISABLE_SESSIONS_FOR:
            return
        super(SelectiveSessionMiddleware, self).process_request(request)

    def process_response(self, request, response):
        if request.path_info[0:5] in settings.DISABLE_SESSIONS_FOR:
            return response
        return super(SelectiveSessionMiddleware, self).process_response(request, response)