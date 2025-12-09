class Adjacency:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v, w, directed):
        # Add edge
        self.matrix[u][v] = w

        if not directed:  # undirected
            self.matrix[v][u] = w

    def show(self):
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)


# ---------------------------
#        FILE INPUT
# ---------------------------

filename = input("Enter input filename: ")

with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]

num_vertices = int(lines[0])   # number of vertices
num_edges = int(lines[1])      # number of edges

edge_lines = lines[2:2 + num_edges]          # list of edges
graph_type1 = lines[2 + num_edges]           # Directed/Undirected
graph_type2 = lines[3 + num_edges]           # Weighted/Unweighted

directed = (graph_type1.lower() == "directed")
weighted = (graph_type2.lower() == "weighted")

graph = Adjacency(num_vertices)

# Process each edge
for line in edge_lines:
    parts = line.replace(",", " ").split()

    u = int(parts[0])
    v = int(parts[1])

    if weighted:
        w = int(parts[2])
    else:
        w = 1  # default weight for unweighted edges

    graph.add_edge(u, v, w, directed)

graph.show()
