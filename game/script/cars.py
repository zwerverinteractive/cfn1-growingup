# -*- coding: utf-8 -*-
from random import choice

class Car():
	def __init__(self):
		self.surf = pygame.Surface((80,32))
		rc = choice((0,1,2))
		self.surf.fill((0,255,0))
		self.surf.set_colorkey((0,255,0))
		self.surf.blit(engine.images.images["cars"][rc], (0,0))
		self.speed = 0.2
		self.alive = True
		self.d = choice((self.speed,-self.speed))
		if self.d < 0:
			self.surf = pygame.transform.flip(self.surf, True, False)
			self.v2 = [1280,97-32]
		else:
			self.v2 = [-80,120-32]
		
	def update(self):
		self.v2[0] += self.d
		if self.v2[0] > 1280 or self.v2[0] < -80:
			self.alive = False