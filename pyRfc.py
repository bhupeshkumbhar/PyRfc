#/H/49.248.130.31
from pyrfc import Connection
conn = Connection(ashost='192.168.2.101', sysnr='00', client='200', sysid='DEV' ,saprouter='/H/49.248.130.31', user='abap_user', passwd='Zenuacpl@321')
result = conn.call('STFC_CONNECTION', REQUTEXT=u'Hello SAP!')
print (result)