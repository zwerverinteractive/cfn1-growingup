# -*- coding: utf-8 -*-
class Text():
	def __init__(self):
		self.font = pygame.font.Font("data/font/zwerveresque.ttf", 8)
		self.window = None
		
	def m(self, text):
		t = self.font.render(text, 0, (255,255,255), (0, 0, 0,255))
		return t
		
	def s(self, text):
		t = self.font.render(text, 0, (0, 0, 0,255), (255,255,255))
		return t
		
	def mw(self, text):
		self.surf = pygame.Surface((64, 110))
		self.surf.fill((0,0,0))
		self.surf.fill((255,255,255), (1,1,62,108))
		self.surf.fill((0,0,0), (2,2,60,106))	
		self.text = text
		self.words = text.split()
		self.time = 0
		self.time_tick = 50
		self.active = True
		self.processed_lines = []
		self.processed_lines.append("")
		self.current_line = 0
		self.current_word = 0
		self.current_letter = 0	
		while self.active:
			engine.controls.update()
			if self.current_word < len(self.words):
				self.time += 1
				if self.time > self.time_tick:
					self.time = 0
					self.processed_lines[self.current_line] += self.words[self.current_word][self.current_letter]
					self.current_letter += 1
					if self.current_letter >= len(self.words[self.current_word]):
						self.current_letter = 0
						self.current_word += 1
						try:
							self.wordsize = self.font.size(self.words[self.current_word])[0]
						except:
							pass
						self.linesize = self.font.size(self.processed_lines[self.current_line])[0]
						if (self.linesize + self.wordsize) > 54:
							self.current_line += 1
							self.processed_lines.append("")
						else:
							self.processed_lines[self.current_line] += " "
					self.surf.fill((0,0,0))
					self.surf.fill((255,255,255), (1,1,62,108))
					self.surf.fill((0,0,0), (2,2,60,106))		
					for l, line in enumerate(self.processed_lines):
						self.surf.blit(engine.text.m(line), (3,3+(l*8)))
			self.surf.blit(engine.images.images["icons"][1], (53,99))
			engine.screen.blit(self.surf, (10,10))
			engine.flip()
			
			if engine.controls.buttons["down"]:
				engine.controls.buttons["down"] = False
				self.active = False
				break
		
	def ch(self,choices):
		self.surf = pygame.Surface((110, 64))
		self.active = True
		self.sel = 0
		while self.active:
			engine.controls.update()
			if engine.controls.buttons["up"]:
				self.sel -= 1
				if self.sel < 0:
					self.sel = len(choices)-1
				engine.controls.buttons["up"] = False
			if engine.controls.buttons["down"]:
				self.sel += 1
				if self.sel > len(choices)-1:
					self.sel = 0
				print(self.sel)
				engine.controls.buttons["down"] = False
			if engine.controls.buttons["right"]:
				self.active = False
				engine.controls.buttons["right"] = False
				return self.sel
				
			self.surf.fill((0,0,0))
			self.surf.fill((255,255,255), (1,1,108,62))
			self.surf.fill((0,0,0), (2,2,106,60))	
			for i,c in enumerate(choices):
				if i == self.sel:
					self.surf.blit(self.s(c + " ->"), (4, 4+(8*i)))
				else:
					self.surf.blit(self.m(c), (4, 4+(8*i)))
			engine.screen.blit(self.surf, (10,10))
			engine.flip()
			
	def poem(self):
		self.mw("This is a poem, a poem so great. I hope you'll die motherfucker.'")
		return poem
