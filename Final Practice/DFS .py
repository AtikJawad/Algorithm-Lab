from fileinput import filename


class DFS:
    def __init__(self,n):
        self.n=n
        self.color = ["white"] * n
        self.parent = [-1] * n
        self.beg_time = [0] * n
        self.end_time = [0] * n
        self.time = 0
        self.DfsOrder =[]

    def doDFS(self,adj):
        self.adj = adj
        for u in range(self.n):
            self.color[u] = "white"
            self.parent[u] = -1
            self.beg_time[u] = 0
            self.end_time[u] = 0 #not in algo
        self.time = 0

        print("Vertex   |  Color  |   Beg Time  |   End Time  |   Parent")

        for u in range(self.n):
            if self.color[u] == "white":
                self.DFS_VISIT(u)
        print(f"DFS Order: {self.DfsOrder} ")
    def DFS_VISIT(self,u):
        self.color[u] = "grey"
        self.time+=1
        self.beg_time[u] = self.time

        self.DfsOrder.append(u)


        for v in range(self.n):
            if self.adj[u][v] == 1 and self.color[v] == "white":
                self.parent[v] = u
                self.DFS_VISIT(v)
        self.color[u] = "black"
        self.time += 1
        self.end_time[u] = self.time

        print(f"{u}  {self.color[u]}   {self.beg_time[u]}    {self.end_time[u]}   {self.parent[u]}")

filename="G:\\Algo lab\\input files\\DFS input.txt"
with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]

n_vert = int(lines[0])


adj = [[0 for col in range(n_vert)] for row in range(n_vert)]

edgelines= lines[1:]

for edge in edgelines:
    u,v = map(int, edge.split())
    adj[u][v] = 1
    adj [v][u] = 1

dfs = DFS(n_vert)
dfs.doDFS(adj)


#adj = [
    #     [0, 1, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1],
    #     [0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 1, 0, 1, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0],
    #     [1, 0, 1, 1, 0, 0, 0, 0]
    # ]
    # 
    # dfs = DFS(8)
    # dfs.doDFS(adj)

