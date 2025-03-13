import pygame

from pygame.sprite import Sprite


class Shark(Sprite):
	"""Класс, представляющий одну акулу"""
	"""Class representing one shark"""

	def __init__(self, ai_game):
		"""Инициализирует акулу и задаёт начальную позицию."""
		"""Initializes the shark and sets the starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings =ai_game.settings

		# Загрузка изображения акулы и назначение атрибута rect.
		# Loading a shark image and assigning a rect attribute.
		self.image = pygame.image.load('images/shark.png')
		self.rect = self.image.get_rect()

		# Сохранение точной горизонтальной позиции акулы.
		# Saving the exact horizontal position of the shark.
		self.x = float(self.rect.x)


	def update(self):
		"""Перемещает акул влево."""
		"""Moves sharks to the left."""
		self.x -= self.settings.shark_speed
		self.rect.x = self.x
