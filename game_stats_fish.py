class GameStats():
	"""Отслеживание статистики для игры."""
	"""Tracking statistics for the game."""
	def __init__(self, ai_game):
		"""Инициализирует статистику."""
		"""Initializes statistics."""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False
		# Игра запускается в активном состоянии.
		# The game starts in the active state.
		self.high_score = 0
	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся во время игры."""
		"""Initializes statistics that change during the game."""
		self.fishs_left = self.settings.fish_limit
		self.score = 0
		self.level = 1
		self.level_fish = 1