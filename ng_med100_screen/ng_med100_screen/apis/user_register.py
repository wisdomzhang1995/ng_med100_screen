
from ng_med100_screen.frame.core.service.base_service import BaseApiService


class UserService(BaseApiService):

    @classmethod
    def get_name(cls):
        return "用户服务"

    @classmethod
    def get_desc(cls):
        return "针对用户提供服务"

    @classmethod
    def get_flag(cls):
        return "user"

    @classmethod
    def get_accept(cls):
        return "application/json"

    @classmethod
    def get_response(cls):
        return "application/json"


user_service = UserService()
from ng_med100_screen.apis.test_api.api import LogProtocol
user_service.add(LogProtocol)
print("user_service API MAP==========================", user_service._api_mapping)
