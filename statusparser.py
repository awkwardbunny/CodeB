from clientpy3 import *

def status_parser(status):
	tokens = status.split(' ')
	# return tokens
	data = {}
	data['position'] = (tokens[1],tokens[2])
	data['velocity'] = (tokens[3],tokens[4])
	num_mines = int(tokens[7])
	data['num_mines'] = num_mines
	data['mines'] = [(tokens[7+3*i+1],tokens[7+3*i+2],token[7+3*i+3]) for i in range(num_mines)]


	return data

if __name__ == '__main__':

	u = 'BSOD'
	p = 'Alboucai'
	while True:
		try:
			status = get_status(u,p)
			print(status_parser(status[0]))
		except (IndexError):
			pass
