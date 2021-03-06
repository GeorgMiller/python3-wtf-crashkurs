import ev3dev.ev3 as ev3


# ( (Hz), duration (ms), delay to next (ms)

class Sound:
    
    @staticmethod
    def play_star_wars():
        ev3.Sound.tone([
            (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
            (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
            (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
            (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
            (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
            (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
            (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
            (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100),
            (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
            (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
            (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100),
            (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100),
            (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
            (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
            (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
            (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200),
            (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
            (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
            ])

    # Play a receive tone
    @staticmethod
    def receive_beep():
        ev3.Sound.tone([(466, 25, 100)])

    # Play a lost tone
    @staticmethod
    def unanswered_beep():
        ev3.Sound.tone([(50, 250, 100)])

    @staticmethod
    # Play an error tone
    def error_beep():
        ev3.Sound.tone([(50, 250, 1000), (50, 250, 1000)])
    
    @staticmethod
    def play_mario_theme():
        ev3.Sound.tone(
            [
             (660, 100, 150), (660, 100, 300), (660, 100, 300), (510, 100, 100), (660, 100, 300), (770, 100, 550),
             (380, 100, 575), (510, 30, 450), (380, 30, 400), (320, 30, 500), (440, 30, 300), (480, 80, 330),
             (450, 30, 150), (430, 30, 300), (380, 30, 200), (660, 80, 200), (760, 50, 150), (860, 30, 300),
             (700, 80, 150), (760, 50, 350), (660, 80, 300), (520, 80, 150), (580, 80, 150), (480, 80, 500),
             (510, 30, 450), (380, 30, 400), (320, 30, 500), (440, 30, 300), (480, 80, 330), (450, 30, 150),
             (430, 30, 300), (380, 30, 200), (660, 80, 200), (760, 50, 150), (860, 30, 300), (700, 80, 150),
             (760, 50, 350), (660, 80, 300), (520, 80, 150), (580, 80, 150), (480, 80, 500), (500, 30, 300),
             (760, 30, 100), (720, 30, 150), (680, 30, 150), (620, 40, 300), (650, 40, 300), (380, 30, 150),
             (430, 30, 150), (500, 30, 300), (430, 30, 150), (500, 30, 100), (570, 30, 220), (500, 30, 300),
             (760, 30, 100), (720, 30, 150), (680, 30, 150), (620, 40, 300), (650, 20, 300), (102, 20, 300),
             (102, 20, 150), (102, 20, 300), (380, 30, 300), (500, 30, 300), (760, 30, 100), (720, 30, 150),
             (680, 30, 150), (620, 40, 300), (650, 40, 300), (380, 30, 150), (430, 30, 150), (500, 30, 300),
             (430, 30, 150), (500, 30, 100), (570, 30, 420), (585, 30, 450), (550, 30, 420), (500, 30, 360),
             (380, 30, 300), (500, 30, 300), (500, 30, 150), (500, 30, 300), (500, 30, 300), (760, 30, 100),
             (720, 30, 150), (680, 30, 150), (620, 40, 300), (650, 40, 300), (380, 30, 150), (430, 30, 150),
             (500, 30, 300), (430, 30, 150), (500, 30, 100), (570, 30, 220), (500, 30, 300), (760, 30, 100),
             (720, 30, 150), (680, 30, 150), (620, 40, 300), (650, 20, 300), (102, 20, 300), (102, 20, 150),
             (102, 20, 300), (380, 30, 300), (500, 30, 300), (760, 30, 100), (720, 30, 150), (680, 30, 150),
             (620, 40, 300), (650, 40, 300), (380, 30, 150), (430, 30, 150), (500, 30, 300), (430, 30, 150),
             (500, 30, 100), (570, 30, 420), (585, 30, 450), (550, 30, 420), (500, 30, 360), (380, 30, 300),
             (500, 30, 300), (500, 30, 150), (500, 30, 300), (500, 60, 150), (500, 80, 300), (500, 60, 350),
             (500, 80, 150), (580, 80, 350), (660, 80, 150), (500, 80, 300), (430, 80, 150), (380, 80, 600),
             (500, 60, 150), (500, 80, 300), (500, 60, 350), (500, 80, 150), (580, 80, 150), (660, 80, 550),
             (870, 80, 325), (760, 80, 600), (500, 60, 150), (500, 80, 300), (500, 60, 350), (500, 80, 150),
             (580, 80, 350), (660, 80, 150), (500, 80, 300), (430, 80, 150), (380, 80, 600), (660, 30, 150),
             (660, 30, 300), (660, 30, 300), (510, 30, 100), (660, 30, 300), (770, 30, 550), (380, 30, 575),
            ]
        )

        
if __name__ == "__main__":
    Sound.play_mario_theme()
