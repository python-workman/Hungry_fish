import pygame

class Fish():
	"""Класс для управления рыбой."""
	"""Class for controlling fish."""
	def __init__(self, ai_game):
		"""Инициализирует рыбу и задает её начальную позицию."""
		"""Initializes the fish and sets its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Загружает изображение рыбы и получает прямоугольник.
		# Loads an image of a fish and gets a rectangle.
		self.image = pygame.image.load('images/fish.png')
		self.rect = self.image.get_rect()

		# рыба по центру экрана. 
		# fish in the center of the screen.
		self.rect.center = self.screen_rect.center
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# Сохранение вещественной координаты центра рыбы
		# Storing the real coordinate of the fish's center
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Обновляет позицию рыбы с учетом флага."""
		"""Updates the fish's position based on the flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.fish_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.fish_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.fish_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.fish_speed
		# Обновление атрибута rect на основаниии self.x.
		# Updating the rect attribute based on self.x.
		self.rect.x = self.x
		self.rect.y = self.y	

	def blitme(self):
		"""Рисует рыбу в текущей позиции."""
		"""Draws a fish at the current position."""
		self.screen.blit(self.image, self.rect)

	def center_fish(self):
		"""Размещает рыбу в центе экрана"""
		"""Places the fish in the center of the screen"""
		self.rect.center = self.screen_rect.center
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
