# -*- coding: utf-8 -*-
class Dialog:
	def __init__(self):
		pass
		
	def talk(self, person, location, destination):
		t = engine.text
		print(person, location, destination)
		
		if person.name == "Jenny":
			if person.run == True:
				t.mw(name+": Just leave me alone, ok?")	
			else:
				if person.know > 2: name = person.name
				else: name = "girl"
				if person.know == 0:
					t.mw(name+": Oh hello...")
					person.know += 1
				elif person.know == 1:
					t.mw(name+": euh...do I know you?")
					person.know += 1
				elif person.know == 2:
					t.mw(name+": Hey, I've seen you around! What is your name?")
					c = t.ch(["Tell her your name.", "Stare at her blindly."])
					if c == 0:
						t.mw("Jenny :That's a cool name duuuude. My name is jenny, nice to meet you.")
						person.know += 1
					else:
						t.mw("girl: Whatever, dude.")
				elif person.know == 3:
					if engine.player.stats["strength"] < 5:
						t.mw(name+": It was nice to meet you, but I don't really talk to wimps.")
					else:			
						t.mw(name+": Those are some very nice biceps, have you been working out?")
						person.know += 1
				elif person.know == 4:
					t.mw(name+": hey, sup?")
					c = t.ch(["ask for work-out tips", "nothing"])
					if c == 0:
						t.mw("That's a really cool question. Personally, i like pumping iron. But cardio is really great too.")
						person.know += 1
					else:
						t.mw(name+": Same here. See you around!")
				elif person.know == 5:
					t.mw(name+": hey, sup?")				
					c = t.ch(["ask to pump iron with you","ask if she wants to feel your biceps", "oh nevermind"])
					if c == 0:
						t.mw(name+": Sure, if you think you can handle it. i want to see you cry.")
						t.mw(name+": Meet me at the gym, jimbo.")
						person.know += 1
					elif c == 1:
						if engine.player.stats["strength"] > 15:
							t.mw(name+" touches your upper arm and squeezes it a bit.")
							t.mw(name+": Not bad!")
							t.mw(name+": Let's work out together! Meet me at the gym.")
							person.know += 1
						else:
							t.mw(name+": Haha, those flimsy things? Not a chance.")
					else:
						t.mw(name+": Allright now, byebye!")
				elif person.know == 6:
					if person.location == "the gym":
						t.mw(name+": Glad you could make it. Are you ready for this?")
						t.mw("You are pushed to your very limits, seeing jenny doing the same.")
						t.mw("Both your faces turn blood-red as you battle out to see who lasts the longest.")
						if engine.player.stats["strength"] > 25:						
							t.mw("Just as you think you can't feel your arms anymore, Jenny collapses.")
							t.mw("You rush to her aid.")						
							t.mw("She's fine. She looks up at you with droopy eyes.")
							t.mw(name+": Oh wow, you really know how to push it!")
							t.mw(name+": I didn't expect you to have that much stamina! I'm thoroughly impressed.")
							engine.time.hour += 1
							person.know += 1
						else:
							t.mw("She pwns and laughs at you.")
							t.mw(name+": I knew it. Once a wimp, always a wimp.")
							t.mw("Better train more, or you'll never impress her.")
							engine.time.hour += 1
					else:
						t.mw(name+": This is not the gym. I said meet me at the gym, didn't I?")
					
				elif person.know == 7:
					t.mw(name+": Hey hotshot! What's up?")
					c = t.ch(["ask if she likes to wrestle", "ask about music video", "ask about fish"])
					if c == 0:
						t.mw(name+": yeah! wrestle-bingo is my favourite show me and my family watch is every sunday.")
						person.know += 1
					elif c == 1:
						t.mw(name+": uhhh yeah... it was quite cool I guess")
					else:
						t.mw(name+"whaaaaa....?")
				elif person.know == 8:
					t.mw(name+": Can I meet you at the basketball court? I have something to tell you.")
					c = t.ch(["of course!", "can't"])
					if c == 0:
						t.mw(name+": Cool. Ok, I'll see you there.")
						person.know += 1
					else:
						t.mw(name+": Ok... some other time then. It's pretty important though.")
				elif person.know == 9:
					t.mw(name+": Hey! Glad you could show up!")
					t.mw("She looks at you silently for a minute, then turns away and looks at a tree.")
					t.mw(name+": I feel kind of bummed out.")
					t.mw(name+": i found out that my little brother is the cat killing gravy-robber.")
					t.mw(name+": I'm a bit confused. I don't know what to do.")
					c = t.ch(["That's terrible. hug?","boys will be boys", "i just dont care, baby."])
					if c == 0:
						t.mw(name+"Yeah it really took a toll on the family, and... yeah i guess I'd like a hug.")
						t.mw("You wrap your arms around " + name + " and she wraps hers around yours.")
						t.mw(name + ": Thanks. I feel loads better.")
						person.know += 1		
						t.mw("Romance increased.")
						engine.player.stats["romance"] += 2			
						t.mw(name+": meet me at the gym when it opens, I have something else to tell you, something even more important.")
	
					elif c == 1:
						t.mw(name+": I guess you're right.")
						t.mw(name+": those pesky cat always ruining our plans, stealing our gravy to sell at the black-cat market. now you now our family-secret.")
						t.mw(name+": meet me at the gym when it opens, I have something else to tell you, something even more important.")
						person.know += 1
					else:
						t.mw(name+": Ah, you're such an idiot.")
						t.mw(name+" sobs and runs away.")
						person.run = True
				elif person.know == 10:
					if person.location == "the gym":
						t.mw(name+": So glad you could make it.")
						t.mw(name+": So... I just wanted to say...")				
						t.mw(name+": That I really like you...")
						t.mw(name+": Do you like me too?")
						c = t.ch(["I do!", "not really, sorry."])
						if c == 0:
							t.mw(name+": Can I kiss you please?")
							c = t.ch(["...yes", "...no"])
							if c == 1: t.mw(name+": I don't care. You're getting a kiss anyway.")					
							t.mw(name+" gives you a short peck on the cheek, then giggles.")
							engine.player.kisses += 1
							person.know += 1
						else:
							t.mw(name+": Oh...I see. That's fine. I understand.")
							t.mw(name+" sobs and runs away.")						
							person.run = True
						
				elif person.know == 11:
					t.mw(name+": Are you my boyfriend now?")
					c=t.ch(["Of course!", "No way!", "Let me think about it some more."])
					if c == 0:
						t.mw(name+": Forever?")
						c=t.ch(["Of course!", "No way!"])
						if c == 0:
							t.mw(name+": Allright, hotshot. I have a boyfriend forever!")
							t.mw(name+": Haha, well ok, boyfriend. Let's hit the gym then!")
							t.mw("And so, you and Jenny decide to stay together forever.")
							t.mw("You grow up to become the owner of your own import-export company.")
							t.mw("You have one kid with Jenny, a very strong boy.")
							t.mw("The end.")
							t.mw("Jenny ending unlocked.")
							engine.bye()
					elif c == 1:
						t.mw(name+": I can't believe you... this is... grrr")
						t.mw(name+" looks sad and runs away.")
						person.run = True
					else:
						t.mw(name+": Take your time, I understand this is a big decision.")

		elif person.name == "Zoe":
			if person.run:
				t.mw(name + " ignores you.")
			else:	
				if person.know > 2: name = person.name
				else: name = "girl"
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
					if engine.player.stats["cool"] < 15:
						t.mw(name+ ": I talked to my friends yesterday about you and they laughed at me for spending time with a loser like you. Could you do something about your cool?")
					else:
						t.mw(name+": Hey, it's you!")
						r = True
						while r:
							t.mw(name+"What's up?")	
							c = t.ch(["Can I ask you a question?", "Nothing much."])
							if c == 0:
								t.mw(name+": Don't ask to ask, fire away!")
								c = t.ch(["What kind of things do you like?","Do you have a boyfriend?","May I kiss you?","Oh nevermind."])
								if c == 0:
									t.mw(name+": Oh tons of things! But if I had to chose I'd say... ")
									t.mw(name+": Extreme sports and Jesus.")	
									self.know += 1
								if c == 1:
									t.mw(name+": Euh... no... why do you ask? Wait, don't answer that.")
								if c == 2:
									t.mw(name+": You? Ew. Gross. No thanks.")
									t.mw(name+": You've lost some cool and romance.")
									engine.player.stats["cool"] -= 1
									engine.player.stats["romance"] -= 1		
							elif c == 1:
								t.mw(name+": Same here. See you around!")
								break
							t.mw(name+": Anything else?")
				elif person.know == 6:
					t.mw(name+": Have you seen my cat? I haven't seen her in such a long time.")
					t.ch(["no"])
					t.mw(name+"Well if you see her, please bring her back to me!")
					person.know += 1
				elif person.know == 7:
					if engine.player.stats["cool"] < 25:
						t.mw(name+": I've done some thinking... If you want to hang out with me, you have to drop the geek act. Be more cool if you want to be with me.")
					elif engine.player.church < 5:
						t.mw(name+": It's to bad you're not going to church on sunday. My parents don't like me hanging out with a non-believer.")
					else:
						t.mw(name+": Hey! Um...can I ask you something personal?")
						c = t.ch(["of course!","sure","I'm not sure I can handle that."])
						if c == 0 or c == 1:
							t.mw(name+": Do you like me?")
							c = t.ch(["yes", "no"])
							if c == 0:
								t.mw(name+": Do you LIKE like me?")
								c = t.ch(["yes", "no"])
								if c == 0:
									t.mw(name+": Oh thats... Come to the skatepark sometime I need to tell you something.")
									person.know += 1
								else: t.mw(name+": Oh nevermind then.")
							else: t.mw(name+": Oh nevermind then.")
						else: t.mw(name+": Oh nevermind then.")
				elif person.know == 9:
					t.mw(name+": So glad you could make it.")
					t.mw(name+": So... I just wanted to say...")				
					t.mw(name+": That I really like you too...")
					t.mw(name+" gives you a short peck on the cheek, then giggles.")
					engine.player.kisses += 1
					person.know += 1
				elif person.know == 10:
					t.mw(name+": Are you my boyfriend now?")
					c=t.ch(["Of course!", "No way!", "Let me think about it some more."])
					if c == 0:
						t.mw(name+": Forever?")
						c=t.ch(["Of course!", "No way!"])
						if c == 0:
							t.mw(name+": OH GOODIE! I have a boyfriend forever!")
							t.mw(name+": Haha, well ok, boyfriend. I'll race you to the skatepark!")
							t.mw("And so, you and Zoe decide to stay together forever.")
							t.mw("You grow up to become the town's radio-host. You have three kids with Zoe.")
							t.mw("The end.")
							t.mw("Zoe ending unlocked.")
							engine.bye()
					elif c == 1:
						t.mw(name+": I can't believe you... this is... grrr")
						t.mw(name+" looks sad and runs away.")
						person.run = True
					else:
						t.mw(name+": Take your time, I understand this is a big decision.")
				
		elif person.name == "Lisa":
			if person.run:
				t.mw(name+": Can you leave me with my books now?")
				t.mw(name+" ignores you.")
			else:		
				if person.know > 2: name = person.name
				else: name = "girl"
				if person.know == 0:
					t.mw(name+": Oh... um... hello there...")
					person.know += 1
				elif person.know == 1:
					t.mw(name+": ...hey...")
					person.know += 1
				elif person.know == 2:
					t.mw(name+": Hey, I've seen you around! What is your name?")
					c = t.ch(["Tell her your name.", "What's it too ya?"])
					if c == 0:
						t.mw("Lisa: That's a cool name duuuude. My name is jenny, nice to meet you.")
						person.know += 1
					else:
						t.mw("girl: How rude!")
				elif person.know == 3:
					if person.location == "the library":
						t.mw(name+": hey, I really like the atmosphere in this beautiful building.")
						c = t.ch(["ask if she's always alone here", "ask if she likes books", "tell her you prefer music videos"])
						if c == 0:
							t.mw(name+": Uhhmm... yeah I guess to. it's nice and quiet here and oh boy do i like books.")
							person.know += 1
						elif c == 1:
							t.mw(name+": Obviously. Books are the greatest things in the whole universe, don't you know.")
							person.know += 1
						else:
							t.mw(name+": To each their own.")
				elif person.know == 4:
					if engine.player.stats["intelligence"] < 25:
						r=choice([
							"the second world war",
							"math",
							"shakespear",
							"music theory"
							])
						
						t.mw(name+": Do you know anything about " + r + "?")
						t.mw("You shake your head. You better become a lot smarter before you can talk to this girl.")
					else:
						t.mw(name+": Oh hello fellow bookworm. hows you journey through the world of books?")
						c = t.ch(["going great", "not so good"])
						if c == 0:
							t.mw(name+": That's the spirit. They're great aren't they? They teleport one to another dimension it seems.")
						elif c == 1:
							t.mw(name+": Aw that's too bad. But don't give up, you have to learn to enjoy them.")
						person.know += 1
						t.mw(name+": you know, last night our cat came home and he was terified whene he saw us eating potatoes with gravy. He started to meow violently and sprinted upstairs. The craziest thing.")
				elif person.know == 5:
					t.mw(name+": Hello there! What can I do for you?")
					while True:
						c=t.ch(["Ask how her cat is doing.", "give her a poem", "Nothing, thanks."])
						if c == 0:
							t.mw(name+": All better, thanks... Wait did you have something to do with that?")
							break
						elif c == 1:
							if len(engine.player.poems) > 0:
								p = engine.player.poems[-1]
								del engine.player.poems[-1]
								t.mw(name+": ow you sure it is for me? hihi. i realy apreciate it. it's lovely. thank you")
								t.mw(name+": " + p)
								person.know += 1
								break
							else:
								t.mw("You haven't written any poems.")
				elif person.know == 6:
					t.mw(name+": Hey!! do you ever think about the future? because i do im afraid that i will end up old and alone with my books.")
					c = t.ch(["all the time", "who cares when you have books"])
					if c == 0:
						t.mw(name+": oh wow. we think very much alike. maybe we can read books together!")
						person.know += 1
					if c == 1:
						t.mw(name+": hehe, yeah... you're right. I'm just being silly.")
						person.run = True
				elif person.know == 7:
					t.mw(name+": 	Hey!!! uhm... yeah... i've been thinking about... you... I mean the poem that you wrote me.")
					t.mw(name+": 	and all that stuff we talked about. do you realy feel this way?")
					c = t.ch(["yes","what?", "no, sorry"])
					if c == 0:
						t.mw(name+": ok, then meet me at the library next time.")
						person.know += 1
					elif c == 1:
						t.mw(name+": oh nevermind...")
					else:
						t.mw(name+": oh... ok... I understand.")
						t.mw(name+" runs home, sobbing.")
						person.run = True
				elif person.know == 8:
					t.mw(name+": So glad you could make it.")
					t.mw(name+": So... I just wanted to say...")				
					t.mw(name+": That I really really like you... so smart and funny.")
					t.mw(name+" gives you a short peck on the cheek, then giggles.")
					engine.player.kisses += 1
					person.know += 1
				elif person.know == 9:
					t.mw(name+": Are you my boyfriend now?")
					c=t.ch(["Of course!", "No way!", "Let me think about it some more."])
					if c == 0:
						t.mw(name+": Forever?")
						c=t.ch(["Of course!", "No way!"])
						if c == 0:
							t.mw(name+": Hooray. I have a boyfriend forever!")
							t.mw(name+": Haha, well ok, boyfriend. I have a wonderful novel we can read together!")
							t.mw("And so it was, you and Lisa decide to stay together forever.")
							t.mw("You grow up to become a best-selling author. You have two bright kids with Lisa.")
							t.mw("The end.")
							t.mw("Lisa ending unlocked.")
							engine.bye()
					elif c == 1:
						t.mw(name+": I can't believe you... this is... grrr")
						t.mw(name+" looks sad and runs away.")
						person.run = True
					else:
						t.mw(name+": Take your time, I understand this is a big decision.")
						
		elif person.name == "Miranda":
			if person.run:
				t.mw(name+": You've got some nerve talking to me.")
			else:
				if person.know > 2: name = person.name
				else: name = "girl"
				if person.know == 0:
					t.mw(name+": Hey!")
					person.know += 1
				elif person.know == 1:
					t.mw(name+": Hello!")
					person.know += 1
				elif person.know == 2:
					t.mw(name+": What's your name?")
					c = t.ch(["tell her your name", "stare at her"])
					if c == 0:
						t.mw("Miranda: Well hello. I'm Miranda. How very nice to meet you.")
						person.know += 1
					elif c == 1:
						t.mw("Ok, mystery-boy.")
				elif person.know == 3:
					t.mw(name+": Have you seen that beautiful romantic sunrise? it truly touches the soul.")
					c = t.ch(["Yes, serene and touching", "what sunrise?", "i wasnt looking"])
					if c == 0:
						t.mw(name+": Beautiful, wasn't it")
						t.mw("She pretends to remove a tear from her eye.")
						person.know += 1
					elif c == 1:
						t.mw(name+": you know, this morning's sunrise? Nevermind.")
					elif c == 2:
						t.mw(name+": can't even appreciate a sunrise. pfff.")
				elif person.know == 4:
					if player.stats["romance"] < 10:
						t.mw(name+": That's no way to approach a lady. You need to learn a bit about romance!")
					else:
						t.mw(name+": Hello again. i've see you around the lake a couple times. Pretty isn't it?")
						c = t.ch(["Gorgious", "was just looking for my marbles", "wasn't me"])
						if c == 0:
							t.mw(name+": It's truly my favourite pace.")
							person.know += 1
						elif c == 1:
							t.mw(name+": how quaint.")
						else:
							t.mw(name+": then it must have been someone who looks like you.")
				elif person.know == 5:
					if player.inventory["tuxedo"]:	
						t.mw(name+": Hello.  you know, you look just like that famous actor.")
						t.mw(name+": if you turn your head just the right way.")
						while True:
							c = t.ch(["give her a poem", "give her the dress", "ask for picknick at the lake"])
							if c == 0:
								if len(engine.player.poems) > 0:
									p = engine.player.poems[-1]
									del engine.player.poems[-1]
									t.mw(name+": for me? how thoughtful, romantic and sweet of you")
									t.mw(name+": " + p)
									t.mw(name+": Aaaw, that's so cute. Thanks a lot!")
									break
								else:
									t.mw("You haven't written any poems.")
							elif c == 1:
								if player.inventory["dress"]:
									t.mw(name+": for me? ow wow! I'm so excited and totaly not creeped out!!!")
									t.mw(name+": this is like in the romance movies, (and thrillers about stalkers)")
									person.know += 1
									break
								else:
									t.mw("You don't have a dress to give.")			
					else:
						t.mw(name+": Hmm. You got the moves, but you look weird.")
						t.mw(name+": If you want to spend more time with me, you need to do something about that outfit.")
				elif person.know == 6:
					if engine.player.stats["romance"] > 25:
						t.mw(name+": Hello there, my shiny knight.")
						c = t.ch(["ask for picknick at the lake", "say goodbye"])
						if c == 0:
							t.mw(name+": I would love to. I'll see you there!")
							person.know += 1
						else:
							t.mw(name+": Goodbye, my liege.")
					else:
						t.mw(name+": If you want things to become more serious, you have to be even more romantic!")
				elif person.know == 7:
					if person.location != "the lake":
						t.mw(name+": The lake... meet me at the lake!")
					else:
						t.mw("You and Miranda start your picknick.")
						t.mw(name+": oohh this picknick is wonderfull, and ever so romantic.")
						t.mw(name+": but... i need to get something of my chest ")
						t.mw(name+": this is exactly what my mom and dad told me. When a boy buys me a dress and...")
						t.mw(name+": Well...")
						t.mw(name+": now i have to kiss you on the lips. close your eyes.")
						t.mw(name+" gives you a long kiss on the lips. You feel sparks in your head and tummy.")
						t.mw(name+": Well that was all very wonderful. But, I have to go now, see you around!")
						player.kisses += 1
						person.know += 1
				elif person.know == 8:
					t.mw(name+": Are you my boyfriend now?")
					c=t.ch(["Of course!", "No way!", "Let me think about it some more."])
					if c == 0:
						t.mw(name+": Forever?")
						c=t.ch(["Of course!", "No way!"])
						if c == 0:
							t.mw(name+": Oh this so perfect. Almost like a romance novel!")
							t.mw(name+": Haha, well ok, boyfriend. Let's go to the lake and look at eachother.")
							t.mw("And so, you and Miranda decide to stay together forever.")
							t.mw("You grow up to become a very poor poet. After 7 years of marriage you divorce.")
							t.mw("The end.")
							t.mw("Miranda ending unlocked.")
							engine.bye()
					elif c == 1:
						t.mw(name+": I can't believe you... this is... grrr")
						t.mw(name+" looks sad and runs away.")
						person.run = True
					else:
						t.mw(name+": Take your time, I understand this is a big decision.")
					
		elif person.name == "Tanya":
			if person.run:
				t.mw(name+" pretends you're not there'.")
			else:
				if person.know > 2: name = person.name
				else: name = "girl"
				if person.know == 0:
					t.mw(name+": Yo")
					person.know += 1
				elif person.know == 1:
					t.mw(name+": Sup.")
					person.know += 1
				elif person.know == 2:
					t.mw(name+": Tell me your name.")
					c = t.ch(["Tell her your name.", "Don't"])
					if c == 0:
						t.mw("Tanya:  Ok, my name is Tanya.")
						person.know += 1
					else:
						t.mw("girl: Ok. yo.")
				elif person.know == 3:
					t.mw(name+": I'm sufacating in this town. Seems like there is no room for my creativity.")
					t.mw(name+": This town is bankrupt, culturally and artistically.")
					person.know += 1
				elif person.know == 4:
					if engine.player.stats["creativity"] < 15:
						t.mw(name+": you are not creative, you are just like the rest. Just like everyone else.")
					else:
						t.mw(name+": eh..hey, do you like the work of this underground artist buttercream?")
						c = t.ch(["heard he is real hush hush about his vision", "yeah he's pretty brutal", "noop"])
						if c == 0 or c == 1:
							t.mw(name+": 	Yeh boi, mad aesthetics.")
							person.know += 1
						else:
							t.mw(name+": 	hmmkey")
				elif person.know == 5:
					t.mw(name+": eh.")
					c = t.ch(["Give painting", "nvm"])
					if c == 0:
						if engine.player.paintings > 0:		
							engine.player.paintings -= 1		
							t.mw(name+": For me? Hmm, let's see.")
							if engine.player.stats["creativity"] < 25:
								t.mw(name+": Composition is not that great.")
								t.mw(name+": Bland colors, they lack feeling.")
								t.mw(name+": Also, it doesn't really say or mean anything.")
								t.mw(name+": Try again. I'm not impressed.")
							else:
								t.mw(name+": Composition is very daring.")
								t.mw(name+": Very interesting colors, they scream at me.")
								t.mw(name+": Ah and this represents life before birth?")
								t.mw(name+": This is very good, thank you very much!")
								t.mw(name+": Will you sign it for me? Thanks!")
								person.know += 1
								t.mw(name+": Tell you what, meet me in the park next time I'm there.")
								t.mw(name+": I have to show you what I've been working on, could use some feedback.")
				elif person.know == 6:
					if person.location != "the park":
						t.mw(name+": I can't show you my piece here. Meet me in front of the park.")
					else:
						t.mw(name+": Glad you could show up.")
						t.mw(name+" Pulls your hand, leading you to a secluded place in the park.")
						t.mw(name+": Before I show you, I have to tell you a bit about where I come from.")
						t.mw(name+" looks especially pretentious for a second.")
						t.mw(name+":  i have always been creative, even in de womb of my mother,")
						t.mw(name+":  but I started painting a bit later, using my cat as a model.")
						t.mw(name+":  but a couple of weeks ago he just dissapeared so i didn''t realy have a good reference.")
						t.mw(name+":  so I stopped drawing and started working on this performance-art piece.")
						t.mw(name+":  close your eyes when you're ready.")
						t.mw("The moment you close your eyes you feel Tanya's soft lips brush against yours.")
						t.mw(name+":  Well? What do you think?")
						engine.player.kisses += 1
						person.know += 1
				elif person.know == 7:				
					t.mw(name+": Are you my muse now?")
					c=t.ch(["Of course!", "No way!", "Let me think about it some more."])
					if c == 0:
						t.mw(name+": Forever?")
						c=t.ch(["Of course!", "No way!"])
						if c == 0:
							t.mw(name+": Oh this so perfect. Like willem and elaine de kooning!")
							t.mw(name+": Haha, well ok, my muse. Let's go to the park and paint eachother.")
							t.mw("And so, you and Tanya decide to stay together forever.")
							t.mw("You grow up to become a succesful art-critic. You and Tanya die holding hands during a plane crash.")
							t.mw("The end.")
							t.mw("Tanya ending unlocked.")
							engine.bye()
					elif c == 1:
						t.mw(name+": I can't believe you... this is... grrr")
						t.mw(name+" looks sad and runs away.")
						person.run = True
					else:
						t.mw(name+": Take your time, I understand this is a big decision.")
	
	if player.kisses > 4:
		t.mw("You head home with a thumping heart, knowing you just kissed every girl in town.")
		t.mw("As you close the door behind you your dad looks at you with a smirk on his face.")
		t.mw("Dad: You didn't think I'd find out huh? You're the talk of the town, son!")
		t.mw("Dad: I'm so proud of you. Just like the old man, huh?")
		t.mw("And so you go through life single, yet never lonely.")
		t.mw("And you grow up to be a techno dj and cocaine addict, dying age 38 of multiple STD's and heart failure.")
		t.mw("Your funeral was packed.")
		t.mw("Playboy ending unlocked, have a nice day!")
		engine.bye()