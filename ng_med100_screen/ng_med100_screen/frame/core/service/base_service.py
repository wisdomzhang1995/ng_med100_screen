from ng_med100_screen.frame.common.singleton import Singleton


class BaseApiService(Singleton):

    _api_mapping = None
    _protocol_set = None


    @classmethod
    def get_name(cls):
        raise NotImplementedError('Please implement this interface in subclass')

    @classmethod
    def get_desc(cls):
        raise NotImplementedError('Please implement this interface in subclass')

    @classmethod
    def get_flag(cls):
        raise NotImplementedError('Please implement this interface in subclass')

    def get_apis(self):
        if self._api_mapping is None:
            return []
        return self._api_mapping.values()

    def add(self, *apis):
        if self._api_mapping is None:
            self._api_mapping = {}
        api_list = list()
        api_list.extend(apis)
        for cur_api in api_list:
            self._api_mapping[cur_api.get_name()] = cur_api
            cur_api.set_service(self)

    def set_protocols(self, protocol, *protocols):
        if self._protocol_set is None:
            self._protocol_set = set([protocol])

        for _pro in protocols:
            self._protocol_set.add(_pro)

    def get_protocols(self):
        return list(self._protocol_set)

    def url_router(self, url):
        api = self._api_mapping.get(url, None)
        if api:
            return api
        raise NotImplementedError('apis is not existed')

    def service_run(self, url, params):
        api = self.url_router(url)
        return api().api_run(params)
