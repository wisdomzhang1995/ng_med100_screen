from ng_med100_screen.frame.common.singleton import Singleton


class BaseAPIManager(Singleton):

    _api_mapping = None

    def add(self, *apis):
        if self._api_mapping is None:
            self._api_mapping = {}
        api_list = list()
        api_list.extend(apis)
        for cur_api in api_list:
            self._api_mapping[cur_api.get_name()] = cur_api
            cur_api.set_service(self)

    def url_router(self, url):
        api = self._api_mapping.get(url, None)
        if api:
            return api
        raise NotImplementedError('api is not existed')

    def service_run(self, url, params):
        api = self.url_router(url)
        return api().api_run(params)
