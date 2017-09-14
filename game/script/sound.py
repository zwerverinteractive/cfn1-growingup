# -*- coding: utf-8 -*-
class Sound():
	def __init__(self):
		print("Loading sound.")
		try:
			pygame.mixer.init()
		except pygame.error:
			print >>sys.stderr, "Could not initialize sound system: %s" % exc
		sounds = []
		self.sound = {}
		for s in sounds:
			self.sound[s] = pygame.mixer.Sound("data/sound/" + s + ".wav")
					
	def playSound(self,n):
		self.sound[n].stop()
		self.sound[n].play(l)
		
	def playMusic(self,n):
		pygame.mixer.music.load("data/music/" + n + ".ogg")
		pygame.mixer.music.set_volume(1)
		pygame.mixer.music.play(-1)
		
	def fadeOutMusic(self, length):
		pygame.mixer.music.fadeout(length)