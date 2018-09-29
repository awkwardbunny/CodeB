import numpy as np
from utils import *

def get_path(x0,y0,x,y,dx,dy):
	ideal_vec = np.array([x-x0,y-y0])
	velocity = 0#np.array([dx,dy])
	
	fin_vel = (ideal_vec - velocity)

	return (min(1,np.sqrt((x0-x)**2+(y-y0)**2)/1000),np.sign(fin_vel[0])*np.arccos(fin_vel[0]/(np.linalg.norm(fin_vel)+.00001)),fin_vel)

def exec_move(user,password,x,y):
	while (np.linalg.norm(np.array(status(user,password)['velocity'])) > 10):
		brake(user,password)
	while True:
		stats = status(user,password)
		pos = stats['position']
		vel = stats['velocity']
		config = get_config(user,password)
		accel = get_path(float(pos[0]),float(pos[1]),x,y,float(vel[0]),float(vel[1]))
		print(stats['position'],stats['velocity'],accel)
		new_vel = np.array(vel).astype(np.float32) + accel[2]
		move(user,password,accel[1],accel[0])
		if (np.linalg.norm(np.array((x,y))-np.array(pos).astype(np.float32)) < 50):
			break
	





if __name__ == '__main__':
	exec_move('BSOD','Alboucai',1000,4444)
