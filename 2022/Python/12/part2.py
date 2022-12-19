from part1 import Node, directions, in_bounds
from itertools import tee

def build_graph(elev, end):
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
                
                # changed this condition to reverse every node direction
                if neighbour.value >= node.value - 1:
                    node.neighbours.append(graph[point[1]][point[0]])
    
    graph[end[1]][end[0]].distance = 0

    return ((node for row in graph for node in row))

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

    nodes = build_graph(elev, end)

    nodes, unvisited = tee(nodes)
    unvisited = set(unvisited)

    # Dijkstra, where every edge has a length of 1, starting at end
    while unvisited:
        smallest = min(unvisited, key=lambda n: n.distance)

        for neighbour in filter(lambda n: n in unvisited, smallest.neighbours):
            next_distance = smallest.distance + 1

            if neighbour.distance > next_distance:
                neighbour.distance = next_distance

        unvisited.remove(smallest)
    
    return min(filter(lambda n: n.value == 0, nodes), key=lambda n: n.distance).distance