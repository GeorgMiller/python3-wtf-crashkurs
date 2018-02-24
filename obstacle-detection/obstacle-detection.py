import ev3dev.ev3 as ev3


class ObstacleDetection:
    # Define inlets here or on construction
    def __init__(self, ts1=ev3.TouchSensor('in2'), ts2=ev3.TouchSensor('in3')):
        self.ts1 = ts1
        self.ts2 = ts2

    def is_obstacle_in_sight(self):
        return self.ts1.value() == 1 or self.ts2.value() == 1
