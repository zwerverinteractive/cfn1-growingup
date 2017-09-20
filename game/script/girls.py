# -*- coding: utf-8 -*-
from random import choice
girl = {}
girl["Zoe"] = {
	"stats" : {
		"strength" : 6,
		"cool" : 10,
		"intelligence" : 4,
		"romance" : 3,
		"creativity" : 4,		
		},
	"schedule_everyday" : (
		#time, 	room, 	x
		(7,		"b2", 	800, "school"),
		(8,   "invisible", 780, "school"),
		(15,	"b2",	432, "school"),
		(16, 	"a1", 	433, "the toystore"),
		(18,	"a1",	926, "skatepark"),
		(19,	"b1",	893, "my home"),
		(20,	"invisible", 888, "my home"),
		),
	"schedule_saturday" : (
		#time, 	room, 	x
		(11,	"b1", 	512, "playground"),
		(15,	"a1",	433, "the toystore"),
		(17,	"a1",	936, "skatepark"),
		(19,	"b1",	893, "my home"),
		(20,	"invisible", 888, "my home"),
		),
	"schedule_sunday" : (
		#time, 	room, 	x
		(8,	"b2", 880, "church"),
		(9, 	"invisible", 900, "church"),
		(11,  "b2", 880, "church"),
		(12,	"a1",	900, "the skatepark"),
		(16,	"a1",	433, "the toystore"),
		(19,	"b1",	200, "my home"),
		(20,	"invisible", 888, "my home"),
		),
	"dialog_unknown" : (
		"hello. my name is zoe.",
		"oh... euh... hello...",
		"what do you want?",
		"can I help you?",
		),
	}

class Girl():
	def __init__(self,name, p):
		self.name = name
		self.current_room = "b1"
		self.destination = None
		self.location = "my home"
		self.sched = 0
		self.rect = [892,40,16,32]
		self.real_rect = [892,40,16,32]
		self.surf = pygame.Surface((16,32))
		self.surf.set_colorkey((0,255,0))
		self.surf.fill((0,255,0))
		self.surf.blit(engine.images.images[self.name][0], (0,0))
		self.speed = 1
		self.love = 0
		self.know = 0
		self.properties = p

		#ANIMATION PROPERTIES
		self.current_animation = "w_left"
		self.current_frame = 0
		self.frame_clock = 0
		self.frame_speed = 64
		self.animations = {
			"w_right" : [0,1,2,3,4],
			"w_left" : [4,5,6,7,8],
			}
		
	def update(self):
		d = engine.time.current_day
		if d == "saturday": sched = "schedule_saturday"
		elif d == "sunday": sched = "schedule_sunday"
		else: sched = "schedule_everyday"
		
		os = self.sched
		a = 0
		for s in self.properties[sched]:
			if engine.time.hour > s[0]:
				a += 1
				
		self.sched = a
		if self.sched > os:
			try:
				self.current_room = self.properties[sched][self.sched+1][1]
				self.rect[0] = self.real_rect[0] = self.properties[sched][self.sched+1][2]
			except:
				pass
		
		if engine.time.hour < 20:
			if engine.time.hour ==  self.properties[sched][self.sched][0]:
				self.destination = self.properties[sched][self.sched]
				if self.current_room == "invisible":
					self.current_room = self.destination[1]
				self.sched += 1
		
				
		if self.destination != None:
			self.frame_clock += 1
			if self.frame_clock > self.frame_speed:
				if self.destination[1] == "invisible":
					if self.real_rect[0] < self.destination[2]-4: self.move("right")
					elif self.real_rect[0] > self.destination[2]+4: self.move("left")
					else: self.current_room = "invisible"; self.location = self.destination; self.destination = None
				elif self.current_room != self.destination[1]:
					if self.real_rect[0] < 585: self.move("right")
					elif self.real_rect[0] > 700: self.move("left")
					else: self.current_room = self.destination[1]
				else:
					if self.real_rect[0] < self.destination[2]-4: self.move("right")
					elif self.real_rect[0] > self.destination[2]+4: self.move("left")
					else:			
						self.current_frame = 0
						self.location = self.destination
						self.destination = None
						self.draw()
				self.frame_clock = 0
				
			self.rect[0] = round(self.real_rect[0])
		else:
			if engine.player.rect[0] < self.rect[0]: self.current_animation = "w_left"; self.draw()
			elif engine.player.rect[0] > self.rect[0]: self.current_animation = "w_right"; self.draw()
					
	def move(self, d):
		self.current_frame += 1
		if self.current_frame >= len(self.animations[self.current_animation])-1: self.current_frame = 0
		if d == "left": self.real_rect[0] -= self.speed; self.current_animation = "w_left"
		else: self.real_rect[0] += self.speed; self.current_animation = "w_right"
		self.draw()
	
	def draw(self):
		self.surf.fill((0,255,0))
		cf = self.animations[self.current_animation][self.current_frame]
		self.surf.blit(engine.images.images[self.name][cf], (0,0))			
		
	def talk(self):
		if self.location != None: l = self.location[3]
		else: l = None
		if self.destination != None: d = self.destination[3]
		else: d = None
		
		engine.dialog.talk(self, l, d)
				
				
				
		
class Girls():
	def __init__(self):
		self.girls = {
			"Zoe" : Girl("Zoe", girl["Zoe"]),
			}
			
	def update(self):
		for girl in self.girls:
			self.girls[girl].update()
			if engine.room.current_room == self.girls[girl].current_room:
				engine.gscreen.blit(self.girls[girl].surf, (self.girls[girl].rect[0],self.girls[girl].rect[1]))
				
			