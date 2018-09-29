from clientpy3 import *
import utils
import time


u = 'BSOD'
pw = 'Alboucai'


#run(u, pw,'BRAKE')
num = 3.14 *1/3

config = get_config(u,pw)
c_dic = utils.config_parser(config)

for i in c_dic:
    print (i, c_dic[i])
'''
while True:
    status = get_status(u,pw)
    data = utils.status_parser(status[0])
    pos = data['position']
    utils.scan(data) 
    utils.move(u,pw, 3.14-1, 0.4+0.2)
    #run(u, pw, 'BOMB '+ pos[0] + ' '+ pos[1] + '1')
    time.sleep(1.5)
'''
