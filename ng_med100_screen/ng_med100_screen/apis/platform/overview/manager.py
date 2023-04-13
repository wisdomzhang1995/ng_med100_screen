from django.db.models import Sum, Count

from model.models import TCase, TCaseExpert, TSiteChargingItem


class OverviewManager(object):
    CASE_MODEL = TCase
    REALTIME_QUERYSET = CASE_MODEL.get_realtime_queryset()
    REGISTERED = 300
    ADMISSIONED = 600
    SIGNED = 800
    STATUS_TYPE = ["已登记", "待接诊", "已签发", "待诊断"]  # 状态<300: 已登记，300，600：待接诊，>=800:已签发，其他：待诊断
    DIAGNOSIS_TYPE_MAP = {
        1: "住院",
        2: "门诊",
        3: "体检",
        4: "两癌筛查",
        5: "普通检查",
    }
    DISEASE_TYPE_MAP = {
        11: "肿瘤(良性)",
        12: "肿瘤(恶性)",
        13: "肿瘤(中间型)",
        14: "肿瘤(不确定)",
        15: "肿瘤(癌前病变)",
    }

    @classmethod
    def statistics_status_count(cls, status_count):
        statistics_status_list = [{"name": name, "count": 0} for name in cls.STATUS_TYPE]
        for status_map in status_count:
            status = status_map["status"]
            count = status_map["count"]
            if status is None:
                continue
            if status < cls.REGISTERED:
                statistics_status_list[0]["count"] = statistics_status_list[0]["count"] + count
            elif cls.REGISTERED <= status <= cls.ADMISSIONED:
                statistics_status_list[1]["count"] = statistics_status_list[1]["count"] + count
            elif status >= cls.SIGNED:
                statistics_status_list[2]["count"] = statistics_status_list[2]["count"] + count
            else:
                statistics_status_list[3]["count"] = statistics_status_list[3]["count"] + count
        return statistics_status_list

    @classmethod
    def get_case_status_count(cls):
        status_count = cls.CASE_MODEL.annotate_field_count(cls.REALTIME_QUERYSET, "status")
        statistics_status_list = cls.statistics_status_count(status_count)
        return statistics_status_list

    @classmethod
    def format_statistic_count_data(cls, field_name, statistic_count_list, format_map=None):
        statistic_count_response_data = []
        for data in statistic_count_list:
            statistic_count_dict = {}
            name = data[field_name]
            if format_map:
                name = format_map.get(name)
            if name is None or name == "":
                continue
            statistic_count_dict["name"] = name
            statistic_count_dict["count"] = data["count"]
            statistic_count_response_data.append(statistic_count_dict)
        return statistic_count_response_data

    @classmethod
    def get_case_diagnosis_type_count(cls):
        annotate_field = "info_diagnosis_type"
        diagnosis_type_list = cls.CASE_MODEL.annotate_field_count(cls.REALTIME_QUERYSET, annotate_field)
        diagnosis_type_count_list = cls.format_statistic_count_data(annotate_field, diagnosis_type_list,
                                                                    cls.DIAGNOSIS_TYPE_MAP)
        return diagnosis_type_count_list

    @classmethod
    def get_case_diagnosis_result(cls):
        annotate_field = "disease_type"
        diagnosis_result_list = cls.CASE_MODEL.annotate_field_count(cls.REALTIME_QUERYSET, annotate_field)
        diagnosis_result_count_list = cls.format_statistic_count_data(annotate_field, diagnosis_result_list,
                                                                      cls.DISEASE_TYPE_MAP)
        return diagnosis_result_count_list

    @classmethod
    def get_active_expert_count(cls):
        active_expert_count = TCaseExpert.search().values("account_id").distinct().count()
        return active_expert_count

    @classmethod
    def get_total_cast_count(cls):
        total_cast_count = cls.CASE_MODEL.search().count()
        return total_cast_count

    @classmethod
    def get_total_charging(cls):
        total_charging = TSiteChargingItem.search().aggregate(total_income=Sum("charging_item_price"))
        total_charging_num = total_charging["total_income"] // 10000
        return total_charging_num

    @classmethod
    def get_case_statistics_count(cls):
        return {
            "active_experts_count": cls.get_active_expert_count(),
            "cast_count": cls.get_total_cast_count(),
            "total_income": cls.get_total_charging()
        }
