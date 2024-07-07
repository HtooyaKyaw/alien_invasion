import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship"""
	def __init__(self,ai_game):
	# """initialize the ship and its starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#load the ship image an get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.image = pygame.transform.scale(self.image, (50, 50))

		self.rect = self.image.get_rect()

		#start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		self.x =float(self.rect.x)

		#movement flag
		self.move_right = False
		self.move_left = False

	def update(self):
		"""update the ship's positin based on the movement flag"""
		#these 4 lines of code taught you how to keep the ship within the screen
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.move_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
			#update rect object form self.x
		self.rect.x = self.x

	def blitme(self):
	# """draw the ship at its current location"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
