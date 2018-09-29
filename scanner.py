import threading
import utils
from clientpy3 import *
import time

class scanner(threading.Thread):
	def __init__(self,user,password):
		threading.Thread.__init__(self)
		self._mines = {}
		self._wormholes = {}
		self._user = user
		self._pass = password
		self._stop_event = threading.Event()
		self._config = utils.config_parser(utils.get_config(user,password))

	def run(self):
		while True:
			status = utils.status(self._user,self._pass)
			if status is not None:
				mines = status['mines']
				for mine in mines:
					# print(mine)
					if mine[1]+' '+mine[2] not in self.mines:
						# print(mine[1]+' '+mine[2])
						mine_mutex.acquire()
						self._mines[mine[1]+' '+mine[2]] = (time.time()-30,mine[0])
						mine_mutex.release()
				wormholes = status['wormholes']
				for wormhole in wormholes:
					if wormhole[0]+' '+wormhole[1] not in self.wormholes:
						wh_mutex.acquire()
						self._wormholes[wormhole[0]+' '+wormhole[1]] = wormhole
						wh_mutex.release()
				scan = utils.scan_parser(utils.scan(self._user,self._pass,status,self._config))
				if scan is not None:
					mines = scan['mines']
					for mine in mines:
						# print(mine)
						if mine[1]+' '+mine[2] not in self.mines:
							# print(mine[1]+' '+mine[2])
							mine_mutex.acquire()
							self._mines[mine[1]+' '+mine[2]] = (time.time()-30,mine[0])
							mine_mutex.release()
					wormholes = scan['wormholes']
					for wormhole in wormholes:
						if wormhole[0]+' '+wormhole[1] not in self.wormholes:
							wh_mutex.acquire()
							self._wormholes[wormhole[0]+' '+wormhole[1]] = wormhole
							wh_mutex.release()

			if self._stop_event.is_set():
				return
	
	def stop(self):
		self._stop_event.set()

	@property
	def mines(self):
		mine_mutex.acquire()
		mines = self._mines
		mine_mutex.release()
		return mines

	@property
	def wormholes(self):
		wh_mutex.acquire()
		wormholes = self._wormholes
		wh_mutex.release()
		return wormholes

mine_mutex = threading.Lock()
wh_mutex = threading.Lock()
# mine_scanner = scanner('BSOD','Alboucai')
# mine_scanner.start()

# import pdb
# pdb.set_trace()

# mine_scanner.stop()
