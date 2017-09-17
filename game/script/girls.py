# -*- coding: utf-8 -*-

girl = {}
girl["zoe"] = {
	"stats" : {
		"strength" : 6,
		"cool" : 10,
		"intelligence" : 4,
		"romance" : 3,
		"creativity" : 4,		
		},
	"schedule" : (
		#time, 	room, 	x
		((7,0),		"b1", 	512), #School
		((15,0),		"b1",	100), #Skatepark
		((19,0),		"b1",	200), #Home
		),
	}

class Girl():
	def __init__(self, stats):
		self.room = "b1"
		self.rect = [400,40,16,32]
		self.surf = pygame.Surface((16,32))
		self.surf.blit(engine.images.images["player"][0], (0,0))
		self.surf.set_colorkey((0,255,0))
		self.speed = 0.05
		self.love = 0
		self.know = 0
		self.stats = stats

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
		pass