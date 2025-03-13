import pygame

from pygame.sprite import Sprite


class Dead_fish(Sprite):
	"""Класс, представляющий изображение жизней"""
	"""Class representing the image of lives"""
	def __init__(self, ai_game):
		"""Инициализирует рыбов и задаёт её начальную позицию."""
		"""Initializes the fish and sets its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings =ai_game.settings
		# Загрузка изображения рыбов и назначение атрибута rect.
		# Load an image of fish and assign a rect attribute.
		self.image = pygame.image.load('images/dead_fish.PNG')
		self.rect = self.image.get_rect()

		
