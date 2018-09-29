#!/usr/bin/env python3
import websocket
import json
ws = websocket.WebSocket()
ws.connect("ws://codebb.cloudapp.net:17427")
data = ws.recv()
print(data)
data = json.loads(data)

#print(data['mines'])
#for i in data['mines']:
#    print('Owner: '+i['owner'])
#    print('X: '+str(i['px']))
#    print('Y: '+str(i['py']))
#    print()
