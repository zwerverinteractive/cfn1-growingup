# -*- coding: utf-8 -*-
class Room():
	def __init__(self):
		self.current_room = "a1"
		self.rect = (0,0,1280,128)
		self.surf = pygame.Surface((1280,128))
		self.draw()
		
	def draw(self):
		self.surf.fill((0,0,0))
		self.surf.blit(engine.images.rooms[self.current_room][0], (0,0))
		
	def swap(self, d):
		if self.current_room == "a1":
			if d == "lu": self.current_room = "b1"
			if d == "ru": self.current_room = "b2"
			if d == "d": self.current_room = "a2"
		elif self.current_room == "a2":
			if d == "lu": self.current_room = "b2"
			if d == "ru": self.current_room = "b1"
			if d == "d": self.current_room = "a1"
		elif self.current_room == "b1":
			if d == "lu": self.current_room = "a2"
			if d == "ru": self.current_room = "a1"
			if d == "d": self.current_room = "b2"
		elif self.current_room == "b2":
			if d == "lu": self.current_room = "a1"
			if d == "ru": self.current_room = "a2"
			if d == "d": self.current_room = "b1"
		self.draw()	