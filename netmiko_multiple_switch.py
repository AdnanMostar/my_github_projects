#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.193',
    'username': 'cisco',
    'password': 'AdnanKahric_68',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.198',
    'username': 'cisco',
    'password': 'AdnanKahric_68',
}

iosv_l2_s3 = {
    'device_type': 'cisco_nxos',
    'ip': '192.168.255.217',
    'username': 'admin',
    'password': 'Adnan_Kahric',
}

with open('iosv_l2_config1') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output) 
