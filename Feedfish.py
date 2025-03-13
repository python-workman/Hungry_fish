import pygame

from pygame.sprite import Sprite


class Feedfish(Sprite):
	"""Класс, представляющий одну рыбу"""
	"""Class representing one fish"""

	def __init__(self, ai_game):
		"""Инициализирует рыбов и задаёт её начальную позицию."""
		"""Initializes the fish and sets its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings =ai_game.settings

		# Загрузка изображения рыбов и назначение атрибута rect.
		# Load an image of fish and assign a rect attribute.
		self.image = pygame.image.load('images/feed_fish.PNG')
		self.rect = self.image.get_rect()

		# Сохранение точной горизонтальной позиции рыбы.
		# Maintain the exact horizontal position of the fish.
		self.x = float(self.rect.x)


	def update(self):
		"""Перемещает рыбов влево."""
		"""Moves fish to the left."""
		self.x -= self.settings.feedfish_speed
		self.rect.x = self.x
