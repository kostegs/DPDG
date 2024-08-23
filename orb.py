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
        self.orb_speed = self.settings.orb_speed

        self.x = float(self.rect.x)
        self.moving_right = True
        self.moving_left = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):

        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.x += self.orb_speed
            else:
                self.change_direction()
        if self.moving_left:
            if self.rect.left > 0:
                self.x -= self.orb_speed
            else:
                self.change_direction()

        self.rect.x = self.x

    def change_direction(self):
        self.moving_right = not self.moving_right
        self.moving_left = not self.moving_left

    def update(self):
        self.move()
        self.draw()

    def change_speed(self, coefficient):
        self.orb_speed += (coefficient * self.settings.orb_speed_step)

