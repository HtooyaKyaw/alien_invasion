class Settings:
	""" A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game settings."""
		#Screen settings

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.ship_speed = 1.5
		self.ship_limit = 3

		#scoring
		self.alien_points = 50
		self.score_scale = 1.5

		#bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 30

		#alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10


		#how quickly the game speed up
		self.speedup_scale = 1.1

		self.initialize_dyanmic_settings()

	def initialize_dyanmic_settings(self):
		"""initialize settings that change through the game"""
		self.alien_speed = 1.5
		self.ship_speed = 1.5
		self.bullet_speed = 1.5

		# fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

	def increase_speed(self):
		self.alien_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.ship_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.speedup_scale)
		print(self.alien_points)