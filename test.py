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

status = get_status(u,pw)
data = utils.status_parser(status[0])

#initialize the dictionaries
mine_db = {}
worm_db = {}
mine_list = []
time1 = datetime.datetime.now()

mine_scanner = scanner.scanner('BSOD', 'Alboucai')
mine_scanner.start()

while len(mine_scanner.mines) < 3:
    utils.move(u,pw,-1,1)

for value in mine_scanner.mines:
    value = value.split(' ')
    x = value[0]
    y = value[1]
   
    min_dist(float(data['position'][0]), float(data['position'][1]),float(x),float(y),float(c_dic['MAP_WIDTH']), float(c_dic['MAP_HEIGHT']))
    print('moving to:', x, y)
    exec_move(u,pw,float(x),float(y))

mine_scanner.stop()
