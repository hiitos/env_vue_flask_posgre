from model.Status import status_dict
from model import Status

def test_getName():
    assert Status.getName(0,status_dict) == 'NEW'
    assert Status.getName(1,status_dict) == 'ACTIVE'
    assert Status.getName(2,status_dict) == 'INACTIVE'
    assert Status.getName(3,status_dict) == 'DELETE'
    assert Status.getName(4,status_dict) == 'ERROR'

def test_getStatusName():
    assert Status.getStatusName('0') == 'NEW'
    assert Status.getStatusName('1') == 'ACTIVE'
    assert Status.getStatusName('2') == 'INACTIVE'
    assert Status.getStatusName('3') == 'DELETE'
    assert Status.getStatusName('a') == 'ERROR'

def test_getKey():
    assert Status.getKey('NEW', status_dict) == 0
    assert Status.getKey('ACTIVE', status_dict) == 1
    assert Status.getKey('INACTIVE', status_dict) == 2
    assert Status.getKey('DELETE', status_dict) == 3
    assert Status.getKey('ERROR', status_dict) == -1
    
def test_getStatusKey():
    assert Status.getStatusKey('NEW') == 0
    assert Status.getStatusKey('ACTIVE') == 1
    assert Status.getStatusKey('INACTIVE') == 2
    assert Status.getStatusKey('DELETE') == 3
    assert Status.getStatusKey('AAA') == -1

def test_getApprovalName():
    assert Status.getApprovalName(0) == 'NOT_APPROVED'
    assert Status.getApprovalName(1) == 'APPROVED'    
    assert Status.getApprovalName(3) == 'ERROR'
