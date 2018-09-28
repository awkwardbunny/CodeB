from clientpy3 import *
import utils
import time

u = 'BSOD'
p = 'Alboucai'

while True:
    status = get_status(u,p)
    data = utils.status_parser(status[0])
    print(data)
    time.sleep(0.5)
