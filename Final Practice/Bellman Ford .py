INF = 9999

def bellman(graph, source,vertices):
    #INITIALIZE SOURCE VERTICES
    V = len(vertices)
    dist=[INF]*V
    parent= [-1]*V
    dist[source] = 0

    #relaxation
    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                if graph[u][v] != INF:
                    if dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
                        parent[v] = u

    neg_cycle = [False]*V
    any_neg = False
    for u in range(V):
        for v in range(V):
            if graph[u][v] != INF:
                if dist[v] > dist[u] + graph[u][v]:
                    neg_cycle[v] = True
                    any_neg = True
    print("Vertex\t parent\t distance\t Negative Cycle")
    print("____________________________________________")

    for i in range(V):
        d = dist[i] if dist[i] < INF else "INF"
        p = vertices[parent[i]] if parent[i] != -1 else "NULL"
        print(f"{vertices[i]}\t {p}\t {d}\t {neg_cycle[i]}")

    if any_neg:
        print("Negative Cycle detected")
    else:
        print("NO Negative Cycles")

vertices = input("Enter vertices with space: ").split()
V = len(vertices)

graph= [[INF for col in range(V)] for row in range(V)]

while True:
    data = input("Enter Edge connection with weight e.g. (0 1 20) {Press q to quit}: ").strip()
    if data == "q":
        break
    u,v,w = map(int,data.split())
    graph[u][v] = w

bellman(graph,0,vertices)

graph = [
#     [0,     6,    INF,   7,    INF],  # s
#     [INF,   0,      5,    8,    -4],  # t
#     [INF,  -2,      0,  INF,   INF],  # x
#     [INF,  INF,    -3,    0,     9],  # y
#     [2,    INF,     7,  INF,     0]   # z
# ]
