"""
File: snakeGame.py
Goal: To Create a New and Improved Snake Game with Mobs a Gun and a Score system 
Developer: Jc
"""

import pygame
from enum import Enum
import random

#Initializing Pygame 
pygame.init() 


#Default Template For all States In the Game 
class State:

	def __init__(self):
		pass
	#Abstract Method 
	def update(self,keys,dt):
		raise NotImplementedError("Update Method Not Implemented in State Class")

	#Abstract Method
	def draw(self, screen):
		raise NotImplementedError("Draw Method Not Implemented in State Class")

class Entity(pygame.sprite.Sprite):

	def __init__(self, rect, imageFile):

		#initializing the parent class with this entity
		pygame.sprite.Sprite.__init__(self)

		#To use features of the Sprite class each sprite must have an image and rect 
		self.image = pygame.image.load(imageFile)
		self.image = pygame.transform.scale(self.image, (rect.width,rect.height)) #Ensuring its the correct Dimensions 
		self.rect = rect

	#Update method of all Entities Must Have 
	def update(self,keys,dt):
		pass

	#Draws the Entitiy on the screen 
	def draw(self,screen):
		screen.blit(self.image, self.rect)

#Simple Enum class
class Dir(Enum):

	UP = 1 
	DOWN = 2
	RIGHT = 3 
	LEFT = 4

	pass

#Player Class 
class Player(Entity):
	#rect imageFile
	def __init__(self, rect, imageFile, speedDebuff):
		
		super().__init__(rect,imageFile) #initializing the Player 
		self.dir = Dir.RIGHT #initially the player is facing right 
		self.speedDebuff = speedDebuff
	#Updates the Player 
	def update(self,keys,dt):

		#Choosing the direction of the player 
		self.__direction(keys)

		#Constantly Moving the Player based on his direction 
		self.__movePlayer(dt)

	#Determines the Direction the Player 
	def __direction(self, keys):


		if keys[pygame.K_w]:
			self.dir = Dir.UP
		if keys[pygame.K_s]:
			self.dir = Dir.DOWN
		if keys[pygame.K_d]:
			self.dir = Dir.RIGHT
		if keys[pygame.K_a]:
			self.dir = Dir.LEFT

	#Constantly Moves the Player 
	def __movePlayer(self,dt):

		if self.dir == Dir.UP:
			self.rect.top -= (self.rect.height / self.speedDebuff)
		if self.dir == Dir.DOWN:
			self.rect.top += (self.rect.height / self.speedDebuff)
		if self.dir == Dir.RIGHT:
			self.rect.left += (self.rect.width / self.speedDebuff)
		if self.dir == Dir.LEFT:
			self.rect.left -= (self.rect.width / self.speedDebuff)

#Defining a Fruit Class 
class Fruit(Entity):
	def __init__(self, screenW, screenH,imageFile):

		#Its Position will always be random 
		rect = random.randInt

		super().__init__(rect,imageFile)



#The Actual Game 
class GameState(State):

	def __init__(self, screenW, screenH):

		self.screenW = screenW
		self.screenH = screenH 
		#pygame.Rect(left, top, width, height)
		self.background = Entity(pygame.Rect((0,0),(screenW,screenH)), "space.jpg")

		#rect, imageFile, speed debuff
		speedDebuff = 4
		self.player = Player(pygame.Rect((screenW//2, screenH//2), (20,20)), "head.png", speedDebuff)


	#Overriding the Abstract Update Method 
	def update(self,keys,dt):
		self.player.update(keys,dt)
		pass

	#Overriding the Abstract Draw Method 
	def draw(self,screen):

		#Drawing the background first 
		self.background.draw(screen)
		#Drawing the Player 
		self.player.draw(screen)
		pass


	pass


#Controls the States of the Game 
class Game:

	def __init__(self,screenW,screenH):

		#Creating the Screen Where We draw everything onto 
		self.screen = pygame.display.set_mode((screenW,screenH))
		pygame.display.set_caption("New And Improved SNAKE GAME")

		#List Containing all the Game States of the Game 
		self.states = [GameState(screenW,screenH)] #Change to Main Menu State Later  


	#Starts the Game 
	def start(self):
		self.__mainGameLoop()

	#Main Game Loop Of the Game 
	def __mainGameLoop(self):

		isOver = False

		#RGB
		SCREEN_COLOR = (75,150,150)

		#Helps control the speed of the game 
		clock = pygame.time.Clock()

		while not isOver:

			#Controls the Speed of the Game 
			dt = clock.tick(60)

			#Event Loop Handler 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					isOver = True

			#Updating the Screen 
			self.screen.fill(SCREEN_COLOR)

			#Getting a List of booleans of every key in the game 
			keys = pygame.key.get_pressed()

			#Updating all The components of the Game 
			self.__updateComponents(keys,dt)

			#Drawing all the components of the Game
			self.__drawComponents()

			#Updating the Screen 
			pygame.display.update()

		#Quitting Pygame
		pygame.quit()

	def __updateComponents(self,keys,dt):

		#Ensuring We have a State to update its components 
		if len(self.states) > 0:
			#Last In First Out 
			self.states[len(self.states) - 1].update(keys,dt)


	def __drawComponents(self):

		#Ensuring we have a State to Draw its components
		if len(self.states) > 0:
			#Last In first out 
			self.states[len(self.states) - 1].draw(self.screen)



def main():

	screenW = 800 
	screenH = 800
	newSnakeGame = Game(screenW,screenH)

	newSnakeGame.start()


if __name__ == "__main__":
	main()





















