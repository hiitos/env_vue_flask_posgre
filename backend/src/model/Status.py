# 0. NEW
# 1. ACTIVE
# 2. INACTIVE
# 3. DELETE

status_dict = {
    '0':'NEW',
    '1':'ACTIVE',
    '2':'INACTIVE',
    '3':'DELETE'
}

def getName(key, p_dict):
    return p_dict.get(str(key), "ERROR")

def getStatusName(key):
    return getName(str(key), status_dict)

def getKey(value, p_dict):
    keys = [k for k, v in p_dict.items() if v == value]
    if (len(keys) == 1):
        return int(keys[0])
    else:
        return -1
   
def getStatusKey(value):
    return getKey(value, status_dict)
    
# 0. NOT_APPROVED
# 1. APPROVED

approval_dict = {
    '0' : 'NOT_APPROVED',
    '1' : 'APPROVED'
}

def getApprovalName(status):
    if status == 0:
        return "NOT_APPROVED"
    elif status == 1:
        return "APPROVED"
    else:
        return "ERROR"

    
