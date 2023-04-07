
class AdapterField(object):
    _field = None

    def __init__(self, field_cls, *args, **kwargs):
        self._field = field_cls(*args, **kwargs)

    def get_field(self):
        return self._field

    def get_choices(self):
        return self.get_field()._choices

    def get_default(self):
        return self.get_field()._default

    def get_type(self):
        return self.get_field().get_type()

    def get_desc(self):
        return self.get_field().get_desc()



class AdapterFieldSet(object):
    _fields = None
    _field_cls = None

    @classmethod
    def get_fields(cls):
        cls._fields = {}
        for name in dir(cls):
            value = getattr(cls, name)
            if isinstance(value, cls._field_cls):
                cls._fields[name] = value
        print("==========================", cls._fields)
        return cls._fields
