from clientpy3 import *
import time
import random
import math
import numpy as np

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

def get_closest_mine(mines, p_pos, dim, user):

    closest = None
    closest_d = 10000000000
    for mine in mines:
        if mine['owner'] == user:
            continue
        d = calc_d(p_pos,(mine['px'],mine['py']),dim)
        if d < closest_d:
            closest_d = d
            closest = mine
    return closest

def calc_d(p,m,d):
    min_dist = 100000000
    points = [(p[0]+d[0]*i,p[1]+d[1]*j) for i in [-1,0,1] for j in [-1,0,1]]
    for point in points:
        dist = (m[0]-point[0])**2+(m[1]-point[1])**2
        if dist < min_dist:
            min_dist = dist
    return min_dist

def move_to(c,p,m,d):
    points = [(m[0]+d[0]*i,m[1]+d[1]*j) for i in [-1,0,1] for j in [-1,0,1]]
    min_dist = -1
    for point in points:
        dist = (p[0]-point[0])**2+(p[1]-point[1])**2
        if (min_dist < 0 or dist < min_dist):
            min_dist = dist
            min_point = point
    x,y = min_point

    if ((math.sqrt((x-p[0])**2+(y-p[1])**2)) <= 300):
       c.send('BRAKE') 

    c.send('ACCELERATE ' + str(np.sign(x-p[0])*math.acos((x-p[0])/(math.sqrt((x-p[0])**2+(y-p[1])**2)))) + " " + str(min(0.5,math.sqrt((x-p[0])**2+(y-p[1])**2))))
