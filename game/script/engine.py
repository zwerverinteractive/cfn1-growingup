# -*- coding: utf-8 -*-
import os
import sys
from random import randint
from script.controls import Controls
from script.sound import Sound
from script.images import Images
from script.room import Room
from script.cars import Car
from script.player import Player
from script.text import Text
from script.time import Time

class Engine():
	def load(self):
		print("Loading engine")
		os.environ["SDL_VIDEO_CENTERED"] = "1"
		pygame.init()
		pygame.display.set_caption("v0.0.1")
		#pygame.mouse.set_visible(False)
		#pygame.event.set_grab(True)
		self.clock = pygame.time.Clock()
		self.wres = (800, 600); self.sres = (128, 128); flags = 0#pygame.FULLSCREEN | pygame.DOUBLEBUF
		self.window = pygame.display.set_mode(self.wres, flags)
		self.screen = pygame.Surface(self.sres)
		self.gscreen = pygame.Surface((1280,128))
		self.objects = []
		self.time = Time()
		self.text = Text()
		self.controls = Controls()
		self.sound = Sound()
		self.images = Images()
		self.room = Room()
		self.player = Player()
		self.cars = []
		
		print("Loaded and ready to go!")
		self.running = True
		while self.running:
			self.clock.tick()
			self.controls.update()
			self.screen.fill((0,0,0)); self.gscreen.fill((0,0,0))
			self.gscreen.blit(self.room.surf, (0,0))

			for obj in self.objects:
				obj.update()
				self.gscreen.blit(obj.surf, obj.rect)

			#spawn cars
			c = engine.room.current_room
			if c == "a1" or c == "a2" or c == "b1" or c == "b2":
				if randint(0,5000) == 0:
					self.cars.append(Car())
			for c,car in enumerate(self.cars):
				car.update()
				if car.alive == False:
					del self.cars[c]
				else:
					self.gscreen.blit(car.surf, car.v2)
					
			if self.player.rect[0] > 64-8:
				self.screen.blit(self.gscreen, (-self.player.rect[0]+64-8,0))
			else:
				self.screen.blit(self.gscreen, (0,0))
			self.time.update()
			pygame.transform.scale(self.screen, self.wres, self.window)
			pygame.display.flip()
			if self.controls.buttons["quit"]:
				self.bye()
		
	def bye(self):
		print("bye!")
		pygame.quit()
		sys.exit()