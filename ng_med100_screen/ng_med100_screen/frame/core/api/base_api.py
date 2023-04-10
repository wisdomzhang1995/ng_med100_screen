import json
import os
import pathlib

import pysnooper

from ng_med100_screen.apis import api_abs_path
from ng_med100_screen.frame.tools.redis.redis_operator import redis_sys


class ApiInterface(object):

    @classmethod
    def get_name(cls, level=3):
        api_name = cls.__name__.lower()
        rel = pathlib.Path(os.sep.join(cls.__module__.split('.'))).relative_to(
            pathlib.Path(api_abs_path).parent)
        namespace = str(rel).split(os.sep, level)
        namespace = namespace if namespace[-1] != "api" else namespace[:-1]
        namespace.append(api_name)
        # todo dong: make the frame looks normally
        return '.'.join(namespace).replace('.', '/')

    @classmethod
    def get_desc(cls):
        return "这是一个测试的desc"

    @classmethod
    def get_author(cls):
        return "djd"

    @classmethod
    def get_version(cls):
        return "v1.0"


class ApiHelper(object):
    _service = None

    @classmethod
    def set_service(cls, service):
        cls._service = service

    @classmethod
    def get_service(cls):
        return cls._service


class BaseApi(ApiHelper, ApiInterface):
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
        for key, helper in request.get_fields().items():
            if key not in params:
                if helper.is_need() or (
                        helper.is_need() and helper.get_field().is_required()):
                    pass
            else:
                try:
                    if helper.get_field().parse_it():
                        setattr(request, key, params[key])
                except Exception as e:
                    pass
        return params

    def enhance_execute(self):
        if redis_sys.get("awesome", invert=int) == 310:
            kwargs = redis_sys.get("awesome_kwargs")
            debug_kwargs = json.loads(kwargs) if kwargs else {}
            return pysnooper.snoop(**debug_kwargs)(self.execute)
        return self.execute

    def deserialize(self, response, result):
        return result

    def api_run(self, params):
        request = self.parse(self.request, params)
        request = params
        self.authorized(request, params)
        result = self.enhance_execute()(request)
        respond_data = self.deserialize(self.response, result)
        return respond_data

