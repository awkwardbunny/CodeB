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

def get_path(x0,y0,x,y,dx,dy,dimx,dimy):
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

def move_to(current,mine,config):
	accel = get_path(float(current['px']),float(current['py']),x,y,float(mine['px']),float(mine['py']),float(config['MAP_WIDTH']),float(config['MAP_HEIGHT']))
	move(user,password,accel[1],accel[0])
	

if __name__ == '__main__':
	exec_move('BSOD','Alboucai',6000,6000)
