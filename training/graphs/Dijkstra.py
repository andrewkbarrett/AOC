"""
https://datagy.io/dijkstras-algorithm-python/
In order to implement Dijkstra’s Algorithm, we’ll want to keep track of a number of different pieces. In particular, we’ll need to track:

    1.The currently known shortest distances from node A to any node,
    2.Which nodes we have visited so far
    3.Which previous node (or vertex) resulted in the shortest path

"""

import heapq

# Converting our graph to an edge list
#edge_list = [('A', 'B', 3), ('A', 'C', 8), ('B', 'C', 2), ('B', 'E', 5), ('C', 'D', 1), ('C', 'E', 6), ('D', 'E', 2), ('D', 'F', 3), ('E', 'F', 5)]
edge_list = [('A','B',1), ('A','C',2),('B','D',1),('C','D',3)]
# Converting our graph to an adjacency list
def edge_list_to_adjacency_list(edge_list):
    adj_list = {}
    for (src, dest, weight) in edge_list:
        if src not in adj_list:
            adj_list[src] = {}
        if dest not in adj_list:
            adj_list[dest] = {}
        
        adj_list[src][dest] = weight
        adj_list[dest][src] = weight

    return dict(sorted(adj_list.items()))#adj_list #dict(sorted(people.items()))



def dijkstra(adj_list, start):
    cntr = 0 
    distances = {node: float('inf') for node in adj_list}
    distances[start] = 0
    print(distances)
    # Priority queue to track nodes and current shortest distance
    priority_queue = [(0, start)]

    while priority_queue:
        print(f'into run {cntr}')
        print(priority_queue)
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)
        #print(f"curr dist = {current_distance} and cur node = {current_node}")
        
        # Skip if a shorter distance to current_node is already found
        if current_distance > distances[current_node]:
            #print(f"skipped {current_node}")
            continue

        # Explore neighbors and update distances if a shorter path is found
        for neighbor, weight in adj_list[current_node].items():
            distance = current_distance + weight
            #print(f"neighbor check for {current_node}")
            #print(f"checking {neighbor} with a weight of {weight} and node distance of {distance}")
            
            # If shorter path to neighbor is found, update distance and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                #print(f" {current_node} -> {neighbor} with {distances[neighbor]}")
                
                heapq.heappush(priority_queue, (distance, neighbor))
        
        cntr +=1 
    
    return distances

adj_list = edge_list_to_adjacency_list(edge_list)
print(adj_list)
d_set = dijkstra(adj_list,"A")
print(d_set)