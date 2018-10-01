#!/usr/bin/env python3
from clientpy3 import *
from utils import *
import datetime
import time
import sys,signal
import websocket
import json
import readchar
import math

class Bot:
    running = True

    def sigint_handler(self, signal, frame):
        print('\nSIGINT Received!')
        self.running = False

    def main(self, user, password, host, port):

        # Start a connection to game server
        c = BIClient()
        c.connect(host,port)
        c.login(user,password)

        # Get config
        config = config_parser(c.send("CONFIGURATIONS"))
        print("Config:\n",config)

        # Set up DBs
        db = {}

        # Begin time
        time_beg = datetime.datetime.now()

        # Loop
        signal.signal(signal.SIGINT, self.sigint_handler)
        while self.running:

            # Get board data from websocket
            db = c.get_ws_data()

            # Print all mines
            #print('----------------------')
            #for mine in db['mines']:
            #    print(mine)

            # Get current player position
            p_pos = {}
            for p in db['players']:
                if p['name'] == user:
                    p_pos = (p['px'], p['py'])
                    break

            closest_mine = get_closest_mine(db['mines'], p_pos, (config['MAPWIDTH'],config['MAPHEIGHT']), user)
            #print(closest_mine)
            #move_to(c, p_pos, (closest_mine['px'],closest_mine['py']), (config['MAPWIDTH'],config['MAPHEIGHT']))

            ch = readchar.readchar()
            print(ch)
            if ch == 'k':
                c.send('ACCELERATE ' + str(3*math.pi/2) + ' 1')
            if ch == 'h':
                c.send('ACCELERATE ' + str(math.pi) + ' 1')
            if ch == 'l':
                c.send('ACCELERATE 0 1')
            if ch == ' ':
                c.send('ACCELERATE ' + str(math.pi/2) + ' 0')
            if ch == 'j':
                c.send('ACCELERATE ' + str(math.pi/2) + ' 1')
            if ch == 'x':
                self.running = False

        # Close
        print('Terminating')
        c.close()

if __name__ == '__main__':
    b = Bot()
    print('Staring bot...')
    b.main(user='BSOD', password='Alboucai', host='codebb.cloudapp.net', port=17429)
