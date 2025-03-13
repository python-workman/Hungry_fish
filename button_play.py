import pygame.font

class Button():
	
	def __init__(self, ai_game, msg):
		"""Инициализирует атрибуты кнопки."""
		"""Initializes the attributes of the button."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Назначение размеров и свойств кнопки.
		# Assigning button sizes and properties.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Построение объекта rect кнопки и выравнивание по центру экрана.
		# Construct a rect button object and align it to the center of the screen.
		self.rect = pygame.Rect(850, 900, self.width, self.height)
		#self.rect.center = self.screen_rect.center

		# Сообщение кнопки создаётся только один раз.
		# The button message is created only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Преобразует msg в прямоугольник и выравнивает текст по центру."""
		"""Converts msg to a rectangle and aligns the text to the center."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Отображение пустой кнопки и вывод сообщения.
		# Display an empty button and display a message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
