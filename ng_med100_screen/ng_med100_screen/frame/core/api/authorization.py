from ng_med100_screen.frame.core.api.base_api import BaseApi


class NoAuthrizedApi(BaseApi):

    def authorized(self, request, parms):
        return parms

    def has_permission(self, account_id, api_code):
        return True


class AuthorizedApi(BaseApi):
    _user_id = None
    _auth_flag = "auth"

    def _check_IP(self, token):
        print('check ip ......')

    def _check_time(self, token):
        print('check api timeout ...')