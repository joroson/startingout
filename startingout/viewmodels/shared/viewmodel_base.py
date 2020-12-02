from pyramid.request import Request

from startingout.infrastructure import request_dict


class ViewModelBase:
    def __init__(self, request: Request):
        self.error: str = None
        self.request = request
        self.request_dict = request_dict.create(request)

    def to_dict(self):
        return self.__dict__
