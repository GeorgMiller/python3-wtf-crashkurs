import math

import ev3dev.ev3 as ev3
from planet import Coordinate


class Odometry:
    def __init__(self, coordinate):
        self.heading = 0
        self.esf = 0.047865151  # This value is empirical. (Encoder Scale Factor)
        self.w_seperation = 10  # This value is empirical. (Wheel seperation)
        self.grid = 40  # Grid value for rounding purposes
        
        self.pos_y = coordinate.y * self.grid  # Position y in cm
        self.pos_x = coordinate.x * self.grid  # Position x in cm
        
        self.l_motor.position = 0  # Resetting motor position (left)
        self.r_motor.position = 0  # Resetting motor position (right)
        
        self.l_motor_x = 0  # Calculation variable
        self.r_motor_x = 0  # Calculation variable
        
        self.compass = coordinate.orientation

    def set_position(self, coordinate):
        self.pos_x = coordinate.x * self.grid
        self.pos_y = coordinate.y * self.grid

    def locate(self, l_motor=ev3.LargeMotor("outD"), r_motor=ev3.LargeMotor("outA")):
        l_motor_delta = l_motor.position - self.l_motor_x  # Calc. of wheel movement (left)
        r_motor_delta = r_motor.position - self.r_motor_x  # Calc. of wheel movement (right)
        
        # Calc. of wheel displacement
        displacement = (l_motor_delta + r_motor_delta) * self.esf / 2  
        
        # Calc. of rotation
        rot_calc = (l_motor_delta - r_motor_delta) * self.esf / self.w_seperation  
        
        # Reassigning motor_x for next calculation
        self.l_motor_x = l_motor.position  
        self.r_motor_x = r_motor.position
        
        self.pos_x = self.pos_x + displacement * math.sin(self.heading + rot_calc / 2)  # Calc. of Position (x)
        self.pos_y = self.pos_y + displacement * math.cos(self.heading + rot_calc / 2)  # Calc. of Position (y)
        
        self.heading = self.heading + rot_calc
        
        return self.heading, self.pos_x, self.pos_y
