import json

from django.http import HttpResponse
from django.shortcuts import render

from frame.common import signature
from frame.core.api.doc import TextApiDoc
from frame.core.exception.api_error import api_errors
from frame.core.exception.business_error import BusinessError
from ng_med100_screen.apis.platform_register import platform_service
from frame.common.json_encoder import JSONEncoder
# from ng_med100_screen.apis.user_register import user_service
from ng_med100_screen.frame.protocol.protocol_main import DjangoProtocol
from ng_med100_screen.frame.thread_contex import RequestContext, _request
from frame.core.exception.pro_error import pro_errors, ProtocolCodes, ProtocolError

protocol = DjangoProtocol()
# protocol.add(user_service)
protocol.add(platform_service)
print(f"protocol service_map=============================", protocol._service_map)


def router(request):
    with RequestContext():
        _request.request = request
        result = protocol.protocol_run(request)
        # data = result["data"]
        # data = {
        #     "data": result,
        #     "resultCode": 0,
        #     "resultMsg": ""
        # }
        resp = HttpResponse(json.dumps(result, cls=JSONEncoder))
        resp['Content-Type'] = 'application/json'
        resp['Access-Control-Allow-Origin'] = '*'  # 处理跨域请求
        resp['Access-Control-Max-Age'] = 86400
        resp['Access-Control-Allow-Methods'] = '*'
        resp['Access-Control-Allow-Headers'] = '*'
        resp['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, ' \
                                               'Fetch-Mode, accept'

        return resp


def api_doc(request):
    try:
        api_signature_doc = signature.__doc__
        services = protocol.get_services()
        for service in services:
            apis = service.get_apis()
            service.api_docs = [TextApiDoc(api) for api in apis]
        print("GGGGGGGGGGGGGG", services)
        error_list = []
        # error_list.append(SysError)
        error_list.extend(pro_errors.get_errors())
        error_list.extend(api_errors.get_errors())
        error_list.append(BusinessError)
        # error_list.append(AccessLimitError)
        # error_list.append(AccountForbiddenError)
        # error_list.append(AuthorizationError)
        error_list_final = [(err.get_flag(), err.get_code(), err.get_desc()) for err
                            in error_list]

        return render(request, 'api_index.html', {
            'api_signature_doc': api_signature_doc,
            'services': services,
            'error_list': error_list_final,
        })
    except:
        import traceback
        print(traceback.print_exc())