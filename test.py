from clientpy3 import *
import time
run('BSOD', 'Alboucai', 'STATUS')

while True:
    run('BSOD', 'Alboucai', 'ACCELERATE 1.0 0.5')
    time.sleep(3)
    run('BSOD', 'Alboucai', 'ACCELERATE 3.14 1')
    time.sleep(5)

