class Settings:
    """Settings class"""

    def __init__(self):
        self.screen_width = 2560
        self.screen_height = 1440
        self.bg_color = (30, 31, 34)
        self.orb_speed = 1.2
        self.orb_speed_step = 0.1
        self.session_duration = 90_000  # in milliseconds (1.5 minutes), how long the session lasts
