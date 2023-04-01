# 1 pygame is a cross-platform set of Python modules designed for writing video games.
# 1 sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment
import pygame, sys
from settings import *											# importing everything from settings
from level import Level											# importing level from level
# from debug import debug 										# import debug to view debug. You can add "debug('hello')" to debug at specific parts

class Game:
	# 1 __init__ method is declared within a class to initialize the attributes of an object as soon as the object is formed
	def __init__(self):											# 1 define the init method to initialize the game
		  
		# general setup
		pygame.init()											# 1 initiate pygame
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))	# 1 creating a screen
		pygame.display.set_caption('Zelda')						# Sets the name of the game window
		self.clock = pygame.time.Clock()						# 1 creating a clock

		self.level = Level()
	
	def run(self):												# 1 define the run method
		while True:												# 1 loop to run the game while true
			for event in pygame.event.get():
				if event.type == pygame.QUIT:					# 1 ends the game if QUIT
					pygame.quit()
					sys.exit()

			self.screen.fill('black')							# 1 fill the screen with a solid color
			self.level.run()
			pygame.display.update()								# 1 updating the screen
			self.clock.tick(FPS)								# 1 controlling the FPS. clock.tick = update the clock

if __name__ == '__main__':										# 1 check if this is the main file
	game = Game()												# 1 create an instance of game
	game.run()													# 1 then call method run of the game class