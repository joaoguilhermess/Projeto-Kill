import os
import subprocess
import psutil
import time

class Kill:
	@classmethod
	def Init(self):
		self.name = "kill.txt"
		self.delay = 0.5

		self.max = 5

		start = time.time()

		while True:
			self.read()

			self.killServices()

			# self.killProcesses()

			if time.time() - start > self.max:
				break

			time.sleep(self.delay)

	@classmethod
	def read(self):
		if not os.path.exists(self.name):
			file = open(self.name, "w")
			file.close()

		file = open(self.name, "r")

		self.list = file.read().split("\n")

	@classmethod
	def killServices(self):
		for s in psutil.win_service_iter():
			try:
				if s.status() == "running":
					name = s.display_name()

					p = psutil.Process(s.pid())

					cmd = " ".join(p.cmdline())

					if cmd in self.list or name in self.list:
						subprocess.run(["net", "stop", str(s.name())], capture_output=True)
						print(s.name(), name, cmd)
			except Exception as e:
				# print("error", e)
				pass

	@classmethod
	def killProcesses(self):
		for p in psutil.process_iter():
			try:
				name = p.name()

				cmd = " ".join(p.cmdline())

				if cmd in self.list or name in self.list:
					subprocess.run(["taskkill", "/f", "/t", "/pid", str(p.pid)], capture_output=True)
					print(name, cmd)
			except Exception as e:
				# print("error", e)
				pass

Kill.Init()