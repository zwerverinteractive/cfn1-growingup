# -*- coding: utf-8 -*-
class Player():
	def __init__(self):
		engine.objects.append(self)
		self.real_rect = [500,42,16,32]
		self.rect = [500,42,16,32]
		self.surf = pygame.Surface((16,32))
		self.surf.blit(engine.images.images["player"][0], (0,0))
		self.surf.set_colorkey((0,255,0))
		self.speed = 0.05
		
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
		b = engine.controls.buttons
		
		if b["left"] or b["right"]:
			self.frame_clock += 1
			if self.frame_clock > self.frame_speed:
				self.frame_clock = 0;
				self.current_frame += 1
			if b["left"]: 	self.real_rect[0] -= self.speed; self.current_animation = "w_left"
			elif b["right"]: 	self.real_rect[0] += self.speed; self.current_animation = "w_right"

			if self.current_frame >= len(self.animations[self.current_animation])-1:
				self.current_frame = 0
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
			
			
		#CROSSROADS
		if self.rect[0]+6 > 580 and self.rect[0]+6 < 596:
			engine.gscreen.blit(engine.images.images["icons"][0], (self.rect[0]+6, self.rect[1] - 12))
			if b["up"]:
				engine.room.swap("lu")
				self.rect[0] = 690; self.real_rect[0] = 690
				b["up"] = False
		elif self.rect[0]+6 > 686 and self.rect[0]+6 < 700:
			engine.gscreen.blit(engine.images.images["icons"][0], (self.rect[0]+6, self.rect[1] - 12))		
			if b["up"]:
				engine.room.swap("ru")
				self.rect[0] = 586; self.real_rect[0] = 586
				b["up"] = False
				
		""" DOWNWARD ZEBRAPATH, TOO DISORIENTING
		if self.rect[0]+6 > 566 and self.rect[0]+6 < 586:
			engine.gscreen.blit(engine.images.images["icons"][1], (self.rect[0]+6, self.rect[1] - 12))
			if b["down"]:
				engine.room.swap("d")
				self.rect[0] = 690; self.real_rect[0] = 690
				b["down"] = False

		if self.rect[0]+6 > 696 and self.rect[0]+6 < 716:
			engine.gscreen.blit(engine.images.images["icons"][1], (self.rect[0]+6, self.rect[1] - 12))
			if b["down"]:
				engine.room.swap("d")
				self.rect[0] = 580; self.real_rect[0] = 580
				b["down"] = False
		"""