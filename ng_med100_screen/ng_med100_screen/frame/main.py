import json

from django.http import HttpResponse

from ng_med100_screen.apis.user_register import user_service
from ng_med100_screen.frame.protocol.protocol_main import DjangoProtocol
from ng_med100_screen.frame.thread_contex import RequestContext, _request

protocol = DjangoProtocol()
protocol.add(user_service)
print(f"ffffffffffffffffffGGGGGGGGGGGGGGGGGGGGGGGGGG", protocol._service_map)


def router(request):
    with RequestContext():
        _request.request = request
        result = protocol.protocol_run(request)
        # resp = HttpResponse(json.dumps({"msg": "WisdomZhang", "status": 0}))
        resp = HttpResponse(json.dumps(result))
        return resp