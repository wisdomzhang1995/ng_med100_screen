import threading

thread_context_map = {}


def get_ident():
    return threading.currentThread().ident


class RequestObj(object):
    ...


class RequestContext(object):

    def __enter__(self):
        pass

    @staticmethod
    def push():
        ident = get_ident()
        request_obj = RequestObj()
        thread_context_map[ident] = request_obj

    @staticmethod
    def pop():
        thread_context_map.pop(get_ident())

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.pop()
        except KeyError as e:
            print("shun ------------------------------>  no such ident")
        if exc_type:
            raise Exception(exc_type, exc_val, exc_tb)


class GlobalRequest(object):

    def __getattr__(self, name):
        ident = get_ident()
        request_obj = thread_context_map.get(ident, None)
        if not request_obj:
            raise Exception(f"ident:{ident} is not exist")
        else:
            return getattr(request_obj, name)

    def __setattr__(self, key, value):
        ident = get_ident()
        request_obj = thread_context_map.get(ident, None)
        if not request_obj:
            raise Exception(f"ident:{ident} is not exist")
        else:
            return setattr(request_obj, key, value)

_request = GlobalRequest()


