# -*- coding: utf-8 -*-
class Room():
	def __init__(self):
		self.current_room = "a1"
		self.rect = (0,0,1280,128)
		self.surf = pygame.Surface((1280,128))
		self.surf.blit(engine.images.rooms[self.current_room][0], (0,0))