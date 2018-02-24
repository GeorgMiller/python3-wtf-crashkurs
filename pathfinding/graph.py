# Adapted from http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_edge(self, from_node, to_node, distance, out_vector, in_vector):
        if from_node in self.graph_dict:
            self.graph_dict[from_node][to_node] = {"out": out_vector, "in": in_vector, "d": distance}
        else:
            self.graph_dict[from_node] = {to_node: {"out": out_vector, "in": in_vector, "d": distance}}

    def add_binary_edge(self, from_node, to_node, distance, out_vector, in_vector):
        self.add_edge(from_node, to_node, distance, out_vector, in_vector)
        self.add_edge(to_node, from_node, distance, in_vector, out_vector)

    def dijkstra(self, src, dest, visited=[], distances={}, predecessors={}):
        if visited is None:
            visited = []
        if src not in self.graph_dict:
            raise TypeError("The root of the shortest path tree cannot be found")
        if dest not in self.graph_dict:
            raise TypeError("The target of the shortest path cannot be found")
        if src == dest:
            path = []
            pred = dest
            while pred is not None:
                path.append(pred)
                pred = predecessors.get(pred, None)
            in_directions = []
            out_directions = []
            if path:
                for i in range(len(path) - 1):
                    in_directions.append(self.graph_dict[path[i]][path[i + 1]]["in"])
                    out_directions.append(self.graph_dict[path[i]][path[i + 1]]["out"])
            return path, in_directions, out_directions, distances[dest]
        else:
            if not visited:
                distances[src] = 0
            for neighbor in self.graph_dict[src]:
                if neighbor not in visited:
                    new_distance = distances[src] + self.graph_dict[src][neighbor]["d"]
                    if new_distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = src
            visited.append(src)
            unvisited = {}
            for k in self.graph_dict:
                if k not in visited:
                    unvisited[k] = distances.get(k, float('inf'))
            new_source = min(unvisited, key=unvisited.get)
            return self.dijkstra(new_source, dest, visited, distances, predecessors)


if __name__ == "__main__":
    graph = Graph()

    graph.add_binary_edge("s", "a", 1, 90, 0)
    graph.add_binary_edge("a", "b", 2, 270, 180)

    p, in_dir, out_dir, dist = graph.dijkstra("s", "b")

    print("Um vom Punkt s nach Punkt b zu gelangen, müssen wir folgenden Weg gehen: {}".format(p))
    print("Wir müssen dabei die Kreuzungen in folgenden Richtungen befahren: {}".format(in_dir))
    print("... und in folgenden Richtungen verlassen: {}".format(out_dir))
    print("Die Distanz zwischen den beiden Punkten beträgt dabei {}.".format(dist))
