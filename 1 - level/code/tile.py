# 1 This is the tile for the game
import pygame
from settings import *																		# 1 from settings import everything

class Tile(pygame.sprite.Sprite):															# 1 inherit sprite.Sprite from pygame. This is super important
	def __init__(self,pos,groups):															# 1 this method will initiate itself and have a POSition for the sprites and groups.
		super().__init__(groups)															# 1 initiate the class above and pass the groups
		# 1 self.image and rect are the two things you need for any sprite
		self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()			# 1 convert_alpha smooths the png's edges
		self.rect = self.image.get_rect(topleft = pos)										# 1 will give the tile a position of topleft