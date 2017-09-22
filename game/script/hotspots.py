# -*- coding: utf-8 -*-

spots = {}


spots["home-up"] = {
	"borders" : (90, 336),
	"exits" : [
		#u/d  hotspot,	 new room,		new pos
		["d", (188, 218), "home-down", 115], #STAIRCASE DOWN
		]
	}
	
spots["home-down"] = {
	"borders" : (29, 361),
	"exits" : [
		["u", (25, 45), "b1", 380], #FRONT DOOR
		["u", (110, 126), "home-up", 190], #STAIRCASE UP
		]
	}

spots["a1"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(580, 593), "b1", 697],#CROSSROAD L
		["u",(688, 703), "b2", 585],#CROSSROAD R
		["d",(120, 140), "a2", 1150],#CROSSING L
		["d",(1140, 1160), "a2", 130],#CROSSING R
		],
	"places": [
		["u",(145,157), 		"office supply", 	((8,30),(18,00)),	["monday", "tuesday", "wednesday", "thursday", "friday"]],
		["u",(272,297), 		"clothing store", 	((8,30),(18,00)),	["monday", "tuesday", "wednesday", "thursday", "friday"]],
		["u",(407,433), 		"toy store",		((8,30),(18,00)),	["monday", "tuesday", "wednesday", "thursday", "friday"]],
		["u",(514,527), 		"art store", 		((8,30),(18,00)),	["monday", "tuesday", "wednesday", "thursday", "friday"]],
		["u",(795,809), 		"gym", 			((8,30),(20,00)),	["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],
		["u",(826,960), 		"skatepark", 		None,				["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],		
		["u",(1074,1097), 	"library", 			((13,00),(17,00)),	["monday", "tuesday", "wednesday", "thursday", "friday"]],
		]
	}

spots["a2"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(580, 593), "b2", 697],#CROSSROAD L
		["u",(688, 703), "b1", 585],#CROSSROAD R
		["d",(120, 140), "a1", 1150],#CROSSING L
		["d",(1140, 1160), "a1", 130],#CROSSING R
		],
	"places": [
		["u",(210,322), 		"playground", 	None,	["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],
		["u",(932,992), 		"park", 			None,	["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],		
		["u",(1092,1118), 	"lake", 			None,	["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],
		],
	"houses": [
		["u", (103,118), "Tanya"],
		["u", (762,775), "Unknown"],		
		]
	}

spots["b1"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(366, 390), "home-down", 	30],#HOME FRONT DOOR
		["u",(580, 593), "a2", 			697],#CROSSROAD L
		["u",(688, 703), "a1", 			585],#CROSSROAD R
		["d",(120, 140), "b2", 1150],#CROSSING L
		["d",(1140, 1160), "b2", 130],#CROSSING R
		
		],
	"places": [
		["u",(980,1144), "basketball court", None,	 ["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],		
		],	
	"houses": [
		["u", (83,97), "Jenny"],
		["u", (223,237), "Miranda"],
		["u", (373,385), "Your"],
		["u", (809,822), "Lisa"],
		["u", (883,897), "Zoe"],
		]
	}
	
spots["b2"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(580, 593), "a1", 697],#CROSSROAD L
		["u",(688, 703), "a2", 585],#CROSSROAD R
		["d",(120, 140), "b1", 1150],#CROSSING L
		["d",(1140, 1160), "b1", 130],#CROSSING R
		
		
		],
	"places": [
		["u",(406, 433), 	"pool", 		((10,00),(15,00)), 	["sunday", "thursday"]],
		["u",(755,780), 		"school", 	((8,30),(14,00)),	["monday", "tuesday", "wednesday", "thursday", "friday"]],
		["u",(904, 929), 	"church", 	((9,00),(11,00)),	["sunday"]],
		["u",(1020,1042),	"paper", 	((6,00),(15,00)),	["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]],
		]
	}