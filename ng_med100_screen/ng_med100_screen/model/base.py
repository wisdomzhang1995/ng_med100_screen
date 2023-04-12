import datetime
from itertools import chain
from django.db.models import *
from django.utils import timezone
from django.forms import model_to_dict, fields_for_model
import traceback
from collections import Iterable


class BaseModel(Model):

    class Meta:
        abstract = True

    @classmethod
    def create(cls, **kwargs):
        valid_keys = set(field.name for field in cls._meta.fields)
        default = {attr: val for attr, val in kwargs.items() if
                   attr in valid_keys}
        try:
            return cls.objects.create(**default)
        except Exception as e:
            raise e

    @classmethod
    def get_by_id(cls, _id):
        try:
            relations = [field.name for field in cls.get_relationship_fields()]
            return cls.objects.select_related(*relations).get(id=_id)
        except Exception as e:
            raise e
            # return None

    @classmethod
    def get_relationship_fields(cls):
        return [field for field in cls._meta.fields if
                isinstance(field, ForeignKey)]

    @classmethod
    def get_valid_field_name(cls):
        return {field.name: field for field in cls._meta.fields}

    @classmethod
    def query(cls, **search_info):
        relations = [field.name for field in cls.get_relationship_fields()]
        valid_mapping = cls.get_valid_field_name()
        qs = cls.objects.select_related(*relations).filter()

        for key, val in search_info.items():
            if key in valid_mapping:
                field = valid_mapping[key]
                if val or isinstance(field, BooleanField) or \
                        isinstance(field, IntegerField):
                    temp = {}
                    if isinstance(field, AutoField):
                        temp.update({field.name: int(val)})
                    elif isinstance(field, CharField):
                        temp.update({'{}__contains'.format(field.name): val})
                    elif isinstance(field, IntegerField):
                        temp.update({field.name: int(val)})
                    elif isinstance(field, BooleanField):
                        temp.update({field.name: bool(val)})
                    elif isinstance(field, TextField):
                        temp.update({'{}__contains'.format(field.name): val})
                    elif isinstance(field, DateTimeField):
                        # fsy
                        temp.update({field.name: val})
                    elif isinstance(field, DateField):
                        # fsy
                        temp.update({field.name: datetime.date(val.year,
                                                               val.month,
                                                               val.day)})
                    elif isinstance(field, ForeignKey):
                        temp.update({field.name: val})
                    qs = qs.filter(**temp)

        return qs

    def update(self, **kwargs):
        valid_files = []
        valid_keys = self.__class__.get_valid_field_name().keys()
        for attr, val in kwargs.items():
            if attr in valid_keys:
                setattr(self, attr, val)
                valid_files.append(attr)

        try:
            if valid_files:
                self.save()
                for attr in valid_files:
                    kwargs.pop(attr)
            return self
        except Exception as e:
            raise e

    @classmethod
    def search(cls, **kwargs):
        res_qs = cls.objects.filter(**kwargs)
        return res_qs

    @classmethod
    def search_ex(cls, *res_cols, **kwargs):
        res_mapping = cls.search(**kwargs).values(*res_cols)
        return res_mapping

    @classmethod
    def annotate_field_count(cls, queryset, field_name):
        return queryset.values(field_name).annotate(count=Count("*"))

    @classmethod
    def single_col_list(cls, col, flat=True):
        return cls.objects.values_list(col, flat=flat)

    @classmethod
    def search_enhance(cls, *q_funcs):
        return cls.objects.filter(*q_funcs)

    def as_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_field_verbose_name(cls):
        field_dict = {}
        for field in cls._meta.fields:
            field_dict[field.name] = field.verbose_name
        for field in cls._meta.many_to_many:
            field_dict[field.name] = field.verbose_name

        return field_dict

    @classmethod
    def _get_id_row(cls):
        name_set = {field.name for field in cls._meta.fields}
        if 'unique_id' in name_set:
            row = 'unique_id'
        elif 'gid' in name_set:
            row = 'gid'
        else:
            row = 'id'
        return row

    @classmethod
    def gen_show_row(cls):
        name_set = {field.name for field in cls._meta.fields}
        if 'name' in name_set:
            row = 'name'
        else:
            row = cls._get_id_row()
        return row

    @classmethod
    def log_model(cls, instance, fields=None, exclude=None):
        if instance is None:
            return {}
        opts = instance._meta
        if exclude is None:
            exclude = ['refer_count', 'create_time', 'update_time']
        data = {}
        try:
            for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
                if not getattr(f, 'editable', False):
                    continue
                if fields is not None and f.name not in fields:
                    continue
                if exclude and f.name in exclude:
                    continue

                if isinstance(f, (ManyToManyField, ForeignKey)):
                    row = f.remote_field.model.gen_show_row()
                    if isinstance(f, ManyToManyField):
                        objs = list(getattr(instance, f.attname).all())
                        data[f.name] = [getattr(x, row) for x in objs]
                    else:
                        id = getattr(instance, f.attname)
                        obj = f.remote_field.model.objects.filter(id=id).first()
                        data[f.name] = getattr(obj, row) if obj else '空'
                else:
                    data[f.name] = getattr(instance, f.attname)
            return data
        except Exception as e:
            print('产生日志报错->log_model')
            print(traceback.print_exc())
            return {}

    @classmethod
    def pas_log_head(cls, pas_dict):
        notice_id = pas_dict[cls._get_id_row()]
        if 'name' in pas_dict:
            name = pas_dict['name']
            head = f'「名称」: {name}, 「ID」 : {notice_id}, 具体修改为 '
        else:
            head = f'「ID」: {notice_id}, 具体修改为 '
        return head

    @classmethod
    def model_compare(cls, from_obj_dict = None, to_obj_dict = None):
        csp = []
        # 编辑操作
        try:
            field_comment_dict = cls.get_field_verbose_name()
            if from_obj_dict and from_obj_dict:
                for _key, from_value in from_obj_dict.items():
                    to_value = to_obj_dict[_key] or '空'
                    from_value = from_value or '空'
                    if type(from_value) == type(to_value) \
                            and from_value != to_value:
                        csp.append(f'「{field_comment_dict[_key]}」从{from_value}修改为{to_value}')
                    elif type(from_value) != type(to_value) \
                            and str(from_value) != str(to_value):
                        csp.append(f'「{field_comment_dict[_key]}」从{from_value}修改为{to_value}')
                head = cls.pas_log_head(to_obj_dict) if csp else ''
                return head + ','.join(csp)

            # 添加操作
            elif from_obj_dict is None and to_obj_dict:
                for _key, from_value in to_obj_dict.items():
                    to_value = to_obj_dict[_key] or '空'
                    csp.append(f'「{field_comment_dict[_key]}」: {to_value}')
                return ','.join(csp)

            # 无效操作
            else:
                return ''
        except Exception as e:
            print('产生日志报错->model_compare')
            print(traceback.print_exc())
            return ''

    @classmethod
    def format_row(cls, row_list):
        return row_list

    @classmethod
    def delete_info(cls, queries, row=None):
        cs_row = cls._get_id_row() if not row else row
        if isinstance(queries, Iterable):
            deleted_ids = [getattr(x, cs_row) for x in queries]
        else:
            deleted_ids = [getattr(queries, cs_row)]
        deleted_ids = cls.format_row(deleted_ids)
        if deleted_ids:
            return f'「ID」：{deleted_ids}' if not row else f'「{row.upper()}」：{deleted_ids}'
        else:
            return ''