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
		self.display_surface = pygame.display.get_surface()						# 1 Get a reference to the currently set display surface

		# sprite group setup
		self.visible_sprites = pygame.sprite.Group()							# 1 create the visible sprite group
		self.obstacle_sprites = pygame.sprite.Group()							# 1 create the obstacle sprite group

		# sprite setup
		self.create_map()														# 1 calling the map method

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):								# 1 need to go through the index and the row as well, we go through every single list
			for col_index, col in enumerate(row):								# 1 now we want to go into every list and find the index inside each column, and it'll be the row
				x = col_index * TILESIZE										# 1 this is the x position * the TileSize of 64
				y = row_index * TILESIZE										# 1 this is the y position * the TileSize of 64
				# with the code above you have the world mapped into positions
				if col == 'x':													# 1 if 'x' convert to Tile (rock)
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites])	# 1 to create Tile you need position and group, groups will be visible_sprites and obstacle_sprites
				if col == 'p':													# 1 if 'p' convert to Tile (player)
					Player((x,y),[self.visible_sprites])						# 1 to create Player you need position and group, groups will be visible_sprites

	def run(self):																# 1 define the run game to draw the sprites
		# update and draw the game
		self.visible_sprites.draw(self.display_surface)							# 1 draws all sprites in visible_sprites