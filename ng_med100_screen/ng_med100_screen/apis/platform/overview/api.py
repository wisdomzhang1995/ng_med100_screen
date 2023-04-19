from apis.platform.overview.manager import OverviewManager
from frame.common.with_metaclass import with_metaclass
from frame.core.api.authorization import NoAuthrizedApi
from frame.core.api.request_parse import RequestFieldSet
from frame.core.api.response_parse import ResponseFieldSet, ResponseField
from frame.core.field.base import ListField, DictField, CharField, IntField


class GetCaseStatusCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="状态分布数据", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

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
        statistics_status_list = OverviewManager.get_case_status_count()
        return statistics_status_list

    def fill(self, response, data):
        response.data_list = data
        return response


class GetCaseDiagnosisTypeCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="就医来源分布列表", fmt=DictField(desc="就医来源分布数据", conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

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
        diagnosis_type_count_list = OverviewManager.get_case_diagnosis_type_count()
        return diagnosis_type_count_list

    def fill(self, response, data):
        response.data_list = data
        return response


class GetCaseDiagnosisResult(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="获取诊断结果分布", fmt=DictField(desc="", conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

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
        diagnosis_type_count_list = OverviewManager.get_case_diagnosis_result()
        return diagnosis_type_count_list

    def fill(self, response, data):
        response.data_list = data
        return response


class GetCaseStatisticsCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.obj = ResponseField(DictField, desc="获取专家病例总收入数", conf={
        "active_experts_count": IntField(desc="昨日活跃专家数"),
        "cast_count": IntField(desc="病例数"),
        "total_income": IntField(desc="总收入（万）"),
    })

    @classmethod
    def get_desc(cls):
        return "获取专家病例总收入数"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        diagnosis_type_count_list = OverviewManager.get_case_statistics_count()
        return diagnosis_type_count_list

    def fill(self, response, data):
        response.obj = data
        return response


class GetCaseSubSpecialty(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="专家病例总收入数", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

    @classmethod
    def get_desc(cls):
        return "获取亚专科分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        sub_specialty_count_list = OverviewManager.get_case_sub_specialty()
        return sub_specialty_count_list

    def fill(self, response, data):
        response.data_list = data
        return response


class GetCaseSiteDynamics(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.head = ResponseField(ListField, desc="数据表头", fmt=DictField(desc="站点数据", conf={
        "name": CharField(desc="表头名称"),
        "prop": CharField(desc="属性名"),
    }))
    response.data_list = ResponseField(ListField, desc="108家站点动态数据", fmt=DictField(desc="站点数据", conf={
        "name": CharField(desc="站点名称"),
        "case_count": IntField(desc="病例总数"),
        "frost_count": IntField(desc="冰冻病例数"),
        "tissue_count": IntField(desc="组织学病例数"),
        "cell_count": IntField(desc="细胞学数"),
        "immunostaining_count": IntField(desc="免疫特染数"),
        "numerator_count": IntField(desc="分子数"),
    }))

    @classmethod
    def get_desc(cls):
        return "108家站点动态"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        sub_specialty_count_list = OverviewManager.get_case_site_dynamics()
        head = [
            {"name": '站点名称', "prop": 'name'},
            {"name": '病例总数', "prop": 'case_count'},
            {"name": '冰冻病例', "prop": 'frost_count'},
            {"name": '组织学病例', "prop": 'tissue_count'},
            {"name": '细胞学', "prop": 'cell_count'},
            {"name": '免疫特染', "prop": 'immunostaining_count'},
            {"name": '分子', "prop": 'numerator_count'},
        ]
        return head, sub_specialty_count_list

    def fill(self, response, head, data):
        response.head = head
        response.data_list = data
        return response


class GetSpecimenCirculation(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="标本流转分布", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

    @classmethod
    def get_desc(cls):
        return "标本流转分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        sub_specialty_count_list = OverviewManager.get_specimen_circulation()
        return sub_specialty_count_list

    def fill(self, response, data):
        response.data_list = data
        return response


class GetCastBusinessType(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)

    @classmethod
    def get_desc(cls):
        return "病例业务类型分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        sub_specialty_count_list = OverviewManager.get_cast_business_type()
        return sub_specialty_count_list

    def fill(self, response, data):
        return data


class GetCellCount(NoAuthrizedApi):
    request = with_metaclass(RequestFieldSet)
    response = with_metaclass(ResponseFieldSet)
    response.data_list = ResponseField(ListField, desc="细胞学分布", fmt=DictField(desc="",conf={
            "name": CharField(desc="名称"),
            "count": IntField(desc="数量"),
    }))

    @classmethod
    def get_desc(cls):
        return "细胞学分布"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return 1

    def execute(self, request):
        cell_count_list = OverviewManager.get_cell_count()
        return cell_count_list

    def fill(self, response, data):
        response.data_list = data
        return response