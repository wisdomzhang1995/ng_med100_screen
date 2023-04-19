import json
from datetime import datetime
from decimal import Decimal


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, bytes):
            return obj.decode("utf-8")
        if isinstance(obj, Decimal):
            try:
                return float(obj)
            except:
                return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)