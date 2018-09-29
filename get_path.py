from utils import *
import math

def min_dist(x0,y0,x1,y1,dimx,dimy):
	points = [(x1+dimx*i,y1+dimy*j) for i in [-1,0,1] for j in [-1,0,1]]
	min_dist = -1
	for point in points:
		dist = math.sqrt((x0-point[0])**2+(y0-point[1])**2)
		if (min_dist < 0 or dist < min_dist):
			min_dist = dist
	return min_dist

def get_path(x0,y0,x,y,dx,dy,dimx,dimy,braking):
	# ideal_vec = np.array([x-x0,y-y0])
	velocity =	 0 #np.array([dx,dy])
	points = [(x+dimx*i,y+dimy*j) for i in [-1,0,1] for j in [-1,0,1]]
	min_dist = -1
	for point in points:
		dist = (x0-point[0])**2+(y0-point[1])**2
		if (min_dist < 0 or dist < min_dist):
			min_dist = dist
			min_point = point
	x,y = min_point
	# print(points,min_point)
	# pdb.set_trace()
	ideal_vec = np.array([x-x0,y-y0])

	fin_vel = (ideal_vec - velocity)
	# print(math.acos((x-x0)/(math.sqrt((x-x0)**2+(y-y0)**2))))
	if ((math.sqrt((x-x0)**2+(y-y0)**2)) == 0):
		return 0,0
	return min(1,math.sqrt((x-x0)**2+(y-y0)**2)),np.sign(x-x0)*math.acos((x-x0)/(math.sqrt((x-x0)**2+(y-y0)**2)))

def exec_move(user,password,x,y):
	while (np.linalg.norm(np.array(status(user,password)['velocity'])) > 1) :
		brake(user,password)
	config = None
	braking = False
	while (config is None):
		config = config_parser(get_config(user,password))

	while True:
		stats = status(user,password)
		if stats is None:
			pass
		else:
			pos = stats['position']
			vel = stats['velocity']
			
			accel = get_path(float(pos[0]),float(pos[1]),x,y,float(vel[0]),float(vel[1]),float(config['MAP_WIDTH']),float(config['MAP_HEIGHT']),braking)
			# print(stats['position'],accel[0])
			move(user,password,accel[1],accel[0])
			if (min_dist(x,y,float(pos[0]),float(pos[1]),float(config['MAP_WIDTH']),float(config['MAP_HEIGHT'])) < 250 and not braking):
				while (np.linalg.norm(np.array(status(user,password)['velocity'])) > .01):
					brake(user,password)
				braking	= True

			if (min_dist(x,y,float(pos[0]),float(pos[1]),float(config['MAP_WIDTH']),float(config['MAP_HEIGHT'])) < config['CAPTURERADIUS'] + 5):
				break
	

if __name__ == '__main__':
	exec_move('BSOD','Alboucai',6000,6000)
