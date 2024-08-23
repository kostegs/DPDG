import pygame, sys
from settings import Settings
from orb import Orb


class DPDG:
    """Main class"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("DPDG")
        self.bg_color = self.settings.bg_color
        self.orb = Orb(self.screen, self.settings)

    def run(self):
        """Main loop"""
        while True:
            self.check_events()
            self.orb.update()
            self.update_screen()
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.orb.draw()

    def move_orb(self):
        self.orb.move()

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.orb.change_speed(1)
        elif event.key == pygame.K_DOWN:
            self.orb.change_speed(-1)
        elif event.key == pygame.K_q:
            sys.exit()


if __name__ == "__main__":
    dpdg = DPDG()
    dpdg.run()
