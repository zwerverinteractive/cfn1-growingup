# -*- coding: utf-8 -*-
class Time():
	def __init__(self):
		self.days = ["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
		self.day = 1
		self.hour = 8
		self.minute = 0
		self.current_day = self.days[(self.day-1)%7]
		self.mili = 0
		self.tick = 1000
			
	def update(self):
		self.current_day = self.days[(self.day-1)%7]
		self.mili += 1
		if self.mili > self.tick:
			self.mili = 0		
			self.minute += 1
			if self.minute >= 60:
				self.minute = 0
				self.hour += 1
				if self.hour >= 24:
					self.hour = 0
					self.day += 1
					
		if engine.controls.buttons["watch"]:
			engine.screen.blit(engine.images.images["watch"][0], (0,0))
			engine.screen.blit(engine.text.m("Day " + str(self.day) + ": "), (18,66))
			engine.screen.blit(engine.text.m(self.current_day), (44,66))
			c = ""
			if self.hour < 10: c = "0" + str(self.hour)
			else: c = str(self.hour)
			c += ":"
			if self.minute < 10: c += "0"; c += str(self.minute)
			else: c += str(self.minute)
			engine.screen.blit(engine.text.m(c), (93,66))
			engine.screen.blit(engine.text.m("money: "  + "$" + str(engine.player.money)), (18,74))
			engine.screen.blit(engine.text.m("girls kissed: " + str(engine.player.kisses)), (18,82))
			stats = ["strength", "cool", "intelligence", "romance", "creativity"]
			for s, stat in enumerate(stats):
				engine.screen.fill((255,255,255), (62,26+(s*8), engine.player.stats[stat],5))
