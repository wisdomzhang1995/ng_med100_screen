

class DjangoProtocol(object):

    def get_service_flag(self, pro_params):
        return pro_params.flag

    def get_api_flag(self, pro_parms):
        return pro_parms.api

    def get_success_parms(self, result):
        return {'status': 0, 'msg': '', 'data': result}

    def get_fail_parms(self, e):
        return {'status': -e.get_code(), 'msg': e.get_msg(), 'data': ''}