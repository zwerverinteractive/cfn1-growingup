# -*- coding: utf-8 -*-
class Time():
	
	def __init__(self):
		self.days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
		self.day = 1
		self.hour = 7
		self.minute = 0
		
		self.mili = 0
		self.tick = 1000
			
	def update(self):
		self.mili += 1
		if self.mili > self.tick:
			self.mili = 0		
			self.minute += 1
			if self.minute > 60:
				self.minute = 0
				self.hour += 1
				if self.hour >= 24:
					self.hour = 0
					self.day += 1
					
		if engine.controls.buttons["watch"]:
			engine.screen.blit(engine.images.images["watch"][0], (0,0))
			engine.screen.blit(engine.text.m("Day " + str(self.day) + ":"), (18,80))
			engine.screen.blit(engine.text.m(self.days[(self.day-1)%7]), (40,80))
			c = ""
			if self.hour < 10: c = "0" + str(self.hour)
			else: c = str(self.hour)
			c += ":"
			if self.minute < 10: c += "0"; c += str(self.minute)
			else: c += str(self.minute)
			engine.screen.blit(engine.text.m(c), (93,80))