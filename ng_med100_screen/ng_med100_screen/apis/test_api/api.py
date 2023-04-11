from ng_med100_screen.frame.common.with_metaclass import with_metaclass
from ng_med100_screen.frame.core.api.authorization import NoAuthrizedApi
from ng_med100_screen.frame.core.api.request_parse import RequestFieldSet, RequestField
from ng_med100_screen.frame.core.api.response_parse import ResponseFieldSet
from ng_med100_screen.frame.core.field.base import DictField, IntField, CharField, DatetimeField
from model.models import TMoneySiteCycle


class GetDisplayCA(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)

    request.page_info = RequestField(DictField, desc="分页条件", conf={
        "page_num": IntField(desc="页码", is_required=False),
        "page_size": IntField(desc="每页条数", is_required=False)
    })

    # response.total_page = ResponseField(IntField, desc='总页数')
    # response.total = ResponseField(IntField, desc='总条数')
    # response.data = ResponseField(ListField, desc='可信证书管理', fmt=DictField(desc="可信证书管理", conf={
    #     "id": IntField(desc="id"),
    #     "upload_name": CharField(desc="上传文件名"),
    #     "save_name": CharField(desc="存储文件名称"),
    #     "content_type": CharField(desc="文件类型"),
    #     "suffix": CharField(desc="文件后缀"),
    #     "size": CharField(desc="文件大小"),
    #     "upload_time": DatetimeField(desc="上传时间"),
    #     "display_type": CharField(desc="证书类型"),
    # }))

    @classmethod
    def get_desc(cls):
        return "获取可信证书管理"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 900001

    @classmethod
    def log_required(cls):
        return False

    def execute(self, request):
        limit = TMoneySiteCycle.objects.filter().all()
        limit_data = [l.as_dict() for l in limit[:2]]
        print("qqqqqqqqqqqqqqqqqqqqqq", limit_data)
        return limit_data

    def fill(self, response, data):
        return data