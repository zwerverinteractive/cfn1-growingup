# -*- coding: utf-8 -*-
class Player():
	def __init__(self):
		engine.objects.append(self)
		self.real_rect = [40,42,16,32]
		self.rect = [40,42,16,32]
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
		for a,b in enumerate(self.real_rect):
			self.rect[a] = round(b)
			
				