import pygame

class Fish_menu():
	"""Класс, представляющий заставку."""
	"""Class representing the splash screen."""
	def __init__(self, ai_game):
		"""Инициализирует заставку."""
		"""Initializes the screensaver."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Загрузка картинки назначение атрибута rect.
		# Loading a picture is the purpose of the rect attribute.
		self.image = pygame.image.load('images/fish_menu.png')
		self.rect = self.image.get_rect()

		# картинка по центру.
		# picture in the center.
		self.rect.center = self.screen_rect.center

	def blitme(self):
		"""Рисует картинку в текущей позиции."""
		"""Draws a picture at the current position."""
		self.screen.blit(self.image, self.rect)

