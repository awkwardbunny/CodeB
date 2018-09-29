from clientpy3 import *
import time
import random
import math

def status_parser(status):
	try:
		tokens = status[0]
	except (IndexError):
		return
	tokens = status.split(' ')
	# print(tokens)
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
    try:
        tokens = config[0]
    except (IndexError):
        return
    #print (type(tokens))
    tokens = tokens.split(' ')
    data = {}
    data['MAP_WIDTH'] = float(tokens[2])
    data['MAP_HEIGHT'] = float(tokens[4])
    data['CAPTURERADIUS'] = float(tokens[6])
    data['VISIONRADIUS'] = float(tokens[8])
    data['FRICTION'] = float(tokens[10])
    data['BRAKEFRICTION'] = float(tokens[12])
    data['BOMBPLACERADIUS'] = float(tokens[14])
    data['BOMBEFFECTRADIUS'] = float(tokens[16])
    data['BOMBDELAY'] = float(tokens[18])
    data['BOMBPOWER'] = float(tokens[20])
    data['SCANRADIUS'] = float(tokens[22])
    data['SCANDELAY'] = float(tokens[24])
    return data

def scan_parser(scan_data):
	if (scan_data == ['ERROR Scanning too soon']):
		return
	try:
		tokens = scan_data[0]
	except (IndexError):
		return 
	tokens = tokens.split(' ')
	data = {}
	# print(tokens)
	num_mines = int(tokens[3])
	data['mines'] = [tokens[3+3*i+1:3+3*i+4] for i in range(num_mines)]
	pinfo_start = 3+3*num_mines+2
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

def status(user,password):
    try:
            status = get_status(user,password)
            return status_parser(status[0])
    except (IndexError, TimeoutError):
            return

def move(user, password, angle, velocity):
    angle = str(angle)
    velocity = str(velocity)
    run(user,password,'ACCELERATE '+angle+' '+velocity)
    return 

def brake(user, password):
    run(user, password,'BRAKE')
    return 

def scan(user, password, data, dic):
<<<<<<< HEAD
	user_x = data['position'][0] 
	user_y = data['position'][1] 
	randx = random.randint(0,dic['MAP_WIDTH']) 
	randy = random.randint(0,dic['MAP_WIDTH']) 
	
	scan_x = str(math.floor((randx) % dic['MAP_WIDTH']))
	scan_y = str(math.floor((randy) % dic['MAP_WIDTH']))
	#print('scanning: ', scan_x, scan_y)
	return get_scan(user, password, scan_x, scan_y)

if __name__ == '__main__':
	u = 'BSOD'
	p = 'Alboucai'
	while True:
		move(u,p,3.14/2,0.25+0.25)
		print(status(u,p))
		time.sleep(2)
=======
    user_x = data['position'][0] 
    user_y = data['position'][1] 
    #randx = random.randint(0,dic['MAP_WIDTH']) 
    #randy = random.randint(0,dic['MAP_WIDTH']) 
    status = get_status('BSOD', 'Alboucai')
    data2 = utils.status_parser(status[0])
    current_x = data2['position'][0]
    current_y = data2['position'][1]
    xvec = float(current_x) - float(user_x)
    print(xvec)
    yvec = float(current_y) - float(user_y)
    print(yvec)
    scan_x = str(math.floor((float(user_x) + 10*xvec) % dic['MAP_WIDTH']))
    scan_y = str(math.floor((float(user_y) + 10*yvec) % dic['MAP_WIDTH']))
    #print('scanning: ', scan_x, scan_y)
    return get_scan(user, password, scan_x, scan_y)

if __name__ == '__main__':
    u = 'BSOD'
    p = 'Alboucai'
    while True:
        move(u,p,3.14/2,0.25+0.25)
        print(status(u,p))
        time.sleep(2)
>>>>>>> b9345a37a0dd213b93d50884f5a3b886ca9496a5
