# -*- coding: utf-8 -*-
class Dialog:
	def __init__(self):
		pass
		
	def talk(self, person, location, destination):
		t = engine.text
		print(person, location, destination)
		if person.name == "Zoe":
			if person.know > 2: name = person.name
			else: name = "girl"
			
			if location == "church":
				if engine.time.hour > 10: t.mw(name + ": That was a very nice sermon!")
				else:
					if person.know > 1: t.mw(name + ": Oh, hello, you go to church too? That's cool!'")
					else: t.mw(name + ": Just because I like to rock, doesn't mean I can't love Jesus.")
			elif destination == "church": t.mw(name + ": I'm curious about today's sermon at the church!")
			if location == "school":
				if person.know < 2:
					t.mw(name + ": Gah, I hate school.")		
				elif person.know == 3:
					t.mw(name + ": Hey, it's you again. What class are you in?")
					t.mw(name + ": Oh we attend the same class?")	
					
			if person.know == 0:
				t.mw(name + ": oh...hello")
				person.know += 1
			elif person.know == 1:
				t.mw(name + ": euh...do I know you?")
				person.know += 1
			elif person.know == 2:
				t.mw(name + ": hey, I've seen you around. What is your name?")
				c = t.ch(["tell her your name", "stare at her"])
				if c == 0:
					t.mw("zoe: Well hello. I'm zoe!")
					t.mw("zoe: See you around!")
					person.know += 1
				elif c == 1:
					t.mw("She stares back at you and the conversation stops.")
					person.know -= 1
			elif person.know == 3:
				t.mw(name + ": Hey, how are you today?")
				c = t.ch(["good", "fine", "not so good"])
				if c == 0: t.mw(name + ": That's great to hear. Same here!")
				elif c == 1: t.mw(name+ ": Same.")
				elif c == 2: t.mw(name+": Aw, sorry to hear that. My mom says always try to fix your problems!")
				person.know += 1
			elif person.know == 4:
				if engine.player.stats["cool"] < 5: t.mw(name + ": Listen, we can be friends and stuff but you gotta do something about your cool. I can't be seen with someone as uncool as you.")
				else:
					if location == "skatepark":
						if engine.player.inventory["skateboard"]: t.mw(name+": That's a sweet ride! Show me your moves!"); person.know += 1
						else: t.mw(name+": ..euh...where's your skateboard? You don't have one?")
					else:
						t.mw(name + ": Hey, it's you again!")
		 				t.mw(name + ": Are you coming to the skatepark later today?")
						c = t.ch(["sure!", "no, but thanks"])
						if c == 0:
							if engine.player.inventory["skateboard"]: t.mw(name+ ": Allright! See you there, and bring that skateboard of yours.")
							else: t.mw(name+": Cool...oh you don't have a board? Well... maybe some other time then.")
						if c == 1: t.mw(name+ ": To bad, suit yourself.")
			elif person.know == 5:
				t.mw(name+": Hey, it's you!")
				r = True
				while r:
					t.mw(name+"What's up?")	
					c = t.ch(["Can I ask you a question?", "I made you something.", "Nothing much."])
					if c == 0:
						t.mw(name+": Don't ask to ask, fire away!")
						c = t.ch(["What kind of things do you like?","Do you have a boyfriend?","May I kiss you?","Oh nevermind."])
						if c == 0:
							t.mw(name+": Oh tons of things! But if I had to chose I'd say... ")
							t.mw(name+": Extreme sports and Jesus.")	
						if c == 1:
							t.mw(name+": Euh... no... why do you ask? Wait, don't answer that.")
						if c == 2:
							t.mw(name+": You? Ew. Gross. No thanks.")
							t.mw(name+": You've lost some cool and romance.")
							engine.player.stats["cool"] -= 1
							engine.player.stats["romance"] -= 1		
					elif c == 1:
						t.mw("Don't lie to the girl, you haven't made anything.")
					elif c == 2:
						t.mw(name+": Same here. See you around!")
						break
					t.mw(name+": Anything else?")
						
				
				
				