class adjacency:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices

        self.matrix = [[0 for col in range(num_vertices)] for row in range(num_vertices)] # inputting a 2d matrix 
                                                                                          

    def addEdge1(self,u,v):  # unweighted undirected 
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1

    def addEdge2(self,u,v, weight):  # weighted directed 
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
    
    def addEdge3(self,u,v,weight):  # weighted undirected 
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
            self.matrix[v][u] = weight

    def show(self):
        print("adjacency matrix: ")
        for row in self.matrix:
            print(row)

option =input("press '1' for Unweighted Undirected & '2' for Weighted Directed & '3' for Weighted Undirected: ")

nVert = int (input("NUMBER OF VERTEX: "))

graph = adjacency(nVert)

print("----ENTER EDGES----")

if option == '1':
    while True :
        data = input("format: u (space) v (type q to stop): ").strip()
        if data == "q":
            break
        u,v = map(int, data.split())
        graph.addEdge1(u,v)
    graph.show()

if option == '2':
    while True :
        data = input("format: u (spc) v (spc) w (type q to stop): ").strip()
        if data == "q":
            break
        u, v, w = map(int, data.split())
        graph.addEdge2(u,v,w)
    graph.show()

if option == '3':
    while True :
        data = input("format: u (spc) v (spc) w (type q to stop): ").strip()
        if data == "q":
            break
        u, v, w = map(int, data.split())
        graph.addEdge3(u,v,w)
    graph.show()
