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
	"schedule_days" : (
		#time, 	room, 	x
		(8,		"b2", 	800, "school"),
		(15,	"a1",	432, "toystore"),
		(17,	"a1",	936, "skatepark"),
		(19,	"b1",	893, "home"),
		),
	"schedule_weekends" : (
		#time, 	room, 	x
		(11,	"b1", 	512, "gym"),
		(15,	"b1",	100, "toystore"),
		(17,	"a1",	100, "skatepark"),
		(19,	"b1",	200, "home"),
		),
	"dialog_unknown" : (
		"hello. my name is zoe.",
		"oh... euh... hello...",
		"what do you want from me?",
		),
	"dialog_school" : (
		"school is stupid.",
		"can't wait for this to be over.",
		),
	"dialog_gym" : (
		"oh you go to the gym too?",
		),
	"dialog_toystore": (
		"I like this place, they sell cool stuff.",
		"I hear they'll sell Gumpa tradingcards here soon!",
		"I'm saving up for a new skateboard.",
		),
	"dialog_skatepark":(
		"haha, what are you doing here?",
		"oh you skate huh?",
		),
	"dialog_home" : (
		"What are you doing at my home?",
		"This is my place.",		
		),
	}

class Girl():
	def __init__(self,name, p):
		self.name = name
		self.current_room = "b1"
		self.destination = None
		self.rect = [892,40,16,32]
		self.real_rect = [892,40,16,32]
		self.surf = pygame.Surface((16,32))
		self.surf.set_colorkey((0,255,0))
		self.surf.fill((0,255,0))
		self.surf.blit(engine.images.images[self.name][0], (0,0))
		
		self.speed = 0.035
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
		d = engine.time.days[(engine.time.day-1)%7]
		if d == "saturday" or d == "sunday": 	sched = "schedule_weekends"
		else: sched = "schedule_days"
		for s in self.properties[sched]:
			if engine.time.hour == s[0]: self.destination = s
				
		if self.destination != None:
			if self.current_room != self.destination[1]:
				if self.real_rect[0] < 585: self.move("right")
				elif self.real_rect[0] > 700: self.move("left")
				else: self.current_room = self.destination[1]
			else:
				if self.real_rect[0] < self.destination[2]-2: self.move("right")
				elif self.real_rect[0] > self.destination[2]+2: self.move("left")
				else: self.current_frame = 0; self.draw()
				
			self.rect[0] = round(self.real_rect[0])
				
	def move(self, d):
		self.frame_clock += 1
		if self.frame_clock > self.frame_speed:
			self.frame_clock = 0
			self.current_frame += 1
			if self.current_frame >= len(self.animations[self.current_animation])-1:
				self.current_frame = 0
			if d == "left":
				self.real_rect[0] -= self.speed
				self.current_animation = "w_left"
			else:
				self.real_rect[0] += self.speed
				self.current_animation = "w_right"
			self.draw()
	
	def draw(self):
		self.surf.fill((0,255,0))
		cf = self.animations[self.current_animation][self.current_frame]
		self.surf.blit(engine.images.images[self.name][cf], (0,0))			
		
	def talk(self):
		engine.text.mw(self.name + ": "+ choice(self.properties["dialog_unknown"]))
		
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
				
			