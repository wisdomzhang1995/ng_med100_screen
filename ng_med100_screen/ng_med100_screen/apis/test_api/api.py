from ng_med100_screen.frame.common.with_metaclass import with_metaclass
from ng_med100_screen.frame.core.api.authorization import NoAuthrizedApi
from frame.core.api.request_parse import RequestFieldSet, RequestField
from frame.core.api.response_parse import ResponseFieldSet, ResponseField
from ng_med100_screen.frame.core.field.base import DictField, IntField, CharField, DatetimeField, ListField
from model.models import TMoneySiteCycle


class LogProtocol(NoAuthrizedApi):
    """日志协议列表"""

    request = with_metaclass(RequestFieldSet)
    request.log_type = RequestField(
        CharField,
        desc="日志类型 NAT: nat, POLICY, SESSION: 会话, DOS: 安全, LEARN, VUL: 漏洞日志, ACL: acl日志, FLOW_CTRL: 流控日志, "
             "IP_MAC: ip_mac日志, INDUS_TPL: 工业模板",
    )
    response = with_metaclass(ResponseFieldSet)

    response.data = ResponseField(ListField, desc="日志信息", fmt=CharField(desc=""))

    @classmethod
    def get_desc(cls):
        return "日志协议列表"

    @classmethod
    def get_author(cls):
        return "zs"

    @classmethod
    def get_protocol_num(cls):
        return "12354"

    @classmethod
    def log_required(cls):
        return False

    def execute(self, request):
        protocol_list = [
            "hopopts",
            "icmp",
            "igmp",
            "ggp",
        ]
        learn_list = ["bacnet-ip", "dnp3", "ethernet-ip", "fins", "iec104", "mms", "modbus", "opc", "opcua", "profinet",
                      "s7", "dns", "ftp", "http", "pop3", "smtp", "mqtt"]
        data = {
            "NAT": protocol_list,
            # "POLICY": protocol_list,
            "SESSION": protocol_list,
            "DOS": protocol_list,
            "LEARN": learn_list,
            "LIMIT": protocol_list,
            "VUL": protocol_list,
            "ACL": protocol_list,
            "FLOW_CTRL": protocol_list,
            "INDUSTRY_POLICY": learn_list,
            "IP_MAC": protocol_list,
            "INDUS_TPL": protocol_list,
        }
        return data.get(request.log_type) if data.get(request.log_type) else []
        # return "ggp"

    def fill(self, response, data):
        response.data = data
        return response