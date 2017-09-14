import __builtin__
import pygame
from script.engine import Engine
class GameApp():
	def __init__(self):
		__builtin__.pygame = pygame
		__builtin__.engine = Engine()
		engine.load()
app = GameApp()
