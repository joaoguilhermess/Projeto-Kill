from time import sleep
from os import path
import psutil

class Kill:
	@classmethod
	def Init(self):
		self.name = "kill.txt"
		self.delay = 1

		while True:
			self.read()

			self.kill()

			sleep(self.delay)

	@classmethod
	def read(self):
		if not path.exists(self.name):
			file = open(self.name, "w")
			file.close()

		file = open(self.name, "r")

		self.list = file.read().split("\n")

	@classmethod
	def kill(self):
		l = psutil.pids()
		for pid in l:
			try:
				p = psutil.Process(pid)

				name = p.name()

				cmd = " ".join(p.cmdline())

				if cmd in self.list or name in self.list:
					p.kill()
					print(name, cmd)

			except Exception as e:
				pass

Kill.Init()