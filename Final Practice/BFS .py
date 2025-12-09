class vertex:
    def __init__(self,name):
        self.name=name
        self.color = "white"
        self.dist = 9999
        self.parent = None

def bfs(vertices,adj,source):
    queue = []

    s= vertices[source]
    s.color = "grey"
    s.dist = 0
    s.parent= None

    queue.append(s)

    bfsOrder= []

    print("Vertex   |  Parent   |  Distance   |  Color")
    print("__________________________________")

    while queue:
        u = queue.pop(0)
        u_index = vertices.index(u)

        bfsOrder.append(u)

        parent_name = u.parent.name if u.parent else "Null"
        print(f"{u.name} | {parent_name} | {u.dist} | {u.color}")

        for v_index in range(len(adj)):
            if adj[u_index][v_index] == 1:
                v= vertices[v_index]

                if v.color == "white":
                    v.color = "grey"
                    v.dist = u.dist + 1
                    v.parent = u
                    queue.append(v)
        u.color = "black"

    print("bfs order: ")
    for vertices in bfsOrder:
        print(vertices.name, end="->")



filename = "G://Algo lab//input files//BFSinput.txt"

with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

verticeList= lines[0].split()
n_vert = len(verticeList)
vertices = [vertex(name) for name in verticeList]

adj = [[0 for col in range(n_vert)] for row in range(n_vert) ]

edgelines = lines[1:]

for edge in edgelines:
        u,v = map(int, edge.split())
        adj[u][v] = 1
        adj[v][u] = 1

bfs(vertices, adj, 0)

# if user input is asked from terminal.....

# verticelist= input("enter vertices with space (A B ..) : ").split()
# n_vert = len(verticelist)
# vertices = [vertex(name) for name in verticelist ]
# adj = [[0 for col in range(n_vert)] for row in range(n_vert)]
# 
# while True:
#     edge= input("Insert edges (1 0/ 2 3) & press q to stop: ")
#     if edge == 'q':
#         break
#     u,v = map(int, edge.split())
#     adj[u][v] = 1
#     adj[v][u] = 1
# 
# bfs( vertices, adj, 0)





