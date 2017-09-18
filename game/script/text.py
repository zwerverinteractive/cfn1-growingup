# -*- coding: utf-8 -*-
class TextWindow():
	def __init__(self, parent, text):
		self.surf = pygame.Surface((64, 64))
		self.surf.fill((0,0,0))
		self.surf.fill((255,255,255), (1,1,62,62))
		self.surf.fill((0,0,0), (2,2,60,60))	
		self.parent = parent
		
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
			#engine.draw()
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
							self.wordsize = self.parent.font.size(self.words[self.current_word])[0]
						except:
							pass
						self.linesize = self.parent.font.size(self.processed_lines[self.current_line])[0]
						if (self.linesize + self.wordsize) > 54:
							self.current_line += 1
							self.processed_lines.append("")
						else:
							self.processed_lines[self.current_line] += " "
					self.surf.fill((0,0,0))
					self.surf.fill((255,255,255), (1,1,62,62))
					self.surf.fill((0,0,0), (2,2,60,60))	
					for l, line in enumerate(self.processed_lines):
						self.surf.blit(engine.text.m(line), (3,3+(l*8)))
			self.surf.blit(engine.images.images["icons"][1], (53,53))
			engine.screen.blit(self.surf, (10,10))
			engine.flip()
			
			if engine.controls.buttons["down"]:
				self.active = False
				self.parent.window = None
				break
class Text():
	def __init__(self):
		self.font = pygame.font.Font("data/font/zwerveresque.ttf", 8)
		self.window = None
		
	def m(self, text):
		t = self.font.render(text, 0, (255,255,255), (0, 0, 0,255))
		return t
		
	def mw(self,text):
		self.window = TextWindow(self, text)