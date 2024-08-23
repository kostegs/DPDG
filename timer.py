import time
import pygame


class Timer:

    def __init__(self, screen):
        self.start_time = time.time()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('comicsans', 20)
        self.rect = pygame.Rect(0, 0, 200, 50)
        self.rect.topleft = self.screen_rect.topleft
        self.minutes_left = 0
        pygame.font.init()

    def draw(self):
        elapsed_seconds = time.time() - self.start_time

        text_elapsed_seconds = self.get_text_elapsed_seconds(elapsed_seconds)
        text_surface = self.font.render(text_elapsed_seconds, True, self.text_color)
        self.screen.blit(text_surface, self.rect)

    def get_text_elapsed_seconds(self, elapsed_seconds):
        if elapsed_seconds >= 60:
            self.minutes_left += 1
            self.start_time = time.time()
            elapsed_seconds = 0

        if self.minutes_left == 0:
            return self.add_lead_zero(elapsed_seconds)
        else:
            return f'{self.minutes_left} : ' + self.add_lead_zero(elapsed_seconds)

    def add_lead_zero(self, number):
        if number < 10:
            return f'0{int(number)}'
        else:
            return f'{int(number)}'

