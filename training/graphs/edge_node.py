##representing edges and nodes
##From a technical perspective, these circles are referred to as nodes. Similarly, the lines connecting them are called edges
#edge lists are often represented as lists of tuples. 
edges = [("a","b"),("b","c"),("c","d"),("a","d")]

nodes = ("a","b","c","d")

#directed/undirected graphs

#Adjancency matrix. 

##Adjacency matrices are often represented as lists of lists, where each list represents a node. 
# The list’s items represent whether an edge exists between the node and another node.

[[0, 1, 0, 0, 0, 0],
 [1, 0, 1, 1, 0, 0],
 [0, 1, 0, 0, 1, 0],
 [0, 1, 0, 0, 1, 0],
 [0, 0, 1, 1, 0, 1],
 [0, 0, 0, 0, 1, 0]]

# A sample adjacency list
{
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D', 'F'],
    'F': ['E']
}


edge_list = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('E', 'F')]

# Being explicit in undirect relationships
undirected = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), ('B', 'D'), ('D', 'B'), ('C', 'E'), ('E', 'C'), 
            ('D', 'E'), ('E', 'D'), ('E', 'F'), ('F', 'E')]

#sets - A set is an unordered collection with no duplicate elements. 

# Creating an adjacency matrix in Python
def edge_list_to_adjacency_matrix(edge_list, directed=False):
    nodes = set()
    for edge in edge_list:
        nodes.add(edge[0])
        nodes.add(edge[1])
        print(nodes)
    #print(f'nodes pre-sorted {nodes}')
    nodes = sorted(list(nodes))
    #print(f'nodes sorted {nodes}')
    num_nodes = len(nodes)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for edge in edge_list:
        index_1 = nodes.index(edge[0])
        index_2 = nodes.index(edge[1])
        adjacency_matrix[index_1][index_2] = 1
        if not directed:
            adjacency_matrix[index_2][index_1] = 1

    return adjacency_matrix

#print(edge_list_to_adjacency_matrix(edge_list,False))

# Defining a function to create an adjacency list
def edge_list_to_adjacency_list(edge_list, directed=False):
    adjacency_list = {}
    
    for edge in edge_list:
        node_1, node_2 = edge
        
        if node_1 not in adjacency_list:
            adjacency_list[node_1] = []
        adjacency_list[node_1].append(node_2)

        if not directed:
            if node_2 not in adjacency_list:
                adjacency_list[node_2] = []
            adjacency_list[node_2].append(node_1)

    return adjacency_list

#print(edge_list_to_adjacency_list(edge_list,True))


# Creating a function to convert a weighted edge list into an adjacency matrix
def edge_list_to_adjacency_matrix(edge_list, directed=False, weighted=False):
    nodes = set()
    for edge in edge_list:
        nodes.add(edge[0])
        nodes.add(edge[1])

    nodes = sorted(list(nodes))
    num_nodes = len(nodes)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for edge in edge_list:
        index_1 = nodes.index(edge[0])
        index_2 = nodes.index(edge[1])
        weight = edge[2] if weighted else 1
        adjacency_matrix[index_1][index_2] = weight
        if not directed:
            adjacency_matrix[index_2][index_1] = weight

    return adjacency_matrix

weighted = [('A', 'B', 2), ('B', 'C', 1), ('B', 'D', 3), ('C', 'E', 4), ('D', 'E', 1), ('E', 'F', 2)]
adj_matrix = edge_list_to_adjacency_matrix(weighted, directed=True, weighted=True)
#print(adj_matrix)


# Creating an adjacency list from an edge list
def edge_list_to_adjacency_list(edge_list, directed=False, weighted=False):
    adjacency_list = {}
    
    for edge in edge_list:
        node_1 = edge[0]
        node_2 = edge[1]
        if weighted:
            weight = edge[2]
        
        if node_1 not in adjacency_list:
            adjacency_list[node_1] = []
        if weighted:
            adjacency_list[node_1].append((node_2, weight))
        else:
            adjacency_list[node_1].append(node_2)

        if not directed:
            if node_2 not in adjacency_list:
                adjacency_list[node_2] = []
            if weighted:
                adjacency_list[node_2].append((node_1, weight))
            else:
                adjacency_list[node_2].append(node_1)

    return adjacency_list

adj_list = edge_list_to_adjacency_list(weighted, directed=True, weighted=True)
print(adj_list)