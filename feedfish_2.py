import pygame

from pygame.sprite import Sprite


class Feedfish_2(Sprite):
	"""Класс, представляющий одну рыбу"""

	def __init__(self, ai_game):
		"""Инициализирует рыбов и задаёт её начальную позицию."""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings =ai_game.settings

		# Загрузка изображения рыбов и назначение атрибута rect.
		self.image = pygame.image.load('images/feed_fish_2.PNG')
		self.rect = self.image.get_rect()

		# Сохранение точной горизонтальной позиции рыбы.
		self.x = float(self.rect.x)


	def update(self):
		"""Перемещает рыбов влево."""
		self.x -= self.settings.feedfish_speed
		self.rect.x = self.x
