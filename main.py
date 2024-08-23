import pygame, sys, time
from settings import Settings
from orb import Orb
from timer import Timer

EVENT_SESSION_END = 1

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
        self.Clock = pygame.time.Clock()
        self.session_duration = self.settings.session_duration
        self.timer = Timer(self.screen)

        event_session_end = pygame.event.Event(pygame.USEREVENT, EventType=EVENT_SESSION_END)
        pygame.time.set_timer(event_session_end, self.settings.session_duration)

    def run(self):
        """Main loop"""
        while True:
            self.check_events()
            delta_time = self.Clock.tick()
            self.orb.update(delta_time)
            self.update_screen()
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.USEREVENT:
                if event.EventType == EVENT_SESSION_END:
                    sys.exit()

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.orb.draw()
        self.timer.draw()

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
