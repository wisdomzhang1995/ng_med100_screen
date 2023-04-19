import os
from importlib import import_module

from frame.global_config import platform_flag_name, platform_flag_cn_name, project_name
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

# from ng_med100_screen.apis.platform.overview.api import GetCaseStatusCount, GetCaseDiagnosisTypeCount, \
#     GetCaseDiagnosisResult, GetCaseStatisticsCount, GetCaseSubSpecialty, GetCaseSiteDynamics, GetSpecimenCirculation, \
#     GetCellCount
# platform_service.add(GetCaseStatusCount, GetCaseDiagnosisTypeCount, GetCaseDiagnosisResult, GetCaseStatisticsCount,
#                      GetCaseSubSpecialty, GetCaseSiteDynamics, GetSpecimenCirculation, GetCellCount)
ump_module = ["overview", "diagnosis_cast"]


def add_all_single_file_api(api_module):
    for api_name, api in api_module.__dict__.items():
        if hasattr(api, '__base__'):
            if api.__base__.__name__ in ["NoAuthrizedApi", "IFWAccountAuthorizedApi"]:
                platform_service.add(api)


for module_name in ump_module:
    base_dir = [project_name, "apis", "platform"]
    module_dir_list = module_name.split(".")
    base_dir += module_dir_list
    api_dir = os.sep.join(base_dir)
    for parent, dir_filenames, filenames in os.walk(api_dir):
        for filename in filenames:
            p = os.path.join(parent, filename)
            if "api." in p and "__pycache__" not in p:
                filename_str = p[p.find(project_name):-3]
                if "/" in p:
                    filename_import_list = filename_str.split("/")
                else:
                    filename_import_list = filename_str.split("\\")
                api_module = import_module(".".join(filename_import_list))
                print("API VARIABLE", api_module)
                add_all_single_file_api(api_module)

for k, v in platform_service._api_mapping.items():
    print(f"{k}: {v}")