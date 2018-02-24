import ev3dev.ev3 as ev3
import sys
import time

try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class KeyboardControl:
    def __init__(self, motor_right=ev3.LargeMotor("outA"), motor_left=ev3.LargeMotor("outD")):
        # Define motor outlets here
        self.motor_right = motor_right
        self.motor_right.stop_action = "brake"
        self.motor_left = motor_left
        self.motor_left.stop_action = "brake"

    def control(self):
        while True:
            if getch() == "q":
                break
            if getch() == "d":
                self.motor_left.run_timed(time_sp=2000, speed_sp=200)
                self.motor_right.run_timed(time_sp=2000, speed_sp=-200)
            if getch() == "a":
                self.motor_left.run_timed(time_sp=2000, speed_sp=-360)
                self.motor_right.run_timed(time_sp=2000, speed_sp=360)
            if getch() == "s":
                self.motor_left.run_timed(time_sp=2000, speed_sp=-200)
                self.motor_right.run_timed(time_sp=2000, speed_sp=-200)
            if getch() == "w":
                self.motor_left.run_timed(time_sp=2000, speed_sp=200)
                self.motor_right.run_timed(time_sp=2000, speed_sp=200)
            if getch() == "e":
                self.motor_left.stop()
                self.motor_right.stop()
            if getch() == "y":
                self.motor_left.run_timed(time_sp=2000, speed_sp=-30)
                self.motor_right.run_timed(time_sp=2000, speed_sp=30)
            if getch() == "x":
                self.motor_left.run_timed(time_sp=2000, speed_sp=30)
                self.motor_right.run_timed(time_sp=2000, speed_sp=-30)


if __name__ == "__main__":
    keyboard = KeyboardControl()
    keyboard.control()
