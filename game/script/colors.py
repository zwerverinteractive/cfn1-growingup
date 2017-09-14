# -*- coding: utf-8 -*-
class Colors():
	def __init__(self):
		print("Loading colors.")
		self.l0 = 0
		self.l1 = 63
		self.l2 = 127
		self.l3 = 255
		self.colors = {}
		self.loadColors()	
		
	def loadColors(self):
		l0 = self.l0
		l1 = self.l1
		l2 = self.l2
		l3 = self.l3
		self.colors["BLACK"] = [l0, l0, l0]
		self.colors["DGRAY"] = (l1, l1, l1)
		self.colors["LGRAY"] = (l2, l2, l2)
		self.colors["WHITE"] = (l3, l3, l3)
		self.colors["LRED"] = (l3, l2, l2)
		self.colors["RED"] = (l3, l0, l0)
		self.colors["DRED"] = (l2, l0, l0)
		self.colors["LYELLOW"] = (l3, l3, l2)
		self.colors["YELLOW"] = (l3, l3, l1)
		self.colors["DYELLOW"] = (l2, l2, l1)
		self.colors["LORANGE"] = (l3, l3, l1)
		self.colors["ORANGE"] = (l3, l3, l0)
		self.colors["DORANGE"] = (l2, l2, l0)
		self.colors["LGREEN"] = (l2, l3, l2)
		self.colors["GREEN"] = (l0, l3, l0)
		self.colors["DGREEN"] = (l0, l2, l0)
		self.colors["LBLUE"] = (l2, l2, l3)
		self.colors["BLUE"] = (l0, l0, l3)
		self.colors["DBLUE"] = (l0, l0, l2)
		self.colors["LCYAN"] = (l2, l3, l3)
		self.colors["CYAN"] = (l0, l3, l3)
		self.colors["DCYAN"] = (l0, l2, l2)
		self.colors["LVIOLET"] = (l3, l2, l3)
		self.colors["VIOLET"] = (l3, l0, l3)
		self.colors["DVIOLET"] = (l2, l0, l2)