import pygame.font
from pygame.sprite import Group
from dead_fish import Dead_fish

class Scoreboard():
	"""Класс для вывода игровой информации."""
	"""Class for displaying game information."""

	def __init__(self, ai_game):
		"""Инициализирует атрибуты подсчёта очков."""
		"""Initializes scoring attributes."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Настройки шрифта для вывода счета.
		# Font settings for invoice display.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		# Подготовка исходного изображения.
		# Preparing the original image.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_dead_fish()
		self.prep_life()

	def prep_dead_fish(self):
		# Вывод количества жизней в левой части экрана.
		# Displays the number of lives on the left side of the screen.
		self.dead_fishs = Group()
		for fish_number in range(self.stats.fishs_left):
			dead_fish = Dead_fish(self.ai_game)
			dead_fish.rect.x = 10 + fish_number * dead_fish.rect.width
			dead_fish.rect.y = 50
			self.dead_fishs.add(dead_fish)	

	def prep_score(self):
		"""Преобразует текущий счёт в графическое изображение"""
		"""Converts the current score into a graphical image"""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

		# Вывод счета в правой части экрана.
		# Display the score on the right side of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_level(self):
		"""Преобразует уровень в графическое изображение."""
		"""Converts the level into a graphical image."""
		level_str = str(f"level {self.stats.level}")
		self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
		# Уровень выводится под текущим счётом.
		# The level is displayed under the current score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_life(self):
		"""Вывод надписи Жизнь над изображением жизней"""
		"""Output of the inscription Life above the image of lives"""
		life_str = str("Life")
		self.life_image = self.font.render(life_str, True, self.text_color, self.settings.bg_color)
		self.life_rect = self.level_image.get_rect()
		self.life_rect.left = self.screen_rect.left + 70
		self.life_rect.top = self.screen_rect.top + 10

	def prep_high_score(self):
		"""Преобразует рекордный счёт в графическое изображение."""
		"""Converts the record score into a graphical image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		record_str = str(f"record {high_score_str}")
		self.high_score_image = self.font.render(record_str, True, self.text_color, self.settings.bg_color)
		# Рекорд выравнивается по центру верхней стороны.
		# The record is aligned to the center of the top side.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def show_score(self):
		"""выводит счёт на экран"""
		"""displays the score on the screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.life_image, self.life_rect)
		self.dead_fishs.draw(self.screen)

	def check_high_score(self):
		"""Проверяет появление рекорда."""
		"""Checks for the appearance of a record."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()