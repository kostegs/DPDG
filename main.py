import pygame, sys
from settings import Settings


class DPDG:
    """Main class"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("DPDG")
        self.bg_color = self.settings.bg_color

    def run(self):
        """Main loop"""
        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.bg_color)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            pass
        elif event.key == pygame.K_DOWN:
            pass
        elif event.key == pygame.K_q:
            sys.exit()


if __name__ == "__main__":
    dpdg = DPDG()
    dpdg.run()