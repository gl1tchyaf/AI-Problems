def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]

    if goal == start:
        return "Goal is at the start"

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path

            explored.append(node)
    return "There is no connecting path found"


graph = {'A': ['B', 'C', 'E'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'], 'D': ['B'], 'E': ['A', 'B', 'D'], 'F': ['C'],
         'G': ['C']}

print(bfs_shortest_path(graph, 'G', 'D'))
