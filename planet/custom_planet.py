#!/usr/bin/env python3
import unittest

from planet import Planet, Coordinate, Path


class PlanetTestCase(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(Coordinate(0, 0, "S"))


class FirstPlanet(PlanetTestCase):
    """

    +-------------+        |   +-----------------+
    |             |        |   |                 |
    |      (1,6)  |        +-(3,6)-------------(5,6)-----(6,6)
    |        +----+   +--------+                 |
    |                 |                          |         +-----+
  (0,5)----(1,5)----(2,5)------+  +--(4,5)-----(5,5)-----(6,5)---+
----+        |                 |  |    |         |         |
             |                 |  |    |         |         |
    +------(1,4)      +------(3,4)+  (4,4)-----(5,4)       |
    |                 |        +-------↰         |         |
    |                 |                |         |         |
  (0,3)-+       +---(2,3) +--(3,3)     |     +-(5,3)-+     |
    |   |       |         |    |       |     |   |   |     |
    |   |       +---------+    |       |     |   |   |     |
    |   +--(1,2)               +-----(4,2)   +-(5,2)-+     |
    |        |                         |         |         |
    |        |                         |         |         |
    +------(1,1)------+              (4,1)-----(5,1)-----(6,1)----
             |        |                          |
    ↓        |        |                          |
  (0,0)----(1,0)    (2,0)                      (5,0)
    |        |        |                          |
    +--------+        +--------------------------+

     """

    def test_shortest_path(self):
        self.planet.add_path(Path(Coordinate(1,1,"E"),Coordinate(2,0,"N")))
        self.planet.add_path(Path(Coordinate(2,0,"S"),Coordinate(5,0,"S")))
        self.planet.add_path(Path(Coordinate(4,1,"E"),Coordinate(5,1,"W")))
        self.planet.add_path(Path(Coordinate(5,0,"N"),Coordinate(5,1,"S")))
        self.planet.add_path(Path(Coordinate(5,1,"E"),Coordinate(6,1,"W")))
        self.planet.add_path(Path(Coordinate(6,1,"E"),Coordinate(6,1,"E")))
        self.planet.add_path(Path(Coordinate(1,1,"W"),Coordinate(0,3,"S")))
        self.planet.add_path(Path(Coordinate(1,2,"S"),Coordinate(1,1,"N")))
        self.planet.add_path(Path(Coordinate(4,1,"N"),Coordinate(4,2,"S")))
        self.planet.add_path(Path(Coordinate(5,1,"N"),Coordinate(5,2,"S")))
        self.planet.add_path(Path(Coordinate(6,1,"N"),Coordinate(6,5,"S")))
        self.planet.add_path(Path(Coordinate(1,2,"W"),Coordinate(0,3,"E")))
        self.planet.add_path(Path(Coordinate(2,3,"W"),Coordinate(3,3,"W")))
        self.planet.add_path(Path(Coordinate(3,3,"S"),Coordinate(4,2,"W")))
        self.planet.add_path(Path(Coordinate(3,4,"S"),Coordinate(4,2,"N")))
        self.planet.add_path(Path(Coordinate(5,2,"W"),Coordinate(5,3,"W")))
        self.planet.add_path(Path(Coordinate(5,2,"N"),Coordinate(5,3,"S")))
        self.planet.add_path(Path(Coordinate(5,2,"E"),Coordinate(5,3,"E")))
        self.planet.add_path(Path(Coordinate(0,3,"N"),Coordinate(1,4,"W")))
        self.planet.add_path(Path(Coordinate(1,4,"N"),Coordinate(1,5,"S")))
        self.planet.add_path(Path(Coordinate(2,3,"N"),Coordinate(3,4,"W")))
        self.planet.add_path(Path(Coordinate(4,4,"E"),Coordinate(5,4,"W")))
        self.planet.add_path(Path(Coordinate(0,5,"S"),Coordinate(0,5,"S")))
        self.planet.add_path(Path(Coordinate(0,5,"E"),Coordinate(1,5,"W")))
        self.planet.add_path(Path(Coordinate(1,5,"E"),Coordinate(2,5,"W")))
        self.planet.add_path(Path(Coordinate(2,5,"E"),Coordinate(3,4,"N")))
        self.planet.add_path(Path(Coordinate(3,4,"E"),Coordinate(4,5,"W")))
        self.planet.add_path(Path(Coordinate(4,4,"N"),Coordinate(4,5,"S")))
        self.planet.add_path(Path(Coordinate(4,5,"E"),Coordinate(5,5,"W")))
        self.planet.add_path(Path(Coordinate(5,4,"N"),Coordinate(5,5,"S")))
        self.planet.add_path(Path(Coordinate(5,4,"S"),Coordinate(5,3,"N")))
        self.planet.add_path(Path(Coordinate(5,5,"E"),Coordinate(6,5,"W")))
        self.planet.add_path(Path(Coordinate(6,5,"E"),Coordinate(6,5,"N")))
        self.planet.add_path(Path(Coordinate(0,5,"N"),Coordinate(1,6,"S")))
        self.planet.add_path(Path(Coordinate(2,5,"N"),Coordinate(3,6,"S")))
        self.planet.add_path(Path(Coordinate(5,6,"S"),Coordinate(5,5,"N")))
        self.planet.add_path(Path(Coordinate(3,6,"E"),Coordinate(5,6,"W")))
        self.planet.add_path(Path(Coordinate(3,6,"W"),Coordinate(3,6,"W")))
        self.planet.add_path(Path(Coordinate(3,6,"N"),Coordinate(5,6,"N")))
        self.planet.add_path(Path(Coordinate(5,6,"E"),Coordinate(6,6,"W")))


if __name__ == "__main__":
    unittest.main()
