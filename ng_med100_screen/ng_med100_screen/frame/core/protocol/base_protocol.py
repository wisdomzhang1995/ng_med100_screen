

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
    def protocol_run(self, request):
        pass
