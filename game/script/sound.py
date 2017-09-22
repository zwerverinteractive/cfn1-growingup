# -*- coding: utf-8 -*-
class Sound():
	def __init__(self):
		print("Loading sound.")
		try:
			pygame.mixer.init()
		except pygame.error:
			print >>sys.stderr, "Could not initialize sound system: %s" % exc
		sounds = ["buy", "corner","newspaper","newspaperdone","statup",
			"step", "talkbeep", "stair", "door", "car", "done", "skate"
			]
		self.sound = {}
		for s in sounds:
			self.sound[s] = pygame.mixer.Sound("data/sound/" + s + ".ogg")
			self.sound[s].set_volume(0.5)
		self.current_song = None
					
					
	def playSound(self,n):
		self.sound[n].stop()
		self.sound[n].play()
		
	def playMusic(self,n):
		pygame.mixer.music.load("data/music/" + n + ".ogg")
		pygame.mixer.music.set_volume(0.4)
		pygame.mixer.music.play(-1)
		self.current_song = n
		
	def fadeOutMusic(self, length):
		pygame.mixer.music.fadeout(length)