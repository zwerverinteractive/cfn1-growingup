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
		]
	}

spots["a2"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(580, 593), "b2", 697],#CROSSROAD L
		["u",(688, 703), "b1", 585],#CROSSROAD R
		]
	}

spots["b1"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(366, 390), "home-down", 30],#HOME FRONT DOOR
		["u",(580, 593), "a2", 697],#CROSSROAD L
		["u",(688, 703), "a1", 585],#CROSSROAD R
		]
	}
	
spots["b2"] = {
	"borders" : (10, 1250),
	"exits" : [
		["u",(580, 593), "a1", 697],#CROSSROAD L
		["u",(688, 703), "a2", 585],#CROSSROAD R
		]
	}