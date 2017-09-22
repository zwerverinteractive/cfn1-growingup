# -*- coding: utf-8 -*-
from random import choice

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
		self.time_tick = 1
		self.active = True
		self.processed_lines = []
		self.processed_lines.append("")
		self.current_line = 0
		self.current_word = 0
		self.current_letter = 0
		self.f = True
		while self.active:
			if self.time_tick > 0:
				engine.clock.tick(30)
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
						if (self.linesize + self.wordsize) > 52:
							self.current_line += 1
							self.processed_lines.append("")
						else:
							self.processed_lines[self.current_line] += " "
					self.surf.fill((0,0,0))
					self.surf.fill((255,255,255), (1,1,62,108))
					self.surf.fill((0,0,0), (2,2,60,106))		
					for l, line in enumerate(self.processed_lines):
						self.surf.blit(engine.text.m(line), (4,4+(l*8)))
						engine.sound.playSound("talkbeep")

				if engine.controls.buttons["down"]:
					self.time_tick = 0
					engine.controls.buttons["down"] = False
					engine.sound.playSound("done")
			else:
				if engine.controls.buttons["down"]:
					engine.controls.buttons["down"] = False
					engine.sound.playSound("done")
					self.active = False
					break


			self.surf.blit(engine.images.images["icons"][1], (50,95))
			engine.screen.blit(self.surf, (10,10))
			engine.flip()
		
	def ch(self,choices):
		self.surf = pygame.Surface((110, 64))
		self.active = True
		self.sel = 0
		engine.controls.buttons["up"] = False
		engine.controls.buttons["down"] = False
		engine.controls.buttons["left"] = False
		engine.controls.buttons["right"] = False
		while self.active:
			engine.clock.tick(30)
			engine.controls.update()
			if engine.controls.buttons["up"]:
				self.sel -= 1
				if self.sel < 0:
					self.sel = len(choices)-1
				engine.sound.playSound("done")
				engine.controls.buttons["up"] = False
			if engine.controls.buttons["down"]:
				self.sel += 1
				if self.sel > len(choices)-1:
					self.sel = 0
				engine.sound.playSound("done")
				engine.controls.buttons["down"] = False
			if engine.controls.buttons["right"] or engine.controls.buttons["trick"] or engine.controls.buttons["start"]:
				self.active = False
				engine.controls.buttons["right"] = engine.controls.buttons["trick"] = engine.controls.buttons["start"] =False
				engine.sound.playSound("corner")
				return self.sel
				
			self.surf.fill((0,0,0))
			self.surf.fill((255,255,255), (1,1,108,62))
			self.surf.fill((0,0,0), (2,2,106,60))	
			for i,c in enumerate(choices):
				if i == self.sel:
					self.surf.blit(self.s(" "+ c + " ->"), (4, 4+(8*i)))
				else:
					self.surf.blit(self.m(" " + c), (4, 4+(8*i)))
			engine.screen.blit(self.surf, (10,10))
			engine.flip()
			
	def poem(self):
		pw = [
			"Love.", "Hate.", "Regret.", "The moon.", "The stars.", "The sun." "If only", "Back to the start.",
			"Forever.", "Touch.", "The cold.", "Close by you.", "Longing.", "Starts at the beginning.",
			"However.", "What does it all mean?", "Why am I not brave?", "Lost in translation.",
			"Fall down on their knees.", "Now you understand.", "I stood there and I cried.",
			"My senses,", "leave me deaf and blind.", "Ten thousand saw it happen.", "Does it come as a surprise",
			"Life is fine.", "I think about you.", "Roses are red.", "Meaning."		
			]
		poem = ""
		for i in range(7):
			poem += choice(pw)
		return poem
