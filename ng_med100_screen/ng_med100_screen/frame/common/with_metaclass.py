

def gen_meta(name, *classes, **conf):
    return type(name, tuple(classes), conf)


def with_metaclass(cls, *classes, **conf):
    base_classes = [cls]
    base_classes.extend(classes)
    conf.update(cls.__dict__)
    conf.update({"__dict__": cls.__dict__})
    new_class = gen_meta("tep" + cls.__name__, *base_classes, **conf)
    return new_class
