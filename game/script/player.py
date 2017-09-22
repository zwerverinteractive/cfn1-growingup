# -*- coding: utf-8 -*-

class Player():
	def __init__(self):
		engine.objects.append(self)
		self.real_rect = [291,42,16,32]
		self.rect = [291,42,16,32]
		self.surf = pygame.Surface((16,32))
		self.surf.blit(engine.images.images["player"][0], (0,0))
		self.surf.set_colorkey((0,255,0))
		self.kisses = 0
		self.money = 5
		self.poems = []
		self.job = False
		self.delivered = False
		self.papers = False
		self.school = False
		self.deliver = []
		self.salary = 0
		self.painting = 0
		self.paintings = 0
		self.church = 0
		self.speed = 0.05
		self.dad = True; self.firstdad = True
		self.z = True
		self.stats = {
			"strength" : 0,
			"cool" : 0,			
			"intelligence" : 0,
			"romance" : 0,
			"creativity" : 0,
			}
		self.inventory = {}
		inv = ["pen", "paper", "tuxedo", "dress", "sunglasses", "skateboard", "basketball", "paint", "brush", "canvas", "gym-sub", "library-sub"]
		for i in inv:
			 self.inventory[i] = False
		self.inventory["tradingcards"] = 0
		#ANIMATION PROPERTIES
		self.current_animation = "w_left"
		self.current_frame = 0
		self.frame_clock = 0
		self.frame_speed = 64
		self.animations = {
			"w_right" : [0,1,2,3,4],
			"w_left" : [4,5,6,7,8],
			"skate_right" : [8],
			"skate_left" : [9],
			}
		
	def update(self):
		b = engine.controls.buttons
		cr = engine.room.current_room
		borders = engine.room.hotspots[cr]["borders"]
		time = engine.time
		
		if b["left"] or b["right"]:
			self.frame_clock += 1
			if self.frame_clock > self.frame_speed:
				self.frame_clock = 0;
				self.current_frame += 1
			if self.inventory["skateboard"] and b["skate"]:
				engine.sound.playSound("skate")
				self.speed = 0.1
				if b["left"] and self.real_rect[0]+6 > borders[0]:
					self.real_rect[0] -= self.speed; self.current_animation = "skate_left"
				elif b["right"] and self.real_rect[0]+6 < borders[1]:
					self.real_rect[0] += self.speed; self.current_animation = "skate_right"
			else:
				self.speed = 0.05
				if b["left"] and self.real_rect[0]+6 > borders[0]:
					self.real_rect[0] -= self.speed; self.current_animation = "w_left"
				elif b["right"] and self.real_rect[0]+6 < borders[1]:
					self.real_rect[0] += self.speed; self.current_animation = "w_right"

			if self.current_frame >= len(self.animations[self.current_animation])-1:
				self.current_frame = 0
				if self.speed == 0.05: engine.sound.playSound("step")
			self.surf.fill((0,255,0))
			cf = self.animations[self.current_animation][self.current_frame]
			self.surf.blit(engine.images.images["player"][cf], (0,0))
		else:
			self.current_frame = 0
			self.surf.fill((0,255,0))
			cf = self.animations[self.current_animation][self.current_frame]
			self.surf.blit(engine.images.images["player"][cf], (0,0))			
		for x,y in enumerate(self.real_rect):
			self.rect[x] = round(y)

		if self.papers:			
			if "houses" in engine.room.hotspots[cr]: houses = engine.room.hotspots[cr]["houses"]
			else: houses = []
			for h in houses:
				if self.rect[0]+6 > h[1][0] and self.rect[0]+6 < h[1][1]:
					engine.gscreen.blit(engine.images.images["icons"][0], (self.rect[0]+3, self.rect[1]-14))
					if b["up"]:
						if not h[2] in self.deliver:
							self.deliver.append(h[2])
							engine.text.mw("You open the mailbox and slide in an edition.")
							engine.sound.playSound("newspaper")
							b["up"] = False
						else:
							if h[2] != "Your":
								b["up"] = False
								engine.text.mw("Even though you delivered a newspaper to this house already, you slip another one in just to be sure.")
								engine.sound.playSound("newspaper")
		if len(self.deliver)-1 >= 6:
			self.salary += 25
			del self.deliver[:]
			self.deliver = []
			self.delivered = True
			self.papers = False
			engine.text.mw("You hear the spirit-voice of the newspaper chief in the back of your head.")
			engine.text.mw("chief: That's the last of 'em! Good job, kid! Come back to the office any time to recieve your salary.")
			engine.sound.playSound("newspaperdone")

		girls = engine.girls.girls
		for g in girls:
			if girls[g].current_room == engine.room.current_room:
				if self.rect[0]+12 > girls[g].rect[0] and self.rect[0] < girls[g].rect[0]+12:
					engine.gscreen.blit(engine.images.images["icons"][0], (self.rect[0]+3, self.rect[1]-14))
					if b["up"]: girls[g].talk(); b["up"] = False
				
		if "exits" in engine.room.hotspots[cr]: exits = engine.room.hotspots[cr]["exits"]
		else: exits = []
		for e in exits:
			if self.rect[0]+6 > e[1][0] and self.rect[0]+6 < e[1][1]:
				if e[0] == "d": d = 1
				else: d = 0
				engine.gscreen.blit(engine.images.images["icons"][d], (self.rect[0]+3, self.rect[1]-14))
				if (b["down"] and d == 1) or (b["up"] and d == 0):
					self.rect[0] = e[3]; self.real_rect[0] = e[3]
					if e[2] == "home-down" and engine.room.current_room == "home-up": engine.sound.playSound("stair")
					elif e[2] == "home-up" and engine.room.current_room == "home-down": engine.sound.playSound("stair")
					elif engine.room.current_room == "home-down": engine.sound.playSound("door")
					elif e[2] == "home-down": engine.sound.playSound("door")
					else: engine.sound.playSound("corner")
					engine.room.swap(e[2])
					b["down"] = False; b["up"] = False
					
		if "places" in engine.room.hotspots[cr]: places = engine.room.hotspots[cr]["places"]
		else: places = []
		for p in places:
			if self.rect[0]+6 > p[1][0] and self.rect[0]+6 < p[1][1]:
				if p[0] == "d": d = 1
				else: d = 0
				engine.gscreen.blit(engine.images.images["icons"][d], (self.rect[0]+3, self.rect[1]-14))			
				if (b["down"] and d == 1) or (b["up"] and d == 0):
					if (p[3] != None):
						if p[3] == "home-down": self.dad = True
						if (time.hour >= p[3][0][0] and time.hour <= p[3][1][0]) and (time.current_day in p[4]):
							engine.places.enter(p[2])
						else: engine.text.mw("Its not open. A sign says open on " + str(p[4]) + " from " + str(p[3][0][0]) + " till " + str(p[3][1][0]) + ".")
					else: engine.places.enter(p[2])
		
				
		d1 = [
			"hey there sleepypants, you finally woke up? there's not a lot to do here on sunday, so why not explore the town a bit?",
			"Good luck on your first day at school this week!",
			"Look who we have here. Sleep well? Ready for school?",
			"Hey, son. Aren't you still a little young to be drinking coffee?",
			"Mornin'. Thursday is a magic day!",
			"Mornin'.'Friday, almost weekend!",
			"Morning. Its finally weekend. Here, you can have your allowance.",
		]
		
		d2 = [
			"Oh, and please remember, don't leave town and be home before 20:00. Keep an eye on your watch by holding TAB. proud of you, son.",
			"Oh, and I heard the local newspaper is looking for paperboys. could be a way to make some extra money. love you, son",
			"And, hey! love you, son.",
			"I'm proud.",
			"And don't forget, I'm really proud of you, son.",
			"Oh, and do you want to do some board games with me tonight?",
			"Don't go spend it all in one place now.",
			]
		if self.job:
			d2[1] = "Oh, and are you making money delivering newspapers? That's great!"
		
		if engine.room.current_room[0] == "h":
			if engine.sound.current_song != "home":
				engine.sound.playMusic("home")
		else:
			if engine.sound.current_song != "town":
				engine.sound.playMusic("town")
		
		if engine.room.current_room == "home-down":
			if self.dad:
				if self.firstdad:

					if self.rect[0] > 84 and self.rect[0] < 88:
						engine.text.mw("Dad: " + d1[engine.time.day-1%7])
						self.rect[0] -= 5;self.real_rect[0] -= 5;
					elif self.rect[0] > 75 and self.rect[0] < 80:
						engine.text.mw("Dad: " + d2[engine.time.day-1%7])
						self.firstdad = False
				elif engine.time.hour >= 18:
					if self.rect[0] > 84 and self.rect[0] < 88:
						if engine.time.hour > 22:
							engine.text.mw("Dad: Well, well, look what the cat dragged in.")
							engine.text.mw("Dad: You're home late... I went ahead and had supper without you. This is very dissapointing, son.")
							engine.text.mw("Dad: Theres some food left in the fridge you'll have to eat cold.")
							engine.text.mw("Dad, mumbling: try so hard to raise them right...")
							engine.text.mw("You eat the cold food and head up to bed.")
							self.endDay()
						elif engine.time.hour > 21:
							engine.text.mw("Dad: You're home late, son, watch some television while I prepare dinner.")
							engine.text.mw("You watch some tv, eat dinner with dad, do your homework before falling sound asleep...")
							self.endDay()
							
						else:
							engine.text.mw("Dad: Hey, welcome back. If you're done outside, watch some television while I prepare dinner.")
							self.dad = False
				else:
					if self.rect[0] > 84 and self.rect[0] < 88:
						if engine.time.current_day != "sunday" and engine.time.current_day != "saturday" and self.school == False:
							if engine.time.hour > 11:
								engine.text.mw("Dad: Are you sick? What are you doing home now? Why aren't you at school?")
								engine.text.mw("Dad places his hand on your forehead feeling your temperature.")
								engine.text.mw("Dad: sounding slightly emotional: You're fine! What the hell is this? You're dissapointing me, son.")
								engine.text.mw("Dad: Your grounded for the rest of the day. Go upstairs and think about what you've done.")
								engine.text.mw("You spend the rest of the day alone in your room.")
								self.endDay()
							elif engine.time.hour > 9:
								engine.text.mw("Dad: What the hell are you doing here? Get your ass to school, pronto!")
						else:
							if engine.time.hour < 18 and not self.firstdad:
								engine.text.mw("Dad: Son! Shouldn't you be outside having adventures and stuff?")
								self.dad = False
						
			if engine.time.hour >= 18:
				if self.rect[0] > 132 and self.rect[0] < 162:
					engine.gscreen.blit(engine.images.images["icons"][1], (self.rect[0]+3, self.rect[1]-14))
					if b["down"]:
						b["down"] = False
						engine.text.mw("You watch some tv, eat dinner with dad and do your homework before falling sound asleep...")
						self.endDay()
						
	def endDay(self):
		#engine.text.mw("Insert dream-sequence here.")
		engine.room.swap("home-up")
		self.rect = [291,42,16,32]; self.real_rect = [291,42,16,32]
		engine.time.day += 1
		if engine.time.days[(engine.time.day-1)%7] == "saturday":
			engine.time.hour = 9
			engine.time.minute = 30
		elif engine.time.days[(engine.time.day-1)%7] == "sunday":
			engine.time.hour = 8
			engine.time.minute = 30
		else:
			engine.time.hour = 8
			engine.time.minute = 0
		self.dad = True
		self.school = False
		self.firstdad = True
		self.delivered = False
		self.papers = False
		del self.deliver[:]
		self.deliver = []
		self.z = True
		for girl in engine.girls.girls:
			g = engine.girls.girls[girl]
			g.sched = 0
			g.spoken = False
			g.current_room = g.properties["home"][1]
			g.rect[0] = g.real_rect[0] = g.properties["home"][2]
			
		engine.text.mw("Day " + str(engine.time.day) + ". " + engine.time.days[(engine.time.day-1)%7])