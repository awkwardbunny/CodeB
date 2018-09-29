from clientpy3 import *
import utils
import datetime
import scanner
import time
from get_path import exec_move, min_dist
import random

u = 'BSOD'
pw = 'Alboucai'

print('starting')
cdic = None
data = None
while (cdic is None and data is None):
    config = get_config(u,pw)
    c_dic = utils.config_parser(config)

    data = utils.status(u,pw)


mine_scanner = scanner.scanner('BSOD', 'Alboucai')
mine_scanner.start()

while len(mine_scanner.mines) < 1:
    try:
        utils.move(u,pw,random.uniform(0,3.14),1)
    except (TimeoutError):
        pass

while True:
    blah = mine_scanner.mines
    min_dis = -1
    for value in list(blah):
        values = value.split(' ')
        x = values[0]
        y = values[1]
        x_,y_ = x,y
        
        dist = min_dist(float(data['position'][0]), float(data['position'][1]),float(x),float(y),float(c_dic['MAP_WIDTH']), float(c_dic['MAP_HEIGHT']))
        print((mine_scanner._mines[value][0]))
        if (min_dis < 0 or dist < min_dis and ((time.time()-mine_scanner._mines[value][0]) > 30)):
            min_dis = dist
            x_,y_ = x,y
    print('moving to:', x_, y_)
    try:
        exec_move(u,pw,float(x_),float(y_))
        scanner.mine_mutex.acquire()
        mine_scanner._mines[value] = (time.time(),u)
        scanner.mine_mutex.release()
    except(TimeoutError,TypeError):
        pass
    utils.move(u,pw,random.uniform(0,3.14),1)
    time.sleep(1)

mine_scanner.stop()
