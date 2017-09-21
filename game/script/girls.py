# -*- coding: utf-8 -*-
from random import choice
girl = {}
girl["Jenny"] = {
	"home" : (8, "b1",	98, "my home"),
	"stats" : {
		"strength" : 10,
		"cool" : 6,
		"intelligence" : 4,
		"romance" : 3,
		"creativity" : 4,		
		},
	"schedule_everyday" : (
		#time, 	room, 	x
		(7,		"b2", 	800, "school"),
		(8,   "invisible", 780, "school"),
		(15,	"b2",	432, "school"),
		(16, 	"a1", 	433, "the gym"),
		(17, "invisible", 450, "the gym"),
		(18, 	"a1", 	433, "the gym"),
		(19,	"b1",	98, "my home"),
		(20,	"invisible", 90, "my home"),
		),
	"schedule_saturday" : (
		#time, 	room, 	x
		(11,	"b1", 	512, "the pool"),
		(15,	"a1",	433, "the toystore"),
		(17,	"a1",	936, "skatepark"),
		(19,	"b1",	98, "my home"),
		(20,	"invisible", 90, "my home"),
		),
	"schedule_sunday" : (
		#time, 	room, 	x
		(12,	"a1",	900, "the basketball court"),
		(16,	"a2",	300, "the playground"),
		(19,	"b1",	98, "my home"),
		(20,	"invisible", 90, "my home"),
		),
	}

girl["Zoe"] = {
	"home" : (8,	"b1",	893, "my home"),
	"stats" : {
		"strength" : 6,
		"cool" : 10,
		"intelligence" : 4,
		"romance" : 3,
		"creativity" : 4,		
		},
	"schedule_everyday" : (
		#time, 	room, 	x
		(7,		"b2", 	810, "school"),
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
		(8,	"b2", 860, "church"),
		(9, 	"invisible", 905, "church"),
		(11,  "b2", 860, "church"),
		(12,	"a1",	900, "the skatepark"),
		(16,	"a1",	433, "the toystore"),
		(19,	"b1",	200, "my home"),
		(20,	"invisible", 888, "my home"),
		),
	}

girl["Lisa"] = {
	"home" : (8,	"b1",	800, "my home"),
	"stats" : {
		"strength" : 6,
		"cool" : 10,
		"intelligence" : 4,
		"romance" : 3,
		"creativity" : 4,		
		},
	"schedule_everyday" : (
		#time, 	room, 	x
		(7,		"b2", 	810, "school"),
		(8,   "invisible", 780, "school"),
		(15,	"b2",	432, "school"),
		(16, 	"a1", 	1064, "the library"),
		(17, 	"invisible", 	1075, "the library"),
		(18, 	"a1", 	1064, "the library"),
		(19,	"b1",	800, "my home"),
		(20,	"invisible", 810, "my home"),
		),
	"schedule_saturday" : (
		#time, 	room, 	x
		(11,	"b1", 	512, "playground"),
		(15,	"a1",	135, "the office supply store"),
		(16,	"invisible",	150, "the office supply store"),
		(17,	"a1",	135, "the office supply store"),
		(18,	"a1",	936, "playground"),
		(19,	"b1",	800, "my home"),
		(20,	"invisible", 810, "my home"),
		),
	"schedule_sunday" : (
		#time, 	room, 	x
		(12,	"a1",	900, "playground"),
		(16,	"a1",	1200, " find a place to be alone"),
		(19,	"b1",	800, "my home"),
		(20,	"invisible", 810, "my home"),
		),
	}
	
	
girl["Miranda"] = {
	"home" : (8,	"b1",	240, "my home"),
	"stats" : {
		"strength" : 3,
		"cool" : 3,
		"intelligence" : 3,
		"romance" : 10,
		"creativity" : 6,		
		},
	"schedule_everyday" : (
		#time, 	room, 	x
		(7,		"b2", 	800, "school"),
		(8,   "invisible", 780, "school"),
		(15,	"b2",	432, "school"),
		(16, 	"a1", 	300, "the clothing store"),
		(17, 	"invisible", 	290, "the clothing store"),
		(18, 	"a1", 	300, "the clothing store"),
		(19,	"b1",	240, "my home"),
		(20,	"invisible", 230, "my home"),
		),
	"schedule_saturday" : (
		#time, 	room, 	x
		(11,	"b1", 	512, "the playground"),
		(13,	"a2",	1090, "the lake"),
		(19,	"b1",	240, "my home"),
		(20,	"invisible", 230, "my home"),
		),
	"schedule_sunday" : (
		#time, 	room, 	x
		(8,	"b2", 880, "church"),
		(9, 	"invisible", 900, "church"),
		(11,  "b2", 880, "church"),
		(12,	"a1",	900, "the lake"),
		(19,	"b1",	240, "my home"),
		(20,	"invisible", 230, "my home"),
		),
	}

girl["Tanya"] = {
	"home" : (8,	"a2",	103, "my home"),
	"stats" : {
		"strength" : 3,
		"cool" : 3,
		"intelligence" : 3,
		"romance" : 6,
		"creativity" : 10,		
		},
	"schedule_everyday" : (
		#time, 	room, 	x
		(7,		"b2", 	800, "school"),
		(8,   "invisible", 780, "school"),
		(15,	"b2",	432, "school"),
		(16, 	"a2", 	920, "the park"),
		(17, 	"invisible", 	930, "the park"),
		(18, 	"a2", 	920, "the park"),
		(19,	"a2",	100, "my home"),
		(20,	"invisible", 110, "my home"),
		),
	"schedule_saturday" : (
		#time, 	room, 	x
		(11,	"b1", 	512, "the playground"),
		(13, 	"a1", 	510, "the art store"),
		(17, 	"invisible", 	520, "the art store"),
		(18, 	"a1", 	510, "the art store"),
		(19,	"b1",	100, "my home"),
		(20,	"invisible", 110, "my home"),
		),
	"schedule_sunday" : (
		#time, 	room, 	x
		(12, 	"a2", 	920, "the park"),
		(13, 	"invisible", 	930, "the park"),
		(15, 	"a2", 	920, "the park"),
		(19,	"b1",	100, "my home"),
		(20,	"invisible", 110, "my home"),
		),
	}

class Girl():
	def __init__(self,name, p):
		self.name = name
		self.current_room = "b1"
		self.destination = None
		self.spoken = False
		self.location = "my home"
		self.sched = 0
		self.properties = p
		x = self.properties["home"][2]
		self.rect = [x,40,16,32]
		self.real_rect = [x,40,16,32]
		self.surf = pygame.Surface((16,32))
		self.surf.set_colorkey((0,255,0))
		self.surf.fill((0,255,0))
		self.surf.blit(engine.images.images[self.name][0], (0,0))
		self.speed = 1
		self.love = 0
		self.know = 0
		self.run = False

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
		if self.spoken:
			engine.text.mw("Easy now. You already talked to this girl today. You don't want to seem desperate!")
		else:
			engine.dialog.talk(self, l, d)
			self.spoken = True			
				
				
		
class Girls():
	def __init__(self):
		self.girls = {
			"Jenny" : Girl("Jenny", girl["Jenny"]),
			"Zoe" : Girl("Zoe", girl["Zoe"]),
			"Lisa" : Girl("Lisa", girl["Lisa"]),
			"Miranda" : Girl("Miranda", girl["Miranda"]),
			"Tanya" : Girl("Tanya", girl["Tanya"]),
			}
			
	def update(self):
		for girl in self.girls:
			self.girls[girl].update()
			if engine.room.current_room == self.girls[girl].current_room:
				engine.gscreen.blit(self.girls[girl].surf, (self.girls[girl].rect[0],self.girls[girl].rect[1]))
				
			