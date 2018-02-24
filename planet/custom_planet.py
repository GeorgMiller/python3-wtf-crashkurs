#!/usr/bin/env python3
import unittest

from pathfinding.graph import Graph


class PlanetTestCase(unittest.TestCase):
    def setUp(self):
        # Do everything to set up the test
        pass


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
        graph = Graph()
        graph.add_binary_edge(from_node=(1, 1), in_vector=0, to_node=(2, 0), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(2, 0), in_vector=270, to_node=(5, 0), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(4, 1), in_vector=0, to_node=(5, 1), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(5, 0), in_vector=90, to_node=(5, 1), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(5, 1), in_vector=0, to_node=(6, 1), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(6, 1), in_vector=0, to_node=(6, 1), out_vector=0, distance=10)
        graph.add_binary_edge(from_node=(1, 1), in_vector=180, to_node=(0, 3), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(1, 2), in_vector=270, to_node=(1, 1), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(4, 1), in_vector=90, to_node=(4, 2), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(5, 1), in_vector=90, to_node=(5, 2), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(6, 1), in_vector=90, to_node=(6, 5), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(1, 2), in_vector=180, to_node=(0, 3), out_vector=0, distance=10)
        graph.add_binary_edge(from_node=(2, 3), in_vector=180, to_node=(3, 3), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(3, 3), in_vector=270, to_node=(4, 2), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(3, 4), in_vector=270, to_node=(4, 2), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(5, 2), in_vector=180, to_node=(5, 3), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(5, 2), in_vector=90, to_node=(5, 3), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(5, 2), in_vector=0, to_node=(5, 3), out_vector=0, distance=10)
        graph.add_binary_edge(from_node=(0, 3), in_vector=90, to_node=(1, 4), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(1, 4), in_vector=90, to_node=(1, 5), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(2, 3), in_vector=90, to_node=(3, 4), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(4, 4), in_vector=0, to_node=(5, 4), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(0, 5), in_vector=270, to_node=(0, 5), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(0, 5), in_vector=0, to_node=(1, 5), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(1, 5), in_vector=0, to_node=(2, 5), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(2, 5), in_vector=0, to_node=(3, 4), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(3, 4), in_vector=0, to_node=(4, 5), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(4, 4), in_vector=90, to_node=(4, 5), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(4, 5), in_vector=0, to_node=(5, 5), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(5, 4), in_vector=90, to_node=(5, 5), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(5, 4), in_vector=270, to_node=(5, 3), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(5, 5), in_vector=0, to_node=(6, 5), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(6, 5), in_vector=0, to_node=(6, 5), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(0, 5), in_vector=90, to_node=(1, 6), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(2, 5), in_vector=90, to_node=(3, 6), out_vector=270, distance=10)
        graph.add_binary_edge(from_node=(5, 6), in_vector=270, to_node=(5, 5), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(3, 6), in_vector=0, to_node=(5, 6), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(3, 6), in_vector=180, to_node=(3, 6), out_vector=180, distance=10)
        graph.add_binary_edge(from_node=(3, 6), in_vector=90, to_node=(5, 6), out_vector=90, distance=10)
        graph.add_binary_edge(from_node=(5, 6), in_vector=0, to_node=(6, 6), out_vector=180, distance=10)

        p, in_dir, out_dir, dist = graph.dijkstra((1, 1), (5, 5))

        print("Um vom Punkt (1,1) nach Punkt (5,5) zu gelangen, müssen wir folgenden Weg gehen: {}".format(p))
        print("Wir müssen dabei die Kreuzungen in folgenden Richtungen befahren: {}".format(in_dir))
        print("... und in folgenden Richtungen verlassen: {}".format(out_dir))
        print("Die Distanz zwischen den beiden Punkten beträgt dabei {}.".format(dist))


if __name__ == "__main__":
    unittest.main()
