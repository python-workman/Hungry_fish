class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""
	"""Class for storing all settings for the Alien Invasion game."""
	def __init__(self):
		"""Инициализирует настройки игры"""
		"""Initializes game settings"""
		# Параметры экрана
		# Screen Options
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (29, 191, 255)
		# Настройки рыбы
		self.fish_limit = 3
		self.speedup_scale = 1.03
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры."""
		"""Initializes settings that change during the game."""
		self.fish_speed = 2
		self.feedfish_speed = 0.4
		self.feedfish_points = 20
		self.shark_speed = 0.7

	def increase_speed(self):
		"""Увеличивает настройки скорости."""
		"""Increases speed settings."""
		self.fish_speed *= self.speedup_scale 
		self.feedfish_speed *= self.speedup_scale
		self.shark_speed *= self.speedup_scale	