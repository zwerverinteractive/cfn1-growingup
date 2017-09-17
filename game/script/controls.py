# -*- coding: utf-8 -*-
class Controls():
	def __init__(self):
		print("Loading controls")
		self.cfg = {
			"up" : 		pygame.K_UP,
			"down" :	pygame.K_DOWN,
			"left" : 		pygame.K_LEFT,
			"right" : 	pygame.K_RIGHT,
			"A": 		pygame.K_z,
			"B": 		pygame.K_x,
			"start": 		pygame.K_RETURN,
			"select": 	pygame.K_SPACE,
			"quit":		pygame.K_ESCAPE,
			"watch":	pygame.K_TAB,
			}
			
		self.buttons = {}
		for b in self.cfg:
			self.buttons[b] = False

	def update(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				self.buttons["quit"] = True
			if e.type == pygame.KEYDOWN:
				for b in self.buttons:
					if e.key == self.cfg[b]:
						self.buttons[b] = True
			if e.type == pygame.KEYUP:
				for b in self.buttons:
					if e.key == self.cfg[b]:
						self.buttons[b] = False		