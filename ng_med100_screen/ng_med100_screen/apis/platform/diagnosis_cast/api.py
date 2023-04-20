from apis.platform.overview.manager import OverviewManager
from frame.common.with_metaclass import with_metaclass
from frame.core.api.authorization import NoAuthrizedApi
from frame.core.api.request_parse import RequestFieldSet
from frame.core.api.response_parse import ResponseFieldSet, ResponseField
from frame.core.field.base import ListField, DictField, CharField, IntField


class GetCaseTypeMonthCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="按病理类型分布", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

    @classmethod
    def get_desc(cls):
        return "按病理类型分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        statistics_status_list = OverviewManager.get_case_status_count()
        return None

    def fill(self, response, data):
        response.data_list = data
        return response


class GetSubSpecialtyTypeMonthCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="按亚专科分类", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

    @classmethod
    def get_desc(cls):
        return "按亚专科分类"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        statistics_status_list = OverviewManager.get_case_status_count()
        return None

    def fill(self, response, data):
        response.data_list = data
        return response


class GetCellMonthCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="细胞学分类", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

    @classmethod
    def get_desc(cls):
        return "按细胞学分类"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        statistics_status_list = OverviewManager.get_case_status_count()
        return None

    def fill(self, response, data):
        response.data_list = data
        return response


class GetFrozenMonthSummary(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="近6月冰冻月度汇总", fmt=DictField(desc="", conf={
            "statistic_time": CharField(desc="统计时间"),
            "cast_count": CharField(desc="病例数"),
            "chain": IntField(desc="环比上月"),
    }))

    @classmethod
    def get_desc(cls):
        return "近6月冰冻月度汇总"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        statistics_status_list = OverviewManager.get_case_status_count()
        return None

    def fill(self, response, data):
        response.data_list = data
        return response


class GetReportMonthGeneratedTime(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="近6月报告平均输出时长", fmt=DictField(desc="", conf={
            "statistic_time": CharField(desc="统计时间"),
            "avg_diagnosis_time": CharField(desc="平均诊断时长"),
            "report_gen_time": IntField(desc="平均报告输出时长"),
    }))

    @classmethod
    def get_desc(cls):
        return "近6月报告平均输出时长"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        statistics_status_list = OverviewManager.get_case_status_count()
        return None

    def fill(self, response, data):
        response.data_list = data
        return response

