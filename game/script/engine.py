# -*- coding: utf-8 -*-
import os
import sys
from script.controls import Controls
from script.sound import Sound
from script.colors import Colors
from script.images import Images
from script.render import Render



class Engine():
	def load(self):
		print("Loading engine")
		os.environ["SDL_VIDEO_CENTERED"] = "1"
		pygame.init()
		pygame.display.set_caption("v0.0.1")
		#pygame.mouse.set_visible(False)
		#pygame.event.set_grab(True)
		self.clock = pygame.time.Clock()
		self.wres = (800, 600); self.sres = (320, 200); flags = 0 #pygame.FULLSCREEN | pygame.DOUBLEBUF
		self.window = pygame.display.set_mode(self.wres, flags)
		self.screen = pygame.Surface(self.sres)
		self.controls = Controls()
		self.sound = Sound()
		self.colors = Colors()
		self.render = Render()
		self.images = Images()
		
		print("Loaded and ready to go!")
		self.running = True
		while self.running:
			self.update()
			if self.controls.buttons["quit"]:
				self.bye()

	def update(self):
		self.controls.update()
		self.render.update()
		
	def bye(self):
		print("bye!")
		pygame.quit()
		sys.exit()