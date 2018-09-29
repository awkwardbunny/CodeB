import socket
import sys
import websocket
import json

class BIClient:
    socket = None
    wsocket = None

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.wsocket = websocket.WebSocket()

    def get_ws_data(self):
        return json.loads(self.wsocket.recv())

    def connect(self, host, port):
        self.socket.connect((host, port))
        print('Client connected.')
        self.wsocket.connect("ws://codebb.cloudapp.net:17427")
        print('Websocket connected.')

    def send(self, command, wait = True):
        self.socket.sendall(bytes(command+"\n", "utf-8"))
        if wait:
            return self.socket.recv(1024).decode("utf-8").strip()

    def login(self, user, password):
        return self.send(user + " " + password, wait = False)

    def close(self):
        res = self.send("CLOSE_CONNECTION", wait = False)
        self.socket.close()
        print('Client closed.')
        return res
    
def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\nSUBSCRIBE\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            rline = sfile.readline()

