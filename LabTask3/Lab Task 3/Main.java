import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new FileReader("graph_input.txt"));

            String[] vertexNames = br.readLine().trim().split("\\s+");

            int V = vertexNames.length;
            Vertex[] vertices = new Vertex[V];
            Map<String, Integer> nameToIndex = new HashMap<>();

            for (int i = 0; i < V; i++) {
                vertices[i] = new Vertex(vertexNames[i]);
                nameToIndex.put(vertexNames[i], i);
            }

            int[][] adjMatrix = new int[V][V];

            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                if (parts.length < 2) continue;

                int u = nameToIndex.get(parts[0]);
                int v = nameToIndex.get(parts[1]);

                adjMatrix[u][v] = 1;
                adjMatrix[v][u] = 1;

            }

            br.close();


            BFS bfs = new BFS();
            bfs.doBFS(vertices, adjMatrix, 0);

            System.out.println("\nBFS Traversal Steps:");
            for (Vertex v : vertices) {
                System.out.println("Vertex: " + v.name +
                        ", Parent: " + (v.parent != null ? v.parent.name : "null") +
                        ", Distance: " + v.dist +
                        ", Color: " + v.color);
            }

        } catch (IOException e) {
            e.getMessage();
        }
    }
}
