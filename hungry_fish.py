import sys

from time import sleep

import pygame

from settings import Settings

from game_stats_fish import GameStats

from scoreboard import Scoreboard

from button_play import Button

from fish import Fish

from Feedfish import Feedfish

from feedfish_2 import Feedfish_2

from shark import Shark

from fish_menu import Fish_menu

from random import randint

class Hungryfish:
	"""Класс для управления ресурсами и поведения игры."""
	"""Class for managing game resources."""

	def __init__(self):
		"""Инициализирует игру и создаёт игровые ресурсы."""
		"""Initializes the game and creates game resources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Hungry Fish")
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.fish = Fish(self)
		self.feedfishs = pygame.sprite.Group()
		self.feedfishs_2 = pygame.sprite.Group()
		self.sharks = pygame.sprite.Group()
		self.fish_menu = Fish_menu(self)
		self.background_image = pygame.image.load('images/background.jpg')
		pygame.mixer.music.load('sounds/background_music.mp3')
		self.eat_sound = pygame.mixer.Sound('sounds/eat.wav')
		self.loss_sound = pygame.mixer.Sound('sounds/loss.mp3')
		# Создание кнопки Play.
		# Creating a Play Button
		self.play_button = Button(self, "Play")

	def run_game(self):
		"""Запуск основного цикла игры."""
		"""Starting the main game loop."""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.fish.update()
				self._update_feedfishs()
				self._update_feedfishs_flock()
				self._update_feedfishs_flock_2()
				self._update_shark_flock()
			self._update_screen()	

	def _check_events(self):
		"""Обрабатывает нажатия клавиш и события мыши"""
		"""Handles button clicks and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_play_botton(self):
		# Сброс скорости.
		# Speed reset.
		self.settings.initialize_dynamic_settings()
		# Сброс статистики.
		pygame.mixer.music.play(-1)
		self.stats.reset_stats()
		self.stats.game_active = True
		self.sb.prep_score()
		self.sb.prep_level()
		self.sb.prep_dead_fish()
		# Очистка рыбов.
		# fish removal.
		self.feedfishs.empty()
		self.feedfishs_2.empty()
		self.sharks.empty()
		# Создание новой стаи и размещение рыбы в центре.
		# Creating a new flock and placing the fish in the center.
		self._create_flock_fish()
		self.fish.center_fish()


		# Указатель мыши скрывается.
		# The mouse pointer is hidden..
		pygame.mouse.set_visible(False)

	def _check_keydown_events(self, event):		
		if event.key == pygame.K_RIGHT:
			self.fish.moving_right = True 
		elif event.key == pygame.K_LEFT:
			self.fish.moving_left = True
		elif event.key == pygame.K_UP:
			self.fish.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.fish.moving_down = True
		elif event.key == pygame.K_p:
			self._check_play_botton()
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_1:
			pygame.mixer.music.pause()
		elif event.key == pygame.K_2:
			pygame.mixer.music.unpause()
		elif event.key == pygame.K_3:
			pygame.mixer.music.unpause()
			pygame.mixer.music.set_volume(0.2)

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.fish.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.fish.moving_left = False
		elif event.key == pygame.K_UP:
			self.fish.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.fish.moving_down = False

	def _update_feedfishs(self):
		"""Обновляет позиции всех рыб в стае."""
		"""Updates the positions of all fish in the flock."""
		self.sharks.update()
		self.feedfishs.update()
		self.feedfishs_2.update()
		self._collide_feedfishs()
		self._collide_feedfishs_2()
		self._collide_fish_shark()
		self._check_availability_fishs()
		self._collide_shark_feedfishs()

	def _feedfish_hit(self):
		"""Обрабатывает столкновения рыбов с краем."""
		"""Handles fish collisions with edges."""
		if self.stats.fishs_left > 0:
			# Уменьшает fishs_left.
			# Reduces fishs_left.
			self.stats.fishs_left -= 1
			self.sb.prep_dead_fish()
			self.loss_sound.play()

			# Очистка списка рыбов.
			# fish removal.
			self.feedfishs.empty()
			self.feedfishs_2.empty()
			self.sharks.empty()

			# Создание новой стаи и размещение рыбы в центре.
			# Creating a new flock and placing the fish in the center.
			self._create_flock_fish()
			self.fish.center_fish()

			# пауза.
			# pause.
			sleep(2)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)	
		
	def _collide_feedfishs(self):
		"""Ищет коллизии рыбов с рыбой."""
		"""Looks for fish-fish collisions"""		
		hits = pygame.sprite.spritecollide(self.fish, self.feedfishs, True)
		if hits:
			self.stats.score += self.settings.feedfish_points
			self.sb.prep_score()
			self.sb.check_high_score()
			self.eat_sound.play()

	def _collide_shark_feedfishs(self):
		"""Ищет коллизии рыбов с акулой для предотвращения наложений."""
		"""Looks for collisions between fish and shark to prevent overlaps."""
		collisions = pygame.sprite.groupcollide(self.sharks, self.feedfishs, False, True)

	def _check_availability_fishs(self):
		if not self.feedfishs:
			self._create_flock_fish()
			# увеличение скорости стаи после того как все рыбы съедены.
			# increasing the speed of the flock after all the fish are eaten.
			self.settings.increase_speed()
			# Увеличение уровня.
			# Level up.
			self.stats.level += 1
			self.stats.level_fish += 1
			self.sb.prep_level()
			if self.stats.level_fish == 3:
				self._create_flock_fish_2()
			if self.stats.level_fish == 5:
				self._create_flock_shark()
				self.stats.level_fish = 1

	def _update_feedfishs_flock(self):
		"""Обновляет позиции рыбов и уничтожает старых рыбов."""
		"""Updates fish positions and destroys old fish."""
		# Update fish positions.
		self.feedfishs.update()
		# Удаление рыбов, вышедших за край экрана.
		# fish collision with edge.
		for feedfish in self.feedfishs.copy():
			if feedfish.rect.left <= 0:
				self._feedfish_hit()

	def _create_flock_fish(self):
		"""Создание стаи кормовых рыб."""
		"""Creating a flock feed-fish."""
		# Создание рыбы и вычисление количества рыб в ряду.
		# Creating fish and calculating the number of fish in a row.
		feedfish = Feedfish(self)
		random_number = randint(1,3)
		feedfish_width, feedfish_height = feedfish.rect.size
		number_feedfishs_x = random_number
		
		"""Определяет количество рядов на экране."""
		"""calculating the number of rows on the screen."""
		number_rows = random_number
		
		# создание рандомной стаи рыб.
		# creating a random flock of fish.
		for row_number in range(number_rows):
			for feedfish_number in range(number_feedfishs_x):
				self._create_feedfish(feedfish_number, row_number)

	def _create_feedfish(self, feedfish_number, row_number):
		# Создание рыбы и размещение её в ряду.
		# Creating fish and placing them in a row.
		feedfish = Feedfish(self)
		random_number1 = randint(1500,1650)
		random_number2 = randint(50,700)
		feedfish_width, feedfish_height = feedfish.rect.size
		feedfish.x = random_number1
		feedfish.y = random_number2
		feedfish.rect.x = random_number1
		feedfish.rect.y = random_number2

		self.feedfishs.add(feedfish)

	def _create_flock_fish_2(self):
		"""Создание стаи кормовых рыб."""
		"""Creating a flock feed-fish."""
		# Создание рыбы и вычисление количества рыб в ряду.
		# Creating fish and calculating the number of fish in a row.
		feedfish_2 = Feedfish_2 (self)
		random_number = randint(1,2)
		feedfish_2_width, feedfish_2_height = feedfish_2.rect.size
		number_feedfish_2_x = random_number
		
		"""Определяет количество рядов на экране."""
		"""calculating the number of rows on the screen."""
		number_rows = random_number
		
		# создание рандомной стаи рыб.
		# creating a random flock of fish.
		for row_number in range(number_rows):
			for feedfish_2_number in range(number_feedfish_2_x):
				self._create_feedfish_2(feedfish_2_number, row_number)

	def _create_feedfish_2(self, feedfish_number, row_number):
		# Создание рыбы и размещение её в ряду.
		# Creating fish and placing them in a row.
		feedfish_2 = Feedfish_2 (self)
		random_number1 = randint(1700,1800)
		random_number2 = randint(50,700)
		feedfish_2_width, feedfish_2_height = feedfish_2.rect.size
		feedfish_2.x = random_number1
		feedfish_2.y = random_number2
		feedfish_2.rect.x = random_number1
		feedfish_2.rect.y = random_number2

		self.feedfishs_2.add(feedfish_2)


	def _collide_feedfishs_2(self):
		"""Ищет коллизии рыбов с рыбой"""
		"""Looks for fish-fish collisions"""		
		hits = pygame.sprite.spritecollide(self.fish, self.feedfishs_2, True)
		if hits:
			self.stats.score += self.settings.feedfish_points
			self.sb.prep_score()
			self.sb.check_high_score()
			self.eat_sound.play()

	def _update_feedfishs_flock_2(self):
		"""Обновляет позиции рыбов и уничтожает старых рыбов."""
		"""Updates fish positions and destroys old fish."""
		# Update fish positions.
		# Обновление позиций рыбов.
		self.feedfishs_2.update()
		# Удаление рыбов, вышедших за край экрана.
		# fish collision with edge.
		for feedfish2 in self.feedfishs_2.copy():
			if feedfish2.rect.left <= 0:
				self._feedfish_hit()

	def _create_flock_shark(self):
		"""Создание flock акул."""
		"""Creating a school of sharks."""
		# Создание акулы и вычисление количества их в ряду.
		# Creating a shark and calculating the number of them in a row.
		shark = Shark(self)
		random_number = randint(1,2)
		shark_width, shark_height = shark.rect.size
		number_sharks_x = random_number
		
		"""Определяет количество рядов на экране."""
		"""Сalculating the number of rows on the screen."""
		number_rows = random_number
		
		# создание рандомной стаи акул.
		# creating a random school of sharks.
		for row_number in range(number_rows):
			for shark_number in range(number_sharks_x):
				self._create_shark(shark_number, row_number)

	def _create_shark(self, shark_number, row_number):
		# Создание акулы и размещение её в ряду.
		# Creating a shark and placing it in a row.
		shark = Shark(self)
		random_number1 = randint(1900,2000)
		random_number2 = randint(50,700)
		shark_width, shark_height = shark.rect.size
		shark.x = random_number1
		shark.y = random_number2
		shark.rect.x = random_number1
		shark.rect.y = random_number2
		self.sharks.add(shark)

		# столкновений - акула/рыба
		# collisions - shark/fish
	def _collide_fish_shark(self):
		if pygame.sprite.spritecollideany(self.fish, self.sharks):
			self._feedfish_hit()

	def _update_shark_flock(self):
		"""Обновляет позиции акул и уничтожает старых."""
		"""Renews shark positions and destroys old ones."""
		# Обновление позиций акул.
		# Shark position update.
		self.sharks.update()
		# Удаление акул, вышедших за край экрана.
		# Removing sharks that go off the edge of the screen.
		for shark in self.sharks.copy():
			if shark.rect.left <= 0:
				self.sharks.empty()
	
	def _update_screen(self):
		"""Обновляет изображение на экране и отображает новый экран"""
		"""Refreshes the screen image and displays a new screen"""
		self.screen.blit(self.background_image, (0, 0))
		self.fish.blitme()
		self.feedfishs.draw(self.screen)
		self.feedfishs_2.draw(self.screen)
		self.sharks.draw(self.screen)
		self.sb.show_score()
		# Кнопка Play отображается если игра не активна.
		# The Play button is displayed if the game is not active.		
		if not self.stats.game_active:
			self.fish_menu.blitme()
		# заставка отображается если игра не активна.
		# The splash screen is displayed if the game is not active.
		if not self.stats.game_active:
			self.play_button.draw_button()
		# Отображение последнего прорисованного экрана.
		# Displays the last drawn screen.
		pygame.display.flip()

if __name__ == '__main__':
	# Создание экземпляра и запуск игры.
	# Creating an instance and running the game
	ai = Hungryfish()
	ai.run_game()