from clientpy3 import *
import utils
import datetime
import scanner
import time
from get_path import exec_move, min_dist

u = 'BSOD'
pw = 'Alboucai'

print('starting')

config = get_config(u,pw)
c_dic = utils.config_parser(config)

data = utils.status(u,pw)

mine_scanner = scanner.scanner('BSOD', 'Alboucai')
mine_scanner.start()

while len(mine_scanner.mines) < 1:
    try:
        utils.move(u,pw,-1,1)
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
        if (min_dis < 0 or dist < min_dis and time.time())-mine_scanner._mines[value][0] > 30:
            min_dis = dist
            x_,y_ = x,y
    print('moving to:', x_, y_)
    try:
        exec_move(u,pw,float(x_),float(y_))
        mine_mutex.acquire()
        mine_scanner._mines[value] = (time.time(),u)
        mine_mutex.release()
    except(TimeoutError):
        pass
    utils.move(u,pw,1,-1)

mine_scanner.stop()
