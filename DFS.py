def dfs(visited, graph, node, goal, poped):
    if goal not in visited:
        if node not in visited:
            visited.append(node)

            if graph[node] == [] and node != goal:
                poped.append(node)
                visited.pop()

            for visit in visited:
                if graph[visit] == poped and poped != []:
                    poped.clear()
                    visited.pop()

            for neighbour in graph[node]:
                    dfs(visited, graph, neighbour, goal,poped)

        return visited
    else:
        return visited


graphs = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
visit = dfs([], graphs, 'A', 'F', [])
print(visit)

