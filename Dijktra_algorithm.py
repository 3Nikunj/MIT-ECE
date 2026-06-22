import heapq

def dijktra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessor = {node: None for node in graph}

    pq = [(0, start)]
    while pq:
        cur_dis, cur_node = heapq.heappop(pq)

        if cur_dis > distances[cur_node]:
            continue

        for neighbour, weight in graph[cur_node].items():
            distance = cur_dis + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance 
                predecessor[neighbour] = cur_node
                heapq.heappush(pq, (distance, neighbour))
    return distances, predecessor



graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2},  # => [('A', 1), ('C', 2)]
    'C': {'A': 4, 'B': 2},
}
shortest_path, predecessor = dijktra(graph, 'A')
print(shortest_path)
print(predecessor)