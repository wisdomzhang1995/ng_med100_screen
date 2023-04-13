import json

from django.http import HttpResponse
from django.shortcuts import render

from frame.common import signature
from frame.core.api.doc import TextApiDoc
from ng_med100_screen.apis.platform_register import platform_service
from frame.common.json_encoder import DateEncoder
from ng_med100_screen.apis.user_register import user_service
from ng_med100_screen.frame.protocol.protocol_main import DjangoProtocol
from ng_med100_screen.frame.thread_contex import RequestContext, _request

protocol = DjangoProtocol()
protocol.add(user_service)
protocol.add(platform_service)
print(f"ffffffffffffffffffGGGGGGGGGGGGGGGGGGGGGGGGGG", protocol._service_map)


def router(request):
    with RequestContext():
        _request.request = request
        result = protocol.protocol_run(request)
        resp = HttpResponse(json.dumps(result, cls=DateEncoder))
        return resp


def api_doc(request):
    try:
        api_signature_doc = signature.__doc__
        services = protocol.get_services()
        for service in services:
            apis = service.get_apis()
            service.api_docs = [TextApiDoc(api) for api in apis]
        print("GGGGGGGGGGGGGG", services)
        # error_list = []
        # error_list.append(SysError)
        # error_list.extend(pro_errors.get_errors())
        # error_list.extend(api_errors.get_errors())
        # error_list.append(BusinessError)
        # error_list.append(AccessLimitError)
        # error_list.append(AccountForbiddenError)
        # error_list.append(AuthorizationError)
        # error_list_final = [(err.get_flag(), err.get_code(), err.get_desc()) for err
        #                     in error_list]

        return render(request, 'api_index.html', {
            'api_signature_doc': api_signature_doc,
            'services': services,
            # 'error_list': error_list_final,
        })
    except:
        import traceback
        print(traceback.print_exc())