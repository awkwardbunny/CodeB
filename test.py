from clientpy3 import *
import utils
import time

u = 'BSOD'
pw = 'Alboucai'

#run(u, pw,'BRAKE')
num = 3.14 *1/3

config = get_config(u,pw)
c_dic = utils.config_parser(config)

while True:
    status = get_status(u,pw)
    data = utils.status_parser(status[0])
    pos = data['position']
    scan_data = utils.scan(u,pw,data,c_dic) 
    output = utils.scan_parser(scan_data)
    print(scan_data)
    print(output)
    time.sleep(5.1)
