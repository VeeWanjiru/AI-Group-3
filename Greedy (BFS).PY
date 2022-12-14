import matplotlib.pyplot as plt
import networkx as nx

bbitb_graph = {
    'Sports Complex': ['Siwaka'],
    'Siwaka': ['Ph.1A', 'Ph.1B'],
    'Ph.1A': ['Mada', 'Ph.1B'],
    'Ph.1B': ['Phase 2', 'STC'],
    'Phase 2': ['Phase 3', 'J1','STC'],
    'Phase 3': ['Parking lot'],
    'J1':['Mada'],
    'Parking lot':['Mada']
}


def show(graph):
    nx_graph = nx.Graph()

    for node in graph:
        for neighbour in graph[node]:
            nx_graph.add_edge(node, neighbour, color="black")

    x = nx.spring_layout(nx_graph)
    colors = [nx_graph[u][v]['color'] for u, v in nx_graph.edges()]
    nx.draw(nx_graph, x, node_color="#ADD8E6", edge_color=colors, width=2, with_labels=True)
    plt.show()


show(bbitb_graph)


from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

# Function For Implementing Best First Search
# Gives output path having lowest cost


def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
    
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()

# Function for adding edges to graph


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# The nodes shown in the graph(by alphabets) are
# implemented using integers addedge(x,y,cost);
addedge(0, 0,730)
addedge(0, 1,405)
addedge(1, 2, 380)
addedge(2, 3,280)
addedge(1, 3, 280)
addedge(3, 4, 213)
addedge(4, 5, 210)
addedge(3, 5, 210)
addedge(5, 6, 160)
addedge(6, 7, 0)
addedge(7, 8, 630)
addedge(8, 2, 380)
addedge(8, 9, 500)
addedge(9, 5, 210)


source = 0
target = 7
best_first_search(source, target, v)



