import pyramid.renderers
import pyramid.httpexceptions as exc

class BaseController:
    def __init__(self, request):
        self.request = request