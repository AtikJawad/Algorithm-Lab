class dfs:
    def __init__(self,n):
        self.n = n
        self.color = ["white"]*n
        self.parent = [-1]*n
        self.d=[0]*n
        self.f= [0]*n
        self.time = 0
        self.dfs_order = []
        self.topological_sort = []

    def DFS(self,adj):
        self.adj= adj

        for u in range(self.n):
            self.color[u] = "white"
            self.parent[u] = -1
            self.d[u] = 0
            self.f[u] = 0
        self.time = 0
        print("Vertex\tParent\tBeg_time\tend_time\tcolor")
        for u in range(self.n):
            if self.color[u] == "white":
                self.DFS_visit(u)
        print("DFS Order: ", self.dfs_order)
        print("Topological sort: ", list(reversed(self.topological_sort)))

    def DFS_visit(self,u):
        self.color[u] = "grey"
        self.time += 1
        self.d[u] = self.time

        self.dfs_order.append(u)
        for v in range(self.n):
            if self.adj[u][v] == 1 and self.color[v] == "white":
                self.parent[v] = u
                self.DFS_visit(v)
        self.color[u] = "black"
        self.time += 1
        self.f[u] = self.time
        self.topological_sort.append(u)
        print(f"{u}\t{self.parent[u]}\t{self.d[u]}\t{self.f[u]}\t{self.color[u]}")


n= int(input("number of Vertx: "))
adj=[]

for _ in range(n):
    row_values = input(f"Input {_} adjacency row with space: ").strip()
    row = list(map(int,row_values.split()))
    adj.append(row)

traverse = dfs(n)
traverse.DFS(adj)

# filename="E:\\Studies\\Uni\\2-2\\Design & Analysis of Algorithm\\Algo lab\\input files\\DFS input.txt"
# with open(filename, "r") as f:
#     lines = [line.strip() for line in f.readlines()]
# 
# n_vert = int(lines[0])
# 
# 
# adj = [[0 for col in range(n_vert)] for row in range(n_vert)]
# 
# edgelines= lines[1:]
# 
# for edge in edgelines:
#     u,v = map(int, edge.split())
#     adj[u][v] = 1
#     adj [v][u] = 1
# 
# dfs = DFS(n_vert)
# dfs.doDFS(adj)

