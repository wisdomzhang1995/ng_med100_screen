
class DictWrapper(dict):

    def __getattr__(self, name):
        try:
            return super(DictWrapper, self).__getitem__(name)
        except KeyError:
            raise AttributeError("key %s not found" % name)

    def __setattr__(self, key, value):
        super(DictWrapper, self).__setitem__(key, value)

    def __delattr__(self, name):
        super(DictWrapper, self).__delitem__(name)

    def hasattr(self, name):
        return name in self

    @classmethod
    def load_dict(cls, orig_data):
        """支持将嵌套的dict转成wrapper, e.g.:
        test_dict = {'a':{'b':1,'c':[2,{'e':3}],'f':{'g':4}}}
        ss = DictWrapper.load_dict(test_dict)
        print ss.a.c[0].e
        print ss.a.b
        后续可用
        """
        if isinstance(orig_data, dict):
            dic = {}
            for k, v in orig_data.items():
                dic.update({k: cls.load_dict(v)})
            return cls(dic)
        elif isinstance(orig_data, (list, tuple)):
            return [cls.load_dict(i) for i in orig_data]
        else:
            return orig_data

