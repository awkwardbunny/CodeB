from clientpy3 import *
import utils
import datetime
import time
from get_path import exec_move

u = 'BSOD'
pw = 'Alboucai'


config = get_config(u,pw)
c_dic = utils.config_parser(config)

#initialize the dictionaries
mine_db = {}
worm_db = {}
mine_list = []
#run it first
time1 = datetime.datetime.now()

while True:
    try:
        # print("test")
        try:
            status = get_status(u,pw)

            data = utils.status_parser(status[0])
            # if data['wormholes']:
            #     worm_x, worm_y = data['wormholes'][0][1], data['wormholes'][0][2]
            #     if worm_x+worm_y not in worm_db:
            #         worm_db[worm_x+worm_y] = (worm_x, worm_y)
            #         print('worm seen: ', worm_db[worm_x+worm_y])
            if data['mines']:
                for mine in data['mines']:
                    mine_x, mine_y = mine[1], mine[2]
                    # if (mine_x,mine_y) not in mine_db:
                    #     mine_db[(mine_x,mine_y)] = time.time()
                    #     print('mine seen: ', mine_db[mine_x+mine_y])
                    if (mine_x,mine_y) not in mine_list:
                        mine_list += [(mine_x,mine_y)]
                        print (mine_x,mine_y,"detected!")
            #run a scan every 5 seconds 
            # if (datetime.datetime.now() - time1) > datetime.timedelta(0,5.2):
            #     scan_data = utils.scan(u,pw,data,c_dic) 
            #     output = utils.scan_parser(scan_data)
            #     time1 = datetime.datetime.now()
            #     if output['wormholes']:
            #         worm_x, worm_y = output['wormholes'][0][0], output['wormholes'][0][1]
            #         worm_db[worm_x+worm_y] = (worm_x, worm_y)   
            #         print('wormhole scanned: ', worm_db[worm_x+worm_y])
            #     if output['mines']:
            #         mine_x, mine_y = output['mines'][0][1], output['mines'][0][2]
            #         mine_db[mine_x+mine_y] = (mine_x, mine_y)
            #         # print('mine scanned: ', mine_db[mine_x+mine_y])
        except (TimeoutError):
            pass
    except (IndexError, TypeError):
        continue

    if len(mine_list) >= 5:
        for mine in mine_list:
            print(mine)

            exec_move(u,pw,float(mine[0]),float(mine[1]))
    else:
        utils.move(u,pw,-2,1)

    
