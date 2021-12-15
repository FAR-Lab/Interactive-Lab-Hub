from picamera import PiCamera
import time


class webCam(object):
	def __init__(self, flip = False):
		self.camera = PiCamera()
		self.camera.resolution = (1280, 720)
		self.camera.vflip = flip
		self.camera.contrast = 10
		# self.fname = name

	def record(self, name):
		file_name = "./"+str(name)+"fall.mp4"
		print("Start recording...")
		self.camera.start_recording(file_name)
		self.camera.wait_recording(10)
		self.camera.stop_recording()
		print("Done.")


