from numpy.f2py.crackfortran import endifs

INF = 9999
def prims(graph):
    V = len(graph)
    key=[INF]*V
    parent = [-1]*V
    selected = [False]*V

    key[0]= 0

    for _ in range (V):
        min_key = INF
        u = -1

        for v in range(V):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u=v
        selected[u] = True
        for v in range(V):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    print("EDGE\t Weight")
    print("___________________")

    total_weight = 0
    for i in range(1,V):
        print(f"{parent[i]} - {i}\t {graph[i][parent[i]]}")
        total_weight += graph[i][parent[i]]
    print(f"Total Minimum Weights: {total_weight}")



filename = "G:\\Algo lab\\input files\\Prims Input.txt"
with open (filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]

graph = []

rows = lines[0:]

for values in rows:
    data = list(map(int,values.replace(",", " ").split()))
    graph.append(data)
  
prims(graph)

# graph = [
#     [0, 0, 47, 0, 80, 54, 0, 0],
#     [0, 0, 55, 31, 32, 0, 74, 79],
#     [47, 55, 0, 88, 23, 75, 66, 0],
#     [0, 31, 88, 0, 0, 74, 0, 29],
#     [80, 32, 23, 0, 0, 0, 93, 0],
#     [54, 0, 75, 74, 0, 0, 0, 0],
#     [0, 74, 66, 0, 93, 0, 0, 68],
#     [0, 79, 0, 29, 0, 0, 68, 0]
# ]


prims(graph)
