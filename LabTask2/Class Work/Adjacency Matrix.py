class adjacent:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        
        self.adj_matrix = [] 

        for i in range(num_vertices):
            row = []  
            for j in range(num_vertices):
                row.append(0) 
            self.adj_matrix.append(row)

            
    def addEdge1(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    
    def addEdge2(self, u, v, weight):
        self.adj_matrix[u][v] = weight

    def addEdge3(self, u, v, weight):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def show(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)



option =input("press '1' for Unweighted Undirected & '2' for Weighted Directed & '3' for Weighted Undirected: ")

if option=='1':

    graph=adjacent(5)
    graph.addEdge1(0, 1);
    graph.addEdge1(0, 4);
    graph.addEdge1(1, 2);
    graph.addEdge1(1, 3);
    graph.addEdge1(1, 4);
    graph.addEdge1(2, 3);
    graph.addEdge1(3, 4);
    graph.show()

elif option=="2":
    graph=adjacent(5)
    graph.addEdge2(0, 1, 2);
    graph.addEdge2(0, 4, 3);
    graph.addEdge2(1, 2, -3);
    graph.addEdge2(1, 3, 4);
    graph.addEdge2(1, 4, 5);
    graph.addEdge2(2, 3, -5);
    graph.addEdge2(3, 4, 6);
    graph.show()

elif option =="3":
    graph=adjacent(5)
    graph.addEdge3(0, 1, 3);
    graph.addEdge3(0, 4, -10);
    graph.addEdge3(1, 2, -5);
    graph.addEdge3(1, 3, 10);
    graph.show()

else:
    print("Invalid Option")
