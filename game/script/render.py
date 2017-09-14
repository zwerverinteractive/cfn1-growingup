# -*- coding: utf-8 -*-
class Render():
	def __init__(self):
		print("Loading render.")
		self.layers = []
		for i in range(5):
			self.layers.append([])
			
	def update(self):
		for layer in self.layers:
			for obj in layer:
				self.obj.update()
				