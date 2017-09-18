# -*- coding: utf-8 -*-
from script.hotspots import spots

class Room():
	def __init__(self):
		self.hotspots = spots
		self.overworld = False
		self.current_room = "home-up"
		self.rect = (0,0,1280,128)
		self.surf = pygame.Surface((1280,128))
		self.draw()
		
	def draw(self):
		self.surf.fill((0,0,0))
		self.surf.blit(engine.images.rooms[self.current_room][0], (0,0))
		
	def swap(self, r):
		del engine.cars[:]
		if r == "home-down":
			engine.player.dad = True
		
		self.current_room = r
		self.draw()	