from math import inf as infinity

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.distance = infinity

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_bounds(x, x_len, y, y_len):
    return x >= 0 and y >= 0 and x < x_len and y < y_len


def build_graph(elev, start, end):
    graph = elev.copy()

    for y in range(len(graph)):
        for x in range(len(graph[0])):
            graph[y][x] = Node(graph[y][x])

    
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            node = graph[y][x]
            options = [(x + dx, y + dy) for (dx, dy) in directions]

            for point in filter(lambda xy: in_bounds(xy[0], len(elev[0]), xy[1], len(elev)), options):
                neighbour = graph[point[1]][point[0]]
                
                if (neighbour.value - 1) <= node.value:
                    node.neighbours.append(graph[point[1]][point[0]])

    graph[start[1]][start[0]].distance = 0

    return (graph[end[1]][end[0]], set(node for row in graph for node in row))

def solution(elev):
    for y in range(len(elev)):
        try:
            x = elev[y].index(-14)
            start = (x, y)
            break
        except ValueError:
            continue

    for y in range(len(elev)):
        try:
            x = elev[y].index(-28)
            end = (x, y)
            break
        except ValueError:
            continue
    
    elev[start[1]][start[0]] = 0
    elev[end[1]][end[0]] = 25

    end, unvisited = build_graph(elev, start, end)

    # Dijkstra, where every edge has a length of 1
    while unvisited:
        smallest = min(unvisited, key=lambda n: n.distance)

        for neighbour in filter(lambda n: n in unvisited, smallest.neighbours):
            next_distance = smallest.distance + 1

            if neighbour.distance > next_distance:
                neighbour.distance = next_distance

        unvisited.remove(smallest)

    return end.distance