from clientpy3 import *
import time

def status_parser(status):
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

def status(user,password):
	try:
		status = get_status(u,p)
		return status_parser(status[0])
	except (IndexError, TimeoutError):
		return

if __name__ == '__main__':

	u = 'BSOD'
	p = 'Alboucai'
	while True:
		print(status(u,p))
		time.sleep(2)
