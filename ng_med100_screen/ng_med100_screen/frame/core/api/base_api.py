import json
import os
import pathlib

import pysnooper

from frame.core.api.request_parse import RequestFieldSet
from frame.core.api.response_parse import ResponseField, ResponseFieldSet
from frame.core.exception.api_error import api_errors, ApiCodes
from ng_med100_screen.apis import api_abs_path
from ng_med100_screen.frame.tools.redis.redis_operator import redis_sys


class ApiInterface(object):

    @classmethod
    def get_name(cls, level=3):
        cls_name = cls.__name__
        api_name = cls_name[0].lower() + cls_name[1:]
        rel = pathlib.Path(os.sep.join(cls.__module__.split('.'))).relative_to(
            pathlib.Path(api_abs_path).parent)
        namespace = str(rel).split(os.sep, level)
        namespace = namespace if namespace[-1] != "api" else namespace[:-1]
        namespace.append(api_name)
        # todo shun: make the frame looks normally
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

    def __init__(self):
        assert self.request is not None
        assert issubclass(self.request, RequestFieldSet)

        assert self.response is not None
        assert issubclass(self.response, ResponseFieldSet)

        self.request = type('tmp' + self.request.__name__, (self.request,),
                            {})()
        self.response = type('tmp' + self.response.__name__, (self.response,),
                             {})()

    def authorized(self, request, params):
        raise NotImplementedError('Please implement this interface in subclass')

    def execute(self, *args, **kwargs):
        raise NotImplementedError('Please implement this interface in subclass')

    def fill(self, response, *args):
        raise NotImplementedError('Please implement this interface in subclass')

    @classmethod
    def get_request_fields(cls):
        """get request fields"""
        if cls.request is None:
            print("request is empty!!!")
            return {}
        return cls.request.get_fields()

    @classmethod
    def get_response_fields(cls):
        """get request fields"""
        if cls.request is None:
            print("request is empty!!!")
            return {}
        return cls.response.get_fields()

    def parse(self, request, params):
        for key, helper in request.get_fields().items():
            if key not in params:
                if helper.is_need() or (
                        helper.is_need() and helper.get_field().is_required()):
                    raise api_errors(ApiCodes.INTERFACE_PARATERS_LOST, key)
            else:
                try:
                    if helper.get_field().parse_it():
                        setattr(request, key, params[key])
                except Exception as e:
                    raise api_errors(ApiCodes.INTERFACE_PARATERS_PARSE_WRONG,
                                     key, e)
        return request

    def enhance_execute(self):
        if redis_sys.get("awesome", invert=int) == 310:
            kwargs = redis_sys.get("awesome_kwargs")
            debug_kwargs = json.loads(kwargs) if kwargs else {}
            return pysnooper.snoop(**debug_kwargs)(self.execute)
        return self.execute

    def pack(self, response, result):
        args = result if type(result) is tuple else [result]
        if args:
            response = self.fill(response, *args)
        pack_data = {}
        print("response.get_fields()===============================", response.get_fields())
        for key in response.get_fields():
            value = getattr(response, key)
            if isinstance(value, ResponseField):
                raise Exception("response lose parameter {}".format(key))
            pack_data[key] = value

        return pack_data

    def api_run(self, params):
        request = self.parse(self.request, params)
        print("=========================GGGGGGGGGGGGGGGGGGGGGGGGG", request)
        self.authorized(request, params)
        respond_data = self.enhance_execute()(request)
        respond_data = self.pack(self.response, respond_data)
        return respond_data

