import numpy as np
import heapq
import queue

def dijkstra(graph, start, end):
    rows, cols = graph.shape
    distances = np.full((rows, cols), np.inf)
    distances[start] = 0

    # Priority queue to store vertices with their distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == end:
            break

        # Explore neighbors
        for neighbor in get_neighbors(graph, current_vertex):
            distance = current_distance + graph[current_vertex[0]][current_vertex[1]]
            if distance < distances[neighbor[0]][neighbor[1]]:
                distances[neighbor[0]][neighbor[1]] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the path
    path = []
    current_vertex = end
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = np.unravel_index(np.argmin(distances), distances.shape)
    path.append(start)

    return path[::-1]

def get_neighbors(graph, vertex):
    rows, cols = graph.shape
    neighbors = []
    r, c = vertex

    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))

    return neighbors

# Example usage
graph = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

start_point = (0, 0)
end_point = (2, 3)

shortest_path = dijkstra(graph, start_point, end_point)
print("Shortest path:", shortest_path)

frontier = queue.PriorityQueue()
frontier.put((0,0))
