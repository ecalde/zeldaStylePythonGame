# 1 This is the player for the game
import pygame
from settings import *																		# 1 from settings import everything

class Player(pygame.sprite.Sprite):															# 1 inherit sprite.Sprite from pygame. This is super important
	def __init__(self,pos,groups):															# 1 this method will initiate itself and have a POSition for the sprites and groups.
		super().__init__(groups)															# 1 initiate the class above and pass the groups
		# 1 self.image and rect are the two things you need for any sprite
		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()		# 1 convert_alpha smooths the png's edges
		self.rect = self.image.get_rect(topleft = pos)										# 1 will give the tile a position of topleft

		self.direction = pygame.math.Vector2()												# 1 player direction movement

	def input(self):																		# 1 this is how you get keyboard input for up down left and right
		keys = pygame.key.get_pressed()														# 1 to get keyboard inputs

		if keys[pygame.K_UP]:																# 1 checks if the key is being pressed up
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:															# 1 checks if the key is being pressed down
			self.direction.y = 1
		else:																				# 1 if nothing is being pressed then no direction changes
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:															# 1 checks if the key is being pressed right
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:															# 1 checks if the key is being pressed left
			self.direction.x = -1
		else:																				# 1 if nothing is being pressed then no direction changes
			self.direction.x = 0
