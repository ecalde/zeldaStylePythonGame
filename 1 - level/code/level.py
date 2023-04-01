# The level file is the core component of the game. It contains the sprites(player, enemies, map) and also deals with their interactions
# Manages hundreds of sprites effectively via groups to give different functionality to each sprite group
import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
	# 1 __init__ method is declared within a class to initialize the attributes of an object as soon as the object is formed
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()						# Get a reference to the currently set display surface

		# sprite group setup
		self.visible_sprites = pygame.sprite.Group()							# 1 create the visible sprite group
		self.obstacle_sprites = pygame.sprite.Group()							# 1 create the obstacle sprite group

		# sprite setup
		self.create_map()

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					Player((x,y),[self.visible_sprites])

	def run(self):																# 1 define the run game to draw the sprites
		# update and draw the game
		self.visible_sprites.draw(self.display_surface)