from clientpy3 import *
import utils
import time

u = 'BSOD'
pw = 'Alboucai'


config = get_config(u,pw)
c_dic = utils.config_parser(config)

#initialize the dictionaries
mine_db = {}
worm_db = {}

while True:
    status = get_status(u,pw)
    data = utils.status_parser(status[0])
    if data['wormholes']:
        worm_x, worm_y = data['wormholes'][0][1], data['wormholes'][0][2]
        worm_db[worm_x+worm_y] = (worm_x, worm_y)
        print(worm_db[worm_x+worm_y], 'worm')
    if data['mines']:
        mine_x, mine_y = data['mines'][0][1], data['mines'][0][2]
        mine_db[mine_x+mine_y] = (mine_x, mine_y)
        print(mine_db[mine_x+mine_y], 'mine')
    scan_data = utils.scan(u,pw,data,c_dic) 
    output = utils.scan_parser(scan_data)
    if output == 0:
        continue
    
    '''
    if output['wormholes']:
        worm_x, worm_y = output['wormholes'][0], output['wormholes'][1]
        worm_db[worm_x+worm_y] = (worm_x, worm_y)   
    if output['mines']:
        mine_x, mine_y = output['mines'][0], output['mines'][1]
        mine_db[mine_x+mine_y] = (mine_x, mine_y)
    '''  
