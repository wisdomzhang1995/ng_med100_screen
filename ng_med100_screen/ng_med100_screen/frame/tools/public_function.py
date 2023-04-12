import datetime


def format_time(format_time):
    try:
        return format_time.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return ""


def str2datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')