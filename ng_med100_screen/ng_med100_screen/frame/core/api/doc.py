# -*- coding: utf-8 -*-
"""
                                      /
 __.  , , , _  _   __ ______  _    __/  __ ____  _,
(_/|_(_(_/_</_/_)_(_)/ / / <_</_  (_/_ (_)/ / <_(_)_
                                                 /|
                                                |/
"""

import inspect
from collections import defaultdict

from frame.core.field.base import ListField, DictField

dict_factory = lambda: defaultdict(dict_factory)


# def dict_factory():
#     return defaultdict(dict_factory)

class DefaultSample:
    @staticmethod
    def null():
        """
        this api has no sample.
        contact relative developer to implement this.

         __.  , , , _  _   __ ______  _    __/  __ ____  _,
        (_/|_(_(_/_</_/_)_(_)/ / / <_</_  (_/_ (_)/ / <_(_)_
                                                         /|
                                                        |/
        """


class ApiDocBuilder(object):

    def __init__(self, api):
        self._api = api

    def get_api(self):
        return self._api

    def generate(self):
        raise NotImplementedError(
            'Please imporlement this interface in subclass')


class TextApiDoc(ApiDocBuilder):
    EXCLUDE_ATTRS = ["x_file_info", "x_headers"]

    def generate(self):
        content_list = [
            self.generate_author(),
            self.generate_version(),
            "",
        ]
        return '\n'.join([
            self.generate_service_flag(),
            self.generate_author(),
            self.generate_version(),
            "",
            self.generate_desc(),
            self.generate_protocol_num(),
            "",
            self.generate_params(),
            "",
            "",
            self.generate_return(),
            "",
            "",
            self.generate_sample()
        ])

    def generate_service_flag(self):
        return "@flag : {}".format(self.get_api().get_service().get_flag())

    def generate_protocol_num(self):
        try:
            proc_str = "@protocol_num : {}".format(
                self.get_api().get_protocol_num())
        except:
            proc_str = '@protocol_num : ----'
        return proc_str

    def generate_author(self):
        return "@author : {}".format(self.get_api().get_author())

    def generate_version(self):
        return "@version : {}".format(self.get_api().get_version())

    def generate_desc(self):
        return "@desc : {}".format(self.get_api().get_desc())

    def generate_return_desc(self, field):
        fmt_str = "{} # {}"
        tmp_str = fmt_str.format(field.get_type(), field.get_desc())
        choices = field.get_choices()
        if choices:
            tmp_str += " 如：" + ' '.join(
                "、".join(map(str, [key, value])) for key, value in choices)
        return tmp_str

    def generate_param_desc(self, field):
        fmt_str = "{} # {}"
        tmp_str = fmt_str.format(field.get_type(), field.get_desc())
        choices = field.get_choices()
        if choices:
            tmp_str += "; 可选值：" + str(choices)

        default = field.get_default()
        if default:
            tmp_str += " 默认值：" + default

        is_need = field.is_need()
        if not is_need:
            tmp_str += " (选填)"

        return tmp_str

    def generate_field(self, field, fields, level):
        fill_flag = " " * 8
        cur_flag = fill_flag * level
        next_flag = fill_flag * (level + 1)

        if isinstance(field, DictField):
            fields.append(cur_flag + '{  # ' + field.get_desc())
            sorted_fileds = dict(sorted(field.get_fields().items(), key=lambda x: x[0]))
            # sorted_fileds = field.get_fields()
            for sub_name, sub_field in sorted_fileds.items():
                fmt_str = next_flag + "{} : {} # {}"
                tmp_str = fmt_str.format(sub_name, sub_field.get_type(),
                                         sub_field.get_desc())
                choices = sub_field.get_choices()
                if choices:
                    tmp_str += "; 可选值：" + str(choices)
                fields.append(tmp_str)
                self.generate_field(sub_field, fields, level + 1)
            fields.append(cur_flag + '}')

        elif isinstance(field, ListField):
            fields.append(cur_flag + '[')
            sub_field = field.get_fmt()
            if not isinstance(sub_field, DictField) and not isinstance(
                    sub_field, ListField):
                fmt_str = next_flag + "{} # {}"
                tmp_str = fmt_str.format(sub_field.get_type(),
                                         sub_field.get_desc())
                fields.append(tmp_str)
            else:
                self.generate_field(sub_field, fields, level + 1)
            fields.append(next_flag + '......')
            fields.append(cur_flag + ']')

    def generate_params(self):
        fmt_str = "@param : {} - {}"
        api = self.get_api()
        fields = []
        for name, field in api.get_request_fields().items():
            tmp_str = fmt_str.format(name, self.generate_param_desc(field))
            fields.append(tmp_str)

            org_field = field.get_field()
            self.generate_field(org_field, fields, level=1)

        return '\n'.join(fields)

    def generate_return(self):
        fmt_str = "@return : {} - {}"
        api = self.get_api()
        fields = []
        for name, field in api.get_response_fields().items():
            if name in self.EXCLUDE_ATTRS:
                continue
            tmp_str = fmt_str.format(name, self.generate_return_desc(field))
            org_field = field.get_field()
            fields.append(tmp_str)
            self.generate_field(org_field, fields, level=1)

        return '\n'.join(fields)

    def generate_sample(self):
        almighty_dividing_line = "-" * 38
        prefix = almighty_dividing_line + " awesome  sample (Python) " + almighty_dividing_line + "\n"
        return prefix

        # source_code = inspect.getsource(
        #     ApiCallSourceCodeMapping.MAPPING.get(self.get_api().get_name(),
        #                                          DefaultSample.null))
        # source_code = "\n".join(source_code.split("\n")[1:])
        #
        # prefix = almighty_dividing_line + " awesome  sample (Python) " + almighty_dividing_line + "\n"
        # return prefix + source_code


class SwaggerDoc():
    VERSION = "2.0"
    SCHEMES = ['https']
    BASEPATH = "/frame"
    HEAD_INFO = {
        "title": "ifw",
        "version": "last",
        "description": "防火墙项目"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = self.VERSION
        self.info = self.HEAD_INFO
        self.schemes = self.SCHEMES
        self.tags = []
        self.required = []
        self.paths = dict_factory()

    def convert_filed_type(self, field):
        """
        自定义字段类型转 open api 对应的字类型
        """
        return {
            'int': 'number',
            'float': 'number',
            'boolean': 'boolean',
            'list': 'array',
            'dict': 'object',
        }.get(field.get_type(), 'string')

    def add_tags(self, tag):
        """
        增加模块tags
        """
        if {
            "name": tag,
            "description": tag
        } not in self.tags:
            self.tags.append({
                "name": tag,
                "description": tag
            })

    def generate_field(self, properties, field):
        """
        提取字信息
        """
        if isinstance(field, DictField):
            sub_properties = dict_factory()
            required = []
            for sub_name, sub_field in field.get_fields().items():
                self.generate_field(sub_properties[sub_name], sub_field)
                if sub_field.is_required():
                    required.append(sub_name)
            properties['type'] = self.convert_filed_type(field)
            properties['description'] = field.get_desc()
            properties['properties'] = sub_properties
            # 处理每一个子项对应的 required 字段
            if required:
                properties['required'] = required

        elif isinstance(field, ListField):
            properties['type'] = self.convert_filed_type(field)
            properties['description'] = field.get_desc()
            sub_field = field.get_fmt()
            if isinstance(sub_field, DictField) or isinstance(sub_field,
                                                              ListField):
                sub_properties = dict_factory()
                self.generate_field(sub_properties, sub_field)
                properties['items'] = sub_properties
            else:
                properties['items']['type'] = self.convert_filed_type(sub_field)

        else:
            properties['type'] = self.convert_filed_type(field)
            properties['description'] = field.get_desc()

    def generate_parameters_properties(self, api):
        """
        生成 response 的 properties 信息
        """
        properties = dict_factory()
        required = []
        for field_name, field in api.get_request_fields().items():
            org_field = field.get_field()
            self.generate_field(properties[field_name], org_field)

            if org_field.is_required():
                required.append(field_name)
        return properties, required

    def generate_response_properties(self, api):
        """
        生成 response 的 properties 信息
        """
        properties = dict_factory()
        required = []

        for field_name, field in api.get_response_fields().items():
            org_field = field.get_field()
            self.generate_field(properties[field_name], org_field)

            if org_field.is_required():
                required.append(field_name)
        return properties, required

    def fill_paths_post_base(self, post_base, api):
        """
        填充 paths 里面的基础信息
        """
        post_base['summary'] = api.get_desc()
        post_base['description'] = ''
        post_base['tags'] = [api.get_name().split('/')[0]]
        post_base['consumes'] = ["application/json"]

    def fill_paths_post_parameter(self, post_base, api):
        """
        填充 paths 里面的 parameter 信息
        """
        parameter = dict_factory()
        parameter['name'] = 'root'
        parameter['in'] = 'body'
        parameter['schema']['type'] = "object"
        properties, required = self.generate_parameters_properties(api)
        parameter['schema']['properties'] = properties
        if required:
            parameter['schema']['required'] = required
        post_base['parameters'] = [parameter]

    def fill_paths_post_response(self, post_base, api):
        """
        填充 paths 里面的 response 信息
        """
        post_base['responses']['200']['description'] = "successful"
        post_base['responses']['200']['schema']['type'] = "object"
        properties, required = self.generate_response_properties(api)
        post_base['responses']['200']['schema']['properties'] = properties
        if required:
            post_base['responses']['200']['schema']['required'] = required

    def generate_paths(self, api):
        """
        生成文件对应的 paths 信息
        """
        url = '/' + api.get_name()
        self.add_tags(api.get_name().split('/')[0])
        self.paths[url]['post'] = dict_factory()
        self.fill_paths_post_base(self.paths[url]['post'], api)
        self.fill_paths_post_parameter(self.paths[url]['post'], api)
        self.fill_paths_post_response(self.paths[url]['post'], api)
