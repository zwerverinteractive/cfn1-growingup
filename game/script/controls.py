# -*- coding: utf-8 -*-
class Controls():
	def __init__(self):
		print("Loading controls")
		self.cfg = {
			"up" : 		pygame.K_UP,
			"down" :	pygame.K_DOWN,
			"left" : 		pygame.K_LEFT,
			"right" : 	pygame.K_RIGHT,
			"skate": 	pygame.K_LSHIFT,
			"trick": 		pygame.K_SPACE,
			"watch":	pygame.K_TAB,
			"start": 		pygame.K_RETURN,
			"quit":		pygame.K_ESCAPE,
			"fullscreen": pygame.K_f,
			}
			
		self.buttons = {}
		for b in self.cfg:
			self.buttons[b] = False

	def update(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				engine.close()
			if e.type == pygame.KEYDOWN:
				for b in self.buttons:
					if e.key == self.cfg[b]:
						self.buttons[b] = True
			if e.type == pygame.KEYUP:
				for b in self.buttons:
					if e.key == self.cfg[b]:
						self.buttons[b] = False