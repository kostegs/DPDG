import pygame


class Orb:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.image = pygame.image.load('images/orb.png')
        # image size for future use
        # self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.orb_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.orb_speed
        self.rect.x = self.x


