from frame.global_config import platform_flag_name, platform_flag_cn_name
from ng_med100_screen.frame.core.service.base_service import BaseApiService


class PlatformService(BaseApiService):

    @classmethod
    def get_name(cls):
        return platform_flag_cn_name

    @classmethod
    def get_desc(cls):
        return "针对云平台服务"

    @classmethod
    def get_flag(cls):
        return platform_flag_name

    @classmethod
    def get_accept(cls):
        return "application/json"

    @classmethod
    def get_response(cls):
        return "application/json"


platform_service = PlatformService()

from ng_med100_screen.apis.platform.overview.api import GetCaseStatusCount, GetCaseDiagnosisTypeCount, \
    GetCaseDiagnosisResult, GetCaseStatisticsCount, GetCaseSubSpecialty, GetCaseSiteDynamics, GetSpecimenCirculation, \
    GetCellCount
platform_service.add(GetCaseStatusCount, GetCaseDiagnosisTypeCount, GetCaseDiagnosisResult, GetCaseStatisticsCount,
                     GetCaseSubSpecialty, GetCaseSiteDynamics, GetSpecimenCirculation, GetCellCount)
print("===================================================")
for k, v in platform_service._api_mapping.items():
    print(f"{k}: {v}")
