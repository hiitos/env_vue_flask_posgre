import datetime

def strftime(p_datetime):
    """
    stringを返却
    """
    print(f"strftime {type(p_datetime)}")
    if (type(p_datetime) == "datetime.datetime"):
        return str(p_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    if (type(p_datetime) == "NoneType"):
        return ""
    else:
        return str(p_datetime)

def strptime(string_time):
    """
    datetimeを返却
    """
    print(f"strptime {type(string_time)}")
    if (type(string_time) == "datetime.datetime"):
        return string_time
    elif (type(string_time) == "str"):
        print(f"common.strptime string_time={string_time}")
        return datetime.datetime.strptime(string_time, "%Y-%m-%d %H:%M:%S")
    else:
        print(f"common.strptime not string_time={string_time}")
        return datetime.datetime.strptime(string_time, "%Y-%m-%d %H:%M:%S")
