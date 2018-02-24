import ev3dev.ev3 as ev3


class ObstacleDetection:
    def __init__(self):
        # Define inlets here
        self.ts1 = ev3.TouchSensor('in2')
        self.ts2 = ev3.TouchSensor('in3')

    def is_obstacle_in_sight(self):
        return self.ts1.value() == 1 or self.ts2.value() == 1
