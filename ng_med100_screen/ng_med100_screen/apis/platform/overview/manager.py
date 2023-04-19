import datetime

from django.conf import settings
from django.db.models import Sum, Count

from apis.platform.overview.sql import *
from frame.tools.database.sql_operator import MysqlManager
from frame.tools.public_function import format_time
from model.models import TCase, TCaseExpert, TSiteChargingItem


class OverviewManager(object):
    CASE_MODEL = TCase
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

    CELL_SAMPLE_TYPE_MAP = {
            20: "宫颈细胞",
            21: "脱落细胞",
            22: "细针穿刺",
            23: "其他类型",
     }

    @classmethod
    def get_time_range(cls):
        start_time = datetime.datetime.now()
        print("QWWWWWWWWWWWWWWWWWWWWWW", start_time)
        end_time = start_time - datetime.timedelta(days=2)
        return start_time, end_time

    @classmethod
    def get_realtime_queryset(cls, model):
        if settings.DEBUG:
            return model.search()
        start_time, end_time = cls.get_time_range()
        return model.search(create_time__gte=start_time, create_time__lte=end_time)

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
        status_count = cls.CASE_MODEL.annotate_field_count(cls.get_realtime_queryset(cls.CASE_MODEL), "status")
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
        realtime_queryset = cls.get_realtime_queryset(cls.CASE_MODEL)
        diagnosis_type_list = cls.CASE_MODEL.annotate_field_count(realtime_queryset, annotate_field)
        diagnosis_type_count_list = cls.format_statistic_count_data(annotate_field, diagnosis_type_list,
                                                                    cls.DIAGNOSIS_TYPE_MAP)
        return diagnosis_type_count_list

    @classmethod
    def get_case_diagnosis_result(cls):
        annotate_field = "disease_type"
        realtime_queryset = cls.get_realtime_queryset(cls.CASE_MODEL)
        diagnosis_result_list = cls.CASE_MODEL.annotate_field_count(realtime_queryset, annotate_field)
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
        db_conn = MysqlManager()
        sql = cls.format_sql_of_debug(total_income_sql, cls.format_realtime())
        result = db_conn.execute_fetchone(sql)
        total_charging_num = round(result["total_income"] / 10000, 1)
        return total_charging_num

    @classmethod
    def get_case_statistics_count(cls):
        return {
            "active_experts_count": cls.get_active_expert_count(),
            "cast_count": cls.get_total_cast_count(),
            "total_income": cls.get_total_charging()
        }

    @classmethod
    def format_sql_of_debug(cls, sql, condition=""):
        if settings.DEBUG:
            format_sql = sql.format(condition="")
        else:
            format_sql = sql.format(condition=condition)
        return format_sql

    @classmethod
    def format_sql_result(cls, result):
        return list(result)

    @classmethod
    def format_realtime(cls):
        start_time, end_time = cls.get_time_range()
        return f" and create_time between {format_time(start_time)} and {format_time(end_time)}"

    @classmethod
    def get_case_sub_specialty(cls):
        db_conn = MysqlManager()
        sql = cls.format_sql_of_debug(sub_specialty_sql, cls.format_realtime())
        result = db_conn.execute_fetchall(sql)
        return cls.format_statistic_count_data("system_name", cls.format_sql_result(result))

    @classmethod
    def format_site_dynamics(cls, result1, result2, result3):
        for r1 in result1:
            for r2 in result2:
                if r1["name"] == r2["name"]:
                    r1.update(r2)
                    for r3 in result3:
                        if r1["name"] == r3["name"]:
                            r1.update(r3)
                    else:
                        r1["numerator_count"] = 0
            else:
                r1["immunostaining_count"] = 0
                for r3 in result3:
                    if r1["name"] == r3["name"]:
                        r1.update(r3)
                else:
                    r1["numerator_count"] = 0
            r1["case_count"] = r1["tissue_count"] + r1["cell_count"] + r1["frost_count"] + r1["immunostaining_count"] + r1["numerator_count"]

        return result1

    @classmethod
    def get_case_site_dynamics(cls):
        # 三个表分开写，程序合并到一块
        db_conn = MysqlManager()
        cast_sql = cls.format_sql_of_debug(site_dynamics_cast_sql, cls.format_realtime())
        advice_sql = cls.format_sql_of_debug(site_dynamics_advice_sql, cls.format_realtime())
        molecular_sql = cls.format_sql_of_debug(site_dynamics_molecular_sql, cls.format_realtime())
        cast_result = db_conn.execute_fetchall(cast_sql)
        advice_result = db_conn.execute_fetchall(advice_sql)
        molecular_result = db_conn.execute_fetchall(molecular_sql)
        result = cls.format_site_dynamics(cast_result, advice_result, molecular_result)
        print("108 bingli----------------", len(result))
        return result

    @classmethod
    def get_specimen_circulation(cls):
        db_conn = MysqlManager()
        applicate_sql = cls.format_sql_of_debug(sql1, cls.format_realtime())
        single_sample_sql = cls.format_sql_of_debug(sql2, cls.format_realtime())
        frozen_sample_sql = cls.format_sql_of_debug(sql3, cls.format_realtime())
        case_slide_sql = cls.format_sql_of_debug(sql4, cls.format_realtime())
        case_advice_sql = cls.format_sql_of_debug(sql5, cls.format_realtime())
        applicate_result = db_conn.execute_fetchone(applicate_sql)
        single_sample_result = db_conn.execute_fetchone(single_sample_sql)
        frozen_sample_result = db_conn.execute_fetchone(frozen_sample_sql)
        case_slide_result = db_conn.execute_fetchone(case_slide_sql)
        case_advice_result = db_conn.execute_fetchone(case_advice_sql)
        name_list = ["申请单", "常规取材", "冰冻取材", "常规玻片", "技术医嘱"]
        return [
            {"name": "申请单", "count": applicate_result["count"]},
            {"name": "常规取材", "count": single_sample_result["count"]},
            {"name": "冰冻取材", "count": frozen_sample_result["count"]},
            {"name": "常规玻片", "count": case_slide_result["count"]},
            {"name": "技术医嘱", "count": case_advice_result["count"]},
                ]

    @classmethod
    def get_cell_count(cls):
        annotate_field = "sample_type"
        realtime_queryset = cls.get_realtime_queryset(cls.CASE_MODEL)
        queryset = realtime_queryset.filter(case_type=2, is_delete=0)
        diagnosis_result_list = cls.CASE_MODEL.annotate_field_count(queryset, annotate_field)
        diagnosis_result_count_list = cls.format_statistic_count_data(annotate_field, diagnosis_result_list,
                                                                      cls.CELL_SAMPLE_TYPE_MAP)
        return diagnosis_result_count_list
