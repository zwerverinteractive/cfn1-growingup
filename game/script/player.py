# -*- coding: utf-8 -*-
class Player():
	def __init__(self):
		engine.objects.append(self)
		self.real_rect = [300,42,16,32]
		self.rect = [300,42,16,32]
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
		cr = engine.room.current_room
		exits = engine.room.hotspots[cr]["exits"]
		borders = engine.room.hotspots[cr]["borders"]
		
		if b["left"] or b["right"]:
			self.frame_clock += 1
			if self.frame_clock > self.frame_speed:
				self.frame_clock = 0;
				self.current_frame += 1
			if b["left"] and self.real_rect[0]+6 > borders[0]:
				self.real_rect[0] -= self.speed; self.current_animation = "w_left"
			elif b["right"] and self.real_rect[0]+6 < borders[1]:
				self.real_rect[0] += self.speed; self.current_animation = "w_right"

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

		for e in exits:
			if self.rect[0]+6 > e[1][0] and self.rect[0]+6 < e[1][1]:
				if e[0] == "d": d = 1
				else: d = 0
				engine.gscreen.blit(engine.images.images["icons"][d], (self.rect[0]+5, self.rect[1]-10))
				
				if (b["down"] and d == 1) or (b["up"] and d == 0):
					self.rect[0] = e[3]; self.real_rect[0] = e[3]
					engine.room.swap(e[2])
					b["down"] = False; b["up"] = False