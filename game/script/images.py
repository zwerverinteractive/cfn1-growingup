# -*- coding: utf-8 -*-
import os

def grabSpriteSheet(filename, s, **kwargs): #Originally written by Tom Eyerman, slightly altered.
	base_image = pygame.image.load(filename).convert()
	base_image.set_colorkey((0, 255, 0))
	sprite_width = s
	sprite_height = s
	columns = base_image.get_width() / s
	rows = base_image.get_height() / s
	current_row, current_column = kwargs.get('start', (0, 0))
	end_row, end_column = kwargs.get('end', (rows - 1, columns - 1))
	image_list = []
	current_frame = pygame.Rect(0, 0, sprite_width, sprite_height)
	while current_row <= end_row:
		current_frame.top = sprite_height * current_row
		while (current_row < end_row and current_column < columns) or (current_row == end_row and current_column <= end_column):
			current_frame.left = sprite_width * current_column
			image_list.append(base_image.subsurface(current_frame))
			current_column += 1
		current_column = 0
		current_row += 1
	return image_list
	

class Images():
	def __init__(self):
		print("Loading images.")
		return
		self.images = {}
		types = ["backgrounds"]
		sizes = [12]
		for i, t in enumerate(types):
			self.images[t] = grabSpriteSheet('content/images/' + t + ".png", sizes[i])

