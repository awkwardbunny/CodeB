#!/usr/bin/env python3
from clientpy3 import *
from utils import *
import datetime
import time
import sys,signal
import websocket
import json

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
        blah = -1
        while self.running:

            # Get board data from websocket
            db = c.get_ws_data()

            print('----------------------')
            for mine in db['mines']:
                print(mine)
                # EXEC MOVE

        # Close
        print('Terminating')
        c.close()

if __name__ == '__main__':
    b = Bot()
    print('Staring bot...')
    b.main(user='BSOD', password='Alboucai', host='codebb.cloudapp.net', port=17429)
