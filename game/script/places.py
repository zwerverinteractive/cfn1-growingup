# -*- coding: utf-8 -*-
from random import randint, choice

class Places:
	def __init__(self):
		self.lockerwarning = 0
		
	def enter(self, location):
		player = engine.player
		if location == "office supply":
			c = engine.text.ch(["Buy a pen. 5$", "Buy a piece of paper. 1$", "leave"])
			if c == 0:
				if player.inventory["pen"] == False:
					if player.money > 5:
						player.money -= 5
						player.inventory["pen"] = True
						engine.sound.playSound("buy")
						engine.text.mw("You acquired a pen!")
					else: engine.text.mw("You don't have enough money.")
				else: engine.text.mw("You have no need for another pen as you know perfectly well how not to lose it.")
			if c == 1:
				if player.inventory["paper"] == False:
					if player.money > 1:
						player.money -= 1
						player.inventory["paper"] = True
						engine.sound.playSound("buy")
						engine.text.mw("At last! You have a piece of paper!")
					else: engine.text.mw("You don't even have a single lousy buck.")
				else: engine.text.mw("You can only carry one piece of paper. (Because game-logic.)")
			if c == 2:
				engine.text.mw("You leave the office supply store.")
				
		elif location == "clothing store":
			c = engine.text.ch(["Buy tuxedo. 150$", "Buy dress 200$", "Buy sunglasses. 25$", "leave"])
			if c == 0:
				if player.inventory["tuxedo"] == False:
					if player.money > 150:
						player.money -= 150
						player.inventory["tuxedo"] = True
						engine.sound.playSound("buy")
						engine.text.mw("The storekeeper winks at you as she pulls the tux over the counter. Sharp as a wistle!")
					else: engine.text.mw("You imagine how good that tux would look on you. Sadly, you don't have enough money.'")
				else: engine.text.mw("You already own a tuxedo.")

			if c == 1:
				if player.inventory["dress"] == False:
					if player.money > 200:
						player.money -= 200
						player.inventory["dress"] = True
						engine.sound.playSound("buy")
						engine.text.mw("With a slight stutter you tell the storekeeper it's for someone else, who smiles and wraps it into a beautiful package.")
					else: engine.text.mw("Couragously you take the dress try to pay for it... but it was to expensive.")
				else: engine.text.mw("You already own a dress. Dad might get suspicious if you'd got another one.")
						
			if c == 2:
				if player.inventory["sunglasses"] == False:
					if player.money > 25:
						player.money -= 25
						player.inventory["sunglasses"] = True
						engine.sound.playSound("buy")
						engine.text.mw("Nonchalantly you throw the money on the counter and put on the sunglasses. Bad to the bone, you think to yourself.")
					else: engine.text.mw("Though these sunglasses would look really cool, but you simple can't afford them.")
				else: engine.text.mw("You already own a pair of sunglasses.")
			if c == 3:
				engine.text.mw("You leave the clothing store.")

		elif location == "toy store":
			c = engine.text.ch(["Buy skateboard. 100$", "Buy basketball 50$", "Buy trading-cards. 10$", "leave"])
			if c == 0:
				if player.inventory["skateboard"] == False:
					if player.money > 100:
						player.money -= 100
						player.inventory["skateboard"] = True
						engine.sound.playSound("buy")
						engine.text.mw("You pull your fingers over the wheel, making them purr for a good few seconds and hand over the money.")
						engine.text.mw("You can skate by holding shift and move around town a lot faster!")
					else: engine.text.mw("You imagine yourself riding the curbs, wind in your hair. Sadly your purse is too light.")
				else: engine.text.mw("You already own a skateboard.")
			if c == 1:
				if player.inventory["basketball"] == False:
					if player.money > 50:
						player.money -= 50
						player.inventory["basketball"] = True
						engine.sound.playSound("buy")
						engine.text.mw("Ah, throwing the ol' b-ball! You pass it clumsily through your legs before legally turning it into your posession.")
					else: engine.text.mw("That ball... is too expensive.")
				else: engine.text.mw("You have no need for another basketball.")
			if c == 2:
				if player.inventory["tradingcards"] > 100:
					engine.text.mw("There's no need to buy any more trading-cards. Your collection is complete!")
				else:
					if player.money > 10:
						player.money -= 10
						engine.text.mw("After pointing a finger at the Gobamen trading-card pack and trade it in for money you peel off its skin and look at the cards.")
						if player.inventory["tradingcards"] == 0:
							engine.sound.playSound("buy")
							engine.text.mw("Oh boy! Your very first cards! Eight of them!")
							player.inventory["tradingcards"] += 8
						else:
							c = randint(0,8)
							if c == 0: engine.text.mw("Oh no! You already have all of these!")
							elif c < 4: engine.text.mw("Meh! You already have most of these!")
							elif c < 8: engine.text.mw("Not bad! A decent amount of new cards!")
							elif c == 8: engine.text.mw("Wow, lucky chance! You didn't have any of these!")
							engine.sound.playSound("buy")
							player.inventory["tradingcards"] += c
							
							if player.inventory["tradingcards"] > 100:
								engine.text.mw("Finally...")
								engine.text.mw("After all this time...")
								engine.text.mw("you collection...")
								engine.text.mw("is...")
								engine.text.mw("complete!!!!!!!!")
					else:
						if player.inventory["tradingcards"] > 0: engine.text.mw("Must... Have... Gobamen... The clerk shakes his head as you show him the insides of your pockets.")
						else: engine.text.mw("Though you feel a certain itch looking at the trading-cards, you just can't afford them right now.")
			if c == 3:
				engine.text.mw("You leave the toysbme.")

		elif location == "art store":
			c = engine.text.ch(["Buy paint. 50$", "Buy brush. 5$", "Buy canvas. 10$", "leave"])
			if c == 0:
				if player.inventory["paint"] == False:
					if player.money > 50:
						player.money -= 50
						player.inventory["paint"] = True
						engine.sound.playSound("buy")
						engine.text.mw("You take from the shelves all the colors of the rainbow and give the artisan some money.")
					else: engine.text.mw("With all that paint you could make a really pretty painting. Sadly, you don't have enough money.")
				else: engine.text.mw("You already have enough paint.")
			if c == 1:
				if player.inventory["brush"] == False:
					if player.money > 5:
						player.money -= 5
						player.inventory["brush"] = True
						engine.sound.playSound("buy")
						engine.text.mw("You put the brush under your nose, pretending it to be a moustache before handing over the money.")
					else: engine.text.mw("To bad, your purse is to light to acquire the brush.")
				else: engine.text.mw("You already have a brush.")
						
			if c == 2:
				if player.inventory["canvas"] == False:
					if player.money > 10:
						player.money -= 10
						player.inventory["canvas"] = True
						engine.sound.playSound("buy")
						engine.text.mw("You close one eye, staring at the canvas with the other, imagining what to put on it, then pay for it.")
					else: engine.text.mw("You do not have enough money to buy the canvas, your vision will have to wait.")
				else: engine.text.mw("You should finish your painting before buying a new canvas.")
			if c == 3:
				engine.text.mw("You leave the art store.")
		elif location == "gym":
			c = engine.text.ch(["get subscription 25$", "work out", "leave"])
			if c == 0:
				if player.inventory["gym-sub"] == False:
					player.inventory["gym-sub"] = True
					engine.sound.playSound("buy")
					engine.text.mw("Gym trainer: First month's free, after that it's 25$ a month.")
				else:
					engine.text.mw("Gym trainer: You already have a subscription here, silly.")
			elif c == 1:
				if player.inventory["gym-sub"] == False: engine.text.mw("Gym trainer: You need a subscription to train here, pal.")		
				else:
					if engine.time.hour >= 18:
						engine.text.mw("Gym trainer: Sorry, pal. A training session is 2 hours, and you'd be home late. Let's do it tomorrow!")
					else:
						engine.time.hour += 2
						r = randint(0,10)
						if r != 0:
							player.stats["strength"] += 2
							engine.text.mw("You push yourself to the limit for a couple of hours. Strength increased!")
							engine.text.mw("Gym trainer: Way to go, pal! Feel the burn!")
							engine.sound.playSound("statup")
						else:
							engine.text.mw("You waste a couple of hours not finding it in you to really push yourself.")
							engine.text.mw("Gym trainer: To bad, pal! But don't feel bad, you'll do better next time.")
			elif c == 2:
				engine.text.mw("You leave the gym.")
							
		elif location == "skatepark":
			if player.inventory["skateboard"] == True:
				r = randint(0,12)
				engine.time.hour += 2	
				if r == 12:
					player.stats["cool"] += 6
					engine.text.mw("Cruisin' that halfpipe and hitting your grinds perfectly. Cool significantly increased!")
					engine.text.mw("Skaterpunk: Gnarly, dude. You sponsored or something?")
					
					engine.sound.playSound("statup")
				elif r == 1:
					player.stats["cool"] -=2
					engine.text.mw("Ouch! You made a pretty nasty fall and ripped your pants. Cool decreased. ")
					engine.text.mw("Skaterpunk: Haha, ouch, that was painful to watch, dude.")
				elif r == 0:
					engine.text.mw("For some reason you feel a bit scared to get hurt and just sit around.")
					engine.text.mw("Skaterpunk: ...")
				else:
					player.stats["cool"] += 2
					engine.text.mw("What a nice feeling to go down that ramp. And you even landed a couple of tricks. Cool increased.")
					engine.sound.playSound("statup")
					engine.text.mw("Skaterpunk: Yeah, you know what you're doing. See you around!")
			else:
				engine.text.mw("You don't own a skateboard, so you have no choice but to hang around for a couple of hours.")
				engine.text.mw("Skaterpunk: Eh, there's really no reason to be here without wheels, dude.")
				engine.text.mw("Cool ever slightly increased")
				player.stats["cool"] += 1
				engine.sound.playSound("statup")
				engine.time.hour += 2
		elif location == "library":
			c = engine.text.ch(["get library card 5$", "read books"])
			if c == 0:
				if player.inventory["library-sub"] == False:
					player.inventory["library-sub"] = True
					engine.text.mw("Librarian: First month's free, after that it's 5$ a month. Happy reading!")
				else:
					engine.text.mw("Librarian: Didn't you already have a library card?")
			elif c == 1:
				if player.inventory["library-sub"] == False: engine.text.mw("Librarian: Can I see your library card please?")		
				else:
					if engine.time.hour >= 19:
						engine.text.mw("Librarian: Shouldn't you'd be going home? Why don't you come back tomorrow!")
					else:
						engine.time.hour += 2
						r = randint(0,10)
						if r != 0:
							player.stats["intelligence"] += 2
							engine.text.mw("You immersed yourself in a really good book.  Intelligence increased!")
							engine.sound.playSound("statup")
							engine.text.mw("Library: You looked really concentrated. Clearly an aficionado of the written word.")
						else:
							engine.text.mw("You waste a couple of hours staring blankly at the pages and rereading scentenses.")
							engine.text.mw("Librarian: Remind me to give you the chair that doesn't squeek next time.")
		elif location == "playground":
			if engine.time.hour >= 19:
				engine.text.mw("Dad almosts expects you home, staying here would probably make him worried.")
			else:
				engine.time.hour += 2
				r = randint(0,10)
				if r > 5:
					player.stats["romance"] += 1
					player.stats["intelligence"] += 1
					engine.text.mw("You sit on the swing and ponder. Am I to old for this playground stuff? What will the future bring? Who will take care of me when dad's gone?")
				else:
					engine.text.mw("You go down the slide a couple of times, then play hide and seek with some of the neighbourhood kids.")
		elif location == "park":
			if engine.time.hour >= 19:
				engine.text.mw("Dad expects you home, staying here would probably make him worried.")
			else:
				engine.time.hour += 2
				if player.inventory["paint"] and player.inventory["brush"] and player.inventory["canvas"] and randint(0,1) == 0:
					engine.text.mw("Feeling inspired, and owning everything needed to paint, you decide to do exactly that.")
					player.painting += 1
					if player.painting > 3:
						player.painting = 0
						engine.text.mw("At long last you finish your painting! And what a beauty it is!")
						engine.text.mw("Creativity significantly increased, cool slightly increased.")
						engine.sound.playSound("statup")
						
						price = player.stats["creativity"] * randint(1,6)
						engine.text.mw("Passerby: Hey, that's pretty good! I wouldn't mind having that over my fireplace! I'll buy it for " + str(price) + "$")
						c = engine.text.ch(["sure!", "no thanks!"])
						if c == 0:				
							engine.text.mw("You sell the painting for" + str(price) + "$.")
						else:
							engine.text.mw("Passerby: Ah, keeping it for someone special, eh?")
							player.paintings += 1				
						player.money += price
						player.stats["creativity"] += 6
						player.stats["cool"] += 1
					else:
						engine.text.mw("You make decent progress on your painting. Creativity increased.")
						engine.sound.playSound("statup")
						player.stats["creativity"] += 2
				else:
					r = randint(0,10)
					if r > 5:			
						engine.text.mw("You stroll around the park for a couple of hours and notice all the intricate shapes in nature.")
						engine.text.mw("Creativity slightly increased.")
						engine.sound.playSound("statup")
						player.stats["creativity"] += 1
					else:
						engine.text.mw("You sit on a bench for a couple of hours, staring at the ducks, thinking of a certain girl.")
						engine.text.mw("Romance increased.")
						engine.sound.playSound("statup")
						player.stats["romance"] += 1
				
		elif location == "lake":
			if engine.time.hour >= 19:
				engine.text.mw("Dad would get worried if you stayed here.")
			else:
				engine.time.hour += 2
				if player.inventory["pen"] and player.inventory["paper"] and randint(0,1) == 0:
					engine.text.mw("Looking at that beautiful lake, and the air feeling especially friendly, you write the following poem...")
					p = engine.text.poem()
					engine.text.mw(p)
					player.poems.append(p)
					engine.text.mw("romance and creativity increased.")
					player.stats["romance"] += 2
					engine.sound.playSound("statup")
					player.stats["creativity"] += 1
					
				else:
					engine.text.mw("For some reason sitting here always makes you think about talking to girls and holding their hand.")
					engine.text.mw("Romance slightly increased.")
					engine.sound.playSound("statup")
					player.stats["romance"] += 1
					
		elif location == "basketball court":
			if player.inventory["basketball"]:
				if engine.time.hour >= 19:
					engine.text.mw("Dad would get worried if you stayed here.")
				else:
					engine.time.hour += 2
					if player.stats["strength"] >= 25:
						engine.text.mw("You win a game of  basketball! Strength and cool increased.")
						engine.sound.playSound("statup")
						engine.text.mw("Basketball player: *pant* *pant* Wowee, that's some fine bouncin'! Didn't stand a chance!'")
						player.stats["strength"] += 2
						player.stats["cool"] += 1
					else:
						engine.text.mw("You lose a game of  basketball, and it hurts. It hurts bad. Strength and cool decreased.")
						engine.text.mw("Basketball player: Beat it, twerp!'")
						player.stats["strength"] -= 1
						player.stats["cool"] -= 1
			else:
				engine.text.mw("You don't have a ball to play with")
				engine.text.mw("Basketball player: You think you can beat me? You don't even have a ball! Haha!")
				
		elif location == "pool":
			if self.lockerwarning == 99:
				engine.text.mw("The pool manager, not having forgotten your face stands up from his seat the moment you enter and points to the door with a stern face.")
				engine.text.mw("You leave the swimming pool.")
			else:
				if engine.time.hour >= 19:
					engine.text.mw("Dad would get worried if you stayed here.")
				else:
					engine.text.mw("You enter the swimming pool, a powerful scent of chloride filling your nostrils.")
					c = engine.text.ch(["swim 5$", "look at girls locker room 5$", "leave"])
					if c == 0:
						if player.money > 5:
							engine.time.hour += 2
							player.money -= 5
							engine.text.mw("You jump into the pool and pull a couple of laps. Strength increased.")
							engine.sound.playSound("statup")
							engine.text.mw("Pool manager: Nothing like a good swim to boost your health!")
							player.stats["strength"] += 1
						else:
							engine.text.mw("You don't have enough money to swim.")
							engine.text.mw("Pool manager: That chloride ain't free, you know.'")
					if c == 1:
						warnings = [
							"I don't know if that's such a good idea...",
							"really...that's very unethical. don't.",
							"I'm warning you nicely, bad things will come of this."
							]
						
						if self.lockerwarning <= 2:
							engine.text.mw(warnings[self.lockerwarning])
							engine.text.mw("The narrator, me, kicks you out of the swimming pool.")
							self.lockerwarning += 1
						else:
							if player.money > 5:
								player.money -= 5
								engine.text.mw("You take a brief moment before opening the girl''s locker room door.")
								engine.text.mw("Like a spie you manouver yourself into a spot where you can see them, but they can't see you.")
								engine.text.mw("Just as your eyes glance at the slightest bit of bare skin a loud 'hey!' is heard from behind you.")
								engine.text.mw("You try to turn around and run away but trip on the floor in front of everybody. All the girls shriek as loud as their lungs allow.")
								engine.text.mw("The manager rushes to the scene and drags you out of his establishment by your ear.")
								engine.text.mw("Pool manager: And don't show your face here ever again!")
								engine.text.mw("Cool decreased to absolute zero.")
								engine.text.mw("You are banned from the swimming pool.")
								player.stats["cool"] = 0
								self.lockerwarning = 99
							else:
								engine.text.mw("You don't have enough money to swim, and therefore not enough to peek into the girls locker room.")
					if c == 2:
						engine.text.mw("You leave the swimming pool.")
			
		elif location == "school":
			trivia = [
				"The capital of Italy is Rome.",
				"W is a letter, and red is a color.",
				"Be sure to open a door before entering it",
				"When the going gets water, the tough get curly-fries ...or was it the other way around?",
				"Math is cool when infinity is involved!",
				"An electric eel can produce a shock of up to 650 volts.",
				"German Shepherds bite humans more than any other breed of dog.",
				"Moles are able to tunnel through 300 feet of earth in a day.",
				"The anaconda, one of the world's largest snakes, gives birth to its young instead of laying eggs.",
				"Julius Caesar and Napoleon Bonaparte both suffered from epilepsy.",
				"The New York phone book had 22 Hitlers listed before World War II ... and none after.",
				"There are more insects in one square mile of rural land than there are human beings on the entire earth.",
				"A pineapple is a berry.",
				"One pound of tea can make 300 cups of tea.",
				"Mercury is the only metal that is liquid at room temperature.",
				"The air we breathe is 78% nitrogen, 21.5% oxygen, .5% argon and other gases.",
				"An ounce of gold can be stretched into a wire 50 miles long.",
				"The game of volleyball was invented in 1895 by William G. Morgan.",
				"There are 100 tiles in a 'Scrabble' crossword game.",
				"Only 55% of all Americans know that the sun is a star.",
				"Uranus is the only planet that rotates on its side.",	
				]
			
			if engine.time.hour == 8:
				engine.text.mw("You made it to school in time.")
				t=15
			elif engine.time.hour == 9:
				engine.text.mw("You are a bit late, but the teacher forgives you.")
				engine.text.mw("Teacher: Don't forget, school starts at nine, but you are expected to be early.")
				t=15
			else:
				engine.text.mw("You are very late. The teacher points to the door.")
				engine.text.mw("Teacher: The principal, now!")
				engine.text.mw("The Principal doesn't even look up from his paperwork.")
				engine.text.mw("Principal: Detention, two hours. Room 302.")
				t =17
				engine.text.mw("You head back to class.")
				
			engine.text.mw("You try to pay attention, but you can only think about what you're going to do when it's all over.")
			engine.text.mw("Finally the bell rings.")
			engine.text.mw("Teacher: Ok, see you next time.")
			engine.text.mw("Teacher: And don't forget now. " + choice(trivia))
			engine.time.hour = t
			engine.player.school = True
			engine.time.minute = 0
		
		elif location == "church":
			preach = [
				"Jer 29:11: For I know the plans I have for you, declares the LORD, plans to prosper you and not to harm you, plans to give you hope and a future.",
				"John 3:16: For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
				"Rom 8:28: And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
				"Phil 4:13: I can do everything through him who gives me strength.",
				"Gen 1:1: In the beginning God created the heavens and the earth.",
				"Prov 3:5: Trust in the LORD with all your heart and lean not on your own understanding.",
				"Prov 3:6: in all your ways acknowledge him, and he will make your paths straight.",
				"Phil 4:6: Do not be anxious about anything, but in everything, by prayer and petition, with thanksgiving, present your requests to God.",
				"Matt 28:19: Therefore go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit.",
				"Eph 2:8: For it is by grace you have been saved, through faith—and this not from yourselves, it is the gift of God—",
				"Gal 5:22: But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness,",
				"John 10:10: The thief comes only to steal and kill and destroy; I have come that they may have life, and have it to the full.",
				"John 15:13: Greater love has no one than this, that he lay down his life for his friends.",
				"Rom 10:17: Consequently, faith comes from hearing the message, and the message is heard through the word of Christ.",
				"John 1:12: Yet to all who received him, to those who believed in his name, he gave the right to become children of God—",
				"Jas 1:3: because you know that the testing of your faith develops perseverance.",
				"Rom 8:38: For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers,",
				"Rom 8:39: neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.",
				"Phil 1:6: being confident of this, that he who began a good work in you will carry it on to completion until the day of Christ Jesus.",
				"Ps 133:3: It is as if the dew of Hermon were falling on Mount Zion. For there the LORD bestows his blessing, even life forevermore.",
				"Heb 4:16: Let us then approach the throne of grace with confidence, so that we may receive mercy and find grace to help us in our time of need.",
				"Ps 37:4: Delight yourself in the LORD and he will give you the desires of your heart.",
				"John 3:17: For God did not send his Son into the world to condemn the world, but to save the world through him.",
				"Acts 4:12: Salvation is found in no one else, for there is no other name under heaven given to men by which we must be saved.",
				"Isa 26:3: You will keep in perfect peace him whose mind is steadfast, because he trusts in you.",
				"1 Pet 2:24: He himself bore our sins in his body on the tree, so that we might die to sins and live for righteousness; by his wounds you have been healed.",
				"Matt 28:18: Then Jesus came to them and said, All authority in heaven and on earth has been given to me.",
				"Col 3:23: Whatever you do, work at it with all your heart, as working for the Lord, not for men,",
				"Matt 22:37: Jesus replied: Love the Lord your God with all your heart and with all your soul and with all your mind.",
				"Ps 133:2: It is like precious oil poured on the head, running down on the beard, running down on Aaron’s beard, down upon the collar of his robes.",
				"Matt 5:16: In the same way, let your light shine before men, that they may see your good deeds and praise your Father in heaven.",
				"Isa 55:8: For my thoughts are not your thoughts, neither are your ways my ways, declares the LORD.",
				"John 13:35: By this all men will know that you are my disciples, if you love one another.",				
				]
			
			if engine.time.hour == 9:
				engine.time.hour = 11
				engine.time.minute = 00
				engine.text.mw("You enter the building and after a handshake and some coffee the sermon begins.")
				engine.text.mw("Preacher: " + choice(preach))
				engine.text.mw("People pray and go away leaving you with nothing to say. Creativity slightly increased.")
				engine.sound.playSound("statup")
				player.church += 1
				player.stats["creativity"] += 1
			elif engine.time.hour > 9:
				engine.text.mw("The sermon has already started. Best not to disturb it.")
		elif location == "paper":
			engine.text.mw("You enter the newspaper office. People are franticly running around for no apparant reason.")
			if player.job == False:
				ch =  engine.text.ch(["apply for delivery route", "leave"])
				if ch == 0:
					engine.text.mw("chief: The job is simple. Grab some papers and deliver them to all the houses every day.")
					engine.text.mw("chief: I don't really care what time they are delivered, as long as they reach their destination on the same day.")
					engine.text.mw("chief: Don't miss any houses or I won't pay you.")
					engine.text.mw("chief: Think you can manage that?")
					ch = engine.text.ch(["yes", "no"])
					if ch == 1: engine.text.mw("chief: To bad, you look like the kind of guy that's going places'. Come back when you change your mind.")
					else:
						engine.text.mw("chief: allright, that's great. here, take todays paper and deliver them, willya?")					
						engine.text.mw("chief: The people of pope-town are counting on you!")		
						player.job = True
						player.papers = True
				else:
					engine.text.mw("chief: bye, now!")
			else:		
				ch =  engine.text.ch(["take daily papers","collect pay", "leave"])
				if ch == 0:
					if player.delivered:
						engine.text.mw("chief: You already delivered todays papers.")
					else:
						if player.papers == False:
							player.papers = True
							engine.text.mw("chief: Here's' todays paper. Kindly deliver them.")
						else:
							engine.text.mw("chief: You already have todays papers. Go deliver them, silly!")
				elif ch == 1:
					if player.salary > 0:
						engine.text.mw("chief: here's the money we owe you. have fun with it.")
						player.money += player.salary
						player.salary = 0
					else:
						engine.text.mw("chief: you haven't made any money yet!'")
				else:
					engine.text.mw("chief: bye, now!")