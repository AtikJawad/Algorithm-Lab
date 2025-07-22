class Graph:
    def __init__(self, num_vertices): #constructor
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def addEdge1(self, u, v):
        # Unweighted Undirected
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def addEdge2(self, u, v, weight):
        # Weighted Directed
        self.adj_list[u].append((v, weight))

    def addEdge3(self, u, v, weight):
        # Weighted Undirected
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def show(self):
        print("Adjacency List:")
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")

option = input("Press '1' for Unweighted Undirected, '2' for Weighted Directed, '3' for Weighted Undirected: ")

graph = Graph(5)

if option == '1':
    graph.addEdge1(0, 1)
    graph.addEdge1(0, 4)
    graph.addEdge1(1, 2)
    graph.addEdge1(1, 3)
    graph.addEdge1(1, 4)
    graph.addEdge1(2, 3)
    graph.addEdge1(3, 4)

elif option == '2':
    graph.addEdge2(0, 1, 2)
    graph.addEdge2(0, 4, 3)
    graph.addEdge2(1, 2, -3)
    graph.addEdge2(1, 3, 4)
    graph.addEdge2(1, 4, 5)
    graph.addEdge2(2, 3, -5)
    graph.addEdge2(3, 4, 6)

elif option == '3':
    graph.addEdge3(0, 1, 3)
    graph.addEdge3(0, 4, -10)
    graph.addEdge3(1, 2, -5)
    graph.addEdge3(1, 3, 10)

else:
    print("Invalid Option")

graph.show()
