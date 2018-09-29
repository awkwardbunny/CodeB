from clientpy3 import *
import time
import random
import math

def status_parser(status):
    tokens = status.split(' ')
    if not tokens[0] == 'STATUS_OUT':
        raise Exception('Invalid Status Data!')

    data = {}
    data['position'] = (tokens[1],tokens[2])
    data['velocity'] = (tokens[3],tokens[4])
    num_mines = int(tokens[7])
    data['num_mines'] = num_mines
    data['mines'] = [tokens[7+3*i+1:7+3*i+4] for i in range(num_mines)]
    pinfo_start = 7+3*num_mines+2
    num_players = int(tokens[pinfo_start])
    data['num_players'] = num_players
    data['players'] = [tokens[pinfo_start+4*i+1:pinfo_start+4*i+5] for i in range(num_players)]
    binfo_start = pinfo_start+4*num_players+2
    num_bombs = int(tokens[binfo_start])
    data['num_bombs'] = num_bombs
    data['bombs'] = [tokens[binfo_start+3*i+1:binfo_start+3*i+4] for i in range(num_bombs)]
    winfo_start = binfo_start+3*num_bombs+2
    num_wormholes = int(tokens[winfo_start])
    data['num_wormholes'] = num_wormholes
    data['wormholes'] = [tokens[winfo_start+5*i+1:winfo_start+5*i+6] for i in range(num_wormholes)]
    return data

def config_parser(config):
    tokens = config.split(' ')
    if not tokens[0] == 'CONFIGURATIONS_OUT':
        raise Exception('Invalid Config Data!')

    data = {}
    for i in range(0,12):
        data[tokens[i*2+1]] = float(tokens[i*2+2])
    return data

def move(client, angle, velocity):
    angle = str(angle)
    velocity = str(velocity)
    client.send('ACCELERATE '+angle+' '+velocity)

def brake(client):
    client.send('BRAKE')
