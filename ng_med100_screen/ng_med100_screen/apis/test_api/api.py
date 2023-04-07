from ng_med100_screen.frame.core.api.authorization import NoAuthrizedApi

class GetDisplayCA(NoAuthrizedApi):


    @classmethod
    def get_desc(cls):
        return "获取可信证书管理"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 900001

    @classmethod
    def log_required(cls):
        return False

    def execute(self, request):
        return request

    def fill(self, response, data):
        return data