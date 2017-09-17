# -*- coding: utf-8 -*-
class Text():
	def __init__(self):
		self.font = pygame.font.Font("data/font/zwerveresque.ttf", 8)

	def m(self, text):
		t = self.font.render(text, 0, (255,255,255), (0, 0, 0))
		return t