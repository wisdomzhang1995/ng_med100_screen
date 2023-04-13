import traceback

from ng_med100_screen.frame.common.dict_wrapper import DictWrapper
from ng_med100_screen.frame.common.singleton import Singleton


class ServiceManager(object):
    _service_map = {}

    def add(self, *services):
        if self._service_map is None:
            self._service_map = {}
        service_list = list()
        service_list.extend(services)
        for cur_service in service_list:
            self._service_map[cur_service.get_flag()] = cur_service
            cur_service.set_protocols(self)

    def get_service(self, flag):
        service = self._service_map.get(flag)
        if service:
            return service
        raise NotImplementedError("The service is not exist")

    def get_services(self):
        return self._service_map.values()


class BaseProtocol(Singleton, ServiceManager):
    parser = None

    def extract_params(self, request):
        raise NotImplementedError('Please implement this interface in subclass')

    def parse_request_data(self, request_params):
        data = request_params.copy()
        pro_params = {}
        fields = self.parser.get_fields()
        for field_name, field_parser in fields.items():
            if field_name in data:
                value = data.pop(field_name)
                try:
                    pro_params[field_name] = field_parser.execute(value)
                except Exception as e:
                    print(f"fS {Exception}")

        print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", fields)
        return DictWrapper(pro_params), DictWrapper(request_params)

    def get_service_flag(self, pro_params):
        raise NotImplementedError('Please implement this interface in subclass')

    def get_api_flag(self, pro_parms):
        raise NotImplementedError('Please implement this interface in subclass')

    def protocol_run(self, request):
        try:
            file_data, request_params = self.extract_params(request)
            pro_params, api_params = self.parse_request_data(request_params)
            print("GGGGGGGGGGGGGGGGGGGGGGGGGGGG", pro_params)
            service_str = self.get_service_flag(pro_params)
            api_str = api_params.api
            api_params.update(flag=service_str)
            api_params.update(file_data)
            service = self.get_service(service_str)
            result = service.service_run(api_str, api_params)
            return result

        except Exception as e:
            print(traceback.print_exc())
            print(f"shun ------------------------------> {e}")
