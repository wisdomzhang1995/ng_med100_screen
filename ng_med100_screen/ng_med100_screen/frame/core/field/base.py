# coding=UTF-8

import datetime
import json
import re

from ng_med100_screen.frame.common.dict_wrapper import DictWrapper


class BaseField(object):

    def __init__(self, desc, choices=None, is_required=True, default=None,
                 reprocess=None, parse_it=True):
        self._desc = desc
        self._choices = choices
        self._default = default
        self._is_required = is_required
        self._parse_it = parse_it
        self._choice_mapping = dict(self._choices) if self._choices else None
        if reprocess is None:
            self._reprocess = []
        else:
            self._reprocess = reprocess if type(reprocess) == list else [
                reprocess]

    def json_loads(self, value):
        try:
            value = json.loads(value)
        except Exception as e:
            raise Exception("parameters is not json data")
        else:
            return value

    def _check_choices(self, value):
        if self._choice_mapping:
            if value not in self._choice_mapping:
                raise NotImplementedError(
                    f'<{value}> is not in choices: {self._choices}')
        return value

    def get_type(self):
        return self.__class__.__name__.lower().replace("field", "")

    def get_desc(self):
        return self._desc if self._is_required else "{} - (选参)".format(
            self._desc)

    def get_choices(self):
        return self._choice_mapping

    def is_required(self):
        return self._is_required

    def parse_it(self):
        return self._parse_it

    def get_default(self):
        return self._default

    def parse_before(self, value):
        return value

    def parsing(self, value):
        raise NotImplementedError('Please implement this interface in subclass')

    def parse_after(self, value):
        return self._check_choices(value)

    def parse(self, value):
        value = self.parse_before(value)
        value = self.parsing(value)
        value = self.parse_after(value)
        return value

    def format_before(self, value):
        return value

    def formatting(self, value):
        raise NotImplementedError('Please implement this interface in subclass')

    def format_after(self, value):
        value = self._check_choices(value)
        return value

    def reprocess(self, value):
        result = value
        if self._reprocess:
            for func in self._reprocess:
                result = func(result)
        return result

    def format(self, value):
        value = self.format_before(value)
        value = self.formatting(value)
        value = self.format_after(value)
        return value


class BooleanField(BaseField):

    def parsing(self, value):
        if value:
            return True
        else:
            return False

    def formatting(self, value):
        if value:
            return True
        else:
            return False


class CharField(BaseField):

    def parsing(self, value):
        return str(value)

    def formatting(self, value):
        if value is None:
            return ""
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return str(value)


class IntField(BaseField):

    def parsing(self, value):
        if value == "":
            return 0
        return int(value)

    def formatting(self, value):
        result = 0
        try:
            result = int(value)
        except ValueError as _:
            pass
        return result


class FloatField(BaseField):

    def parsing(self, value):
        return float(value)

    def formatting(self, value):
        return float(value)


class JsonField(BaseField):

    def parsing(self, value):
        return json.loads(value)

    def formatting(self, value):
        return json.dumps(value)


class DateField(BaseField):

    def parsing(self, value):
        value_time = datetime.datetime.strptime(value, '%Y-%m-%d')
        value_time_day = datetime.date(value_time.year, value_time.month,
                                       value_time.day)
        return value_time_day

    def formatting(self, value):
        if not isinstance(value, datetime.date):
            return None
        return value.strftime('%Y-%m-%d')


class DatetimeField(BaseField):

    def parsing(self, value):
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(e)
        return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    def formatting(self, value):
        if not isinstance(value, datetime.datetime):
            return None
        return value.strftime("%Y-%m-%d %H:%M:%S")


class DictField(BaseField):

    def __init__(self, conf, *args, **kwargs):
        super(DictField, self).__init__(*args, **kwargs)
        if self.parse_it():
            if type(conf) is not dict:
                raise Exception("DictField need dict type value")

            for key, value in conf.items():
                if not isinstance(value, BaseField):
                    raise Exception("DictField is just to load BaseField")
                setattr(self, key, value)

    def get_fields(self):
        if not hasattr(self, '_fields'):
            self._fields = {key: value for key, value in self.__dict__.items()
                            if
                            isinstance(value, BaseField)}
        return self._fields

    def parsing(self, value):
        if type(value) is str:
            value = self.json_loads(value)

        if type(value) is dict:
            fields = self.get_fields()
            result = {}
            for key, helper in fields.items():
                if key not in value:
                    if helper.is_required():
                        raise Exception("parameter '{}' lost".format(key))
                    else:
                        continue
                if helper.get_choices() is not None and \
                        value[key] not in helper.get_choices():
                    raise Exception(
                        f"parameter:'{key}', value: '{value[key]}' not in choices: "
                        f"{helper.get_choices()}")

                try:
                    cur_value = helper.parsing(value[key])
                except Exception as e:
                    raise Exception(
                        "parameter '{}' format error: {}".format(key, e))
                else:
                    result[key] = cur_value
            return DictWrapper(result)

        raise Exception("parameter is not dict")

    def formatting(self, value):
        if type(value) is not dict:
            raise Exception("parameter is not dict")

        fields = self.get_fields()
        result = {}
        for key, helper in fields.items():
            if key not in value:
                if helper.is_required():
                    if helper.get_default() is None:
                        raise Exception("parameter '{}' lost".format(key))
                    else:
                        value[key] = helper.get_default()
                else:
                    continue
            if helper.get_choices() is not None and \
                    value[key] not in helper.get_choices():
                raise Exception(
                    f"parameter '{key}' not in choices: "
                    f"{helper.get_choices()}")

            try:
                cur_value = helper.formatting(value[key])
            except Exception as e:
                raise Exception(
                    "parameter '{}' format error, e = {}".format(key, e))
            else:
                result[key] = cur_value
        return DictWrapper(result)

    def reprocess(self, value):
        fields = self.get_fields()
        result = {}
        for key, helper in fields.items():
            if key not in value:
                continue

            try:
                cur_value = helper.reprocess(value[key])
            except Exception as e:
                raise Exception(
                    "parameter '{}' format error, e = {}".format(key, e))
            else:
                result[key] = cur_value
        return DictWrapper(result)


class ListField(BaseField):

    def __init__(self, fmt, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)
        self._fmt = fmt

    def get_fmt(self):
        return self._fmt

    def parsing(self, value):
        if type(value) is str:
            value = self.json_loads(value)

        if type(value) is list:
            return [self._fmt.parse(cur_value) for cur_value in value]

        raise Exception("parameter is not list")

    def formatting(self, value):
        if type(value) is not list:
            raise Exception("parameter is not list")

        return [self._fmt.formatting(cur_value) for cur_value in value]

    def reprocess(self, value):
        return [self._fmt.reprocess(cur_value) for cur_value in value]


class FileField(BaseField):

    def parsing(self, value):
        return value

    def formatting(self, value):
        return value


class MobileField(BaseField):

    def parsing(self, value):
        return str(value)

    def formatting(self, value):
        if value:
            p = re.compile(r'(\d{3})(\d{4})(\d{4})')
            value = p.sub(r'\1****\3', value)
        return value


# case 1
# class NewDictField(BaseField):
#
#     def parsing(self, value):
#         return value
#
#     def formatting(self, value):
#         return value

# case 2

NewDictField = type('NewDictField', (BaseField,),
                    {'parsing': lambda _, value: value,
                     'formatting': lambda _, value: value})

MixedListField = type("MixedListField", (BaseField,),
                      {'parsing': lambda _, value: value,
                       'formatting': lambda _, value: value})
