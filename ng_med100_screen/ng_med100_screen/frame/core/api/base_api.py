import json

import pysnooper

from ng_med100_screen.frame.tools.redis.redis_operator import redis_sys


class ApiHelper(object):
    _service = None

    @classmethod
    def set_service(cls, service):
        cls._service = service

    @classmethod
    def get_service(cls):
        return cls._service


class BaseApi(ApiHelper):
    request = None
    response = None
    # def __init__(self):
    #     assert self.request is not None
    #     assert issubclass(self.request, RequestFieldSet)
    #
    #     assert self.response is not None
    #     assert issubclass(self.response, ResponseFieldSet)
    #
    #     self.request = type('tmp' + self.request.__name__, (self.request,),
    #                         {})()
    #     self.response = type('tmp' + self.response.__name__, (self.response,),
    #                          {})()

    def authorized(self, request, params):
        raise NotImplementedError('Please implement this interface in subclass')

    def execute(self, *args, **kwargs):
        raise NotImplementedError('Please implement this interface in subclass')

    def parse(self, request, params):
        return request

    def enhance_execute(self):
        if redis_sys.get("awesome", invert=int) == 310:
            kwargs = redis_sys.get("awesome_kwargs")
            debug_kwargs = json.loads(kwargs) if kwargs else {}
            return pysnooper.snoop(**debug_kwargs)(self.execute)
        return self.execute

    def api_run(self, params):
        request = self.parse(self.request, params)
        self.authorized(request, params)
        result = self.enhance_execute()(request)
        respond_data = self.deserialize(self.response, result)
        return respond_data

