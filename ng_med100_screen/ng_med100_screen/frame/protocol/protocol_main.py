import json

from frame.core.protocol.responser import Responser, ResponseField
from ng_med100_screen.frame.core.field.base import CharField, IntField
from ng_med100_screen.frame.core.protocol.base_protocol import BaseProtocol
from frame.core.protocol.parser import Parser, ParseField


class DjangoProtocol(BaseProtocol):

    parser = Parser()
    parser.flag = ParseField(CharField, desc="服务标识")
    responser = Responser()
    responser.resultCode = ResponseField(IntField, desc="状态码")
    responser.resultMsg = ResponseField(CharField, desc="错误消息")
    responser.data = ResponseField(CharField, desc="空字符")

    _upload_files = "_upload_files"
    _remote_ip = "_remote_ip"
    _agent = "_agent"

    def get_service_flag(self, pro_params):
        return pro_params.flag

    def get_api_flag(self, pro_params):
        return pro_params.api

    def get_api_str(self, path_info):
        return path_info.replace('/api/', '').rstrip("/")

    def set_protocol(self):
        pass

    def get_success_parms(self, result):
        return {'resultCode': 0, 'resultMsg': '', 'data': result}

    def get_fail_parms(self, e):
        return {'resultCode': -e.get_code(), 'resultMsg': e.get_msg(), 'data': ''}

    def extract_params(self, request):
        # for k, v in request.POST.items():
        #     print(f"POST {k}: {v}")
        # for k, v in request.META.items():
        #     print(f"META {k}: {v}")
        meta = request.META
        api_str = self.get_api_str(meta.get("PATH_INFO"))
        jwt_token = meta.get("HTTP_AUTHORIZATION")
        print("==============================", request.body, request.POST)
        try:
            request_params = {key: value for key, value in json.loads(request.body.decode("utf-8")).items()}
        except Exception as e:
            print("zs----------------------------", e)
            request_params = {key: value for key, value in request.POST.items()}
        request_params.update({"api": api_str, "jwt_token": jwt_token})
        remote_ip = meta['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in meta else meta['REMOTE_ADDR']
        file_data = {
            self._upload_files: request.FILES if hasattr(request, "FILES") else "",
            self._remote_ip: remote_ip,
            self._agent: meta.get("HTTP_USER_AGENT", "")
        }
        return file_data, request_params