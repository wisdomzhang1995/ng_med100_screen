from apis.platform.overview.manager import OverviewManager
from frame.common.with_metaclass import with_metaclass
from frame.core.api.authorization import NoAuthrizedApi
from frame.core.api.request_parse import RequestFieldSet
from frame.core.api.response_parse import ResponseFieldSet


class GetCaseStatusCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)

    @classmethod
    def get_desc(cls):
        return "获取状态分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        print("qqqqqqqqqqqqqqqqqqqqqq")
        statistics_status_list = OverviewManager.get_case_status_count()
        return statistics_status_list

    def fill(self, response, data):
        return data


class GetCaseDiagnosisTypeCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)

    @classmethod
    def get_desc(cls):
        return "获取就医来源分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        print("qqqqqqqqqqqqqqqqqqqqqq")
        diagnosis_type_count_list = OverviewManager.get_case_diagnosis_type_count()
        return diagnosis_type_count_list

    def fill(self, response, data):
        return data


class GetCaseDiagnosisResult(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)

    @classmethod
    def get_desc(cls):
        return "获取诊断结果分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        print("qqqqqqqqqqqqqqqqqqqqqq")
        diagnosis_type_count_list = OverviewManager.get_case_diagnosis_result()
        return diagnosis_type_count_list

    def fill(self, response, data):
        return data