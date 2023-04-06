import traceback

from ng_med100_screen.frame.common.dict_wrapper import DictWrapper


class ServiceManager(object):
    _service_map = {}

    def add(self, service, *services):
        pass

    def get_service(self, flag):
        service = self._service_map.get(flag)
        if not service:
            return service
        raise NotImplementedError("The service is not exist")

    def get_services(self):
        return self._service_map.values()


class BaseProtocol(ServiceManager):

    def extract_params(self, request):
        raise NotImplementedError('Please implement this interface in subclass')

    def parse_request_data(self, request_params):
        return DictWrapper(request_params)

    def get_service_flag(self, pro_params):
        raise NotImplementedError('Please implement this interface in subclass')

    def get_api_flag(self, pro_parms):
        raise NotImplementedError('Please implement this interface in subclass')

    def protocol_run(self, request):
        try:
            file_data, request_params = self.extract_params(request)
            api_params = self.parse_request_data(request_params)
            service_str = self.get_service_flag(api_params)
            service_str = "user"
            api_str = api_params.api
            api_params.update(flag=service_str)
            api_params.update(file_data)
            service = self.get_service(service_str)
            service.service_run()
            url = "/api/api_doc"
            result = service.service_run(api_str, api_params)

            ...
        except Exception as e:
            print(traceback.print_exc())
            print(f"shun ------------------------------> {e}")
