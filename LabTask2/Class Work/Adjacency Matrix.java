import java.util.Scanner;

class Adjacent {
    private int[][] adjMatrix;
    private int numVertices;

    // Constructor
    public Adjacent(int numVertices) {
        this.numVertices = numVertices;
        adjMatrix = new int[numVertices][numVertices]; // Matrix is initialized to 0 by default in Java

        
    }

    // Unweighted Undirected
    public void addEdge1(int u, int v) {
        if (u >= 0 && u < numVertices && v >= 0 && v < numVertices) {
            adjMatrix[u][v] = 1;
            adjMatrix[v][u] = 1;
        }
    }

    // Weighted Directed
    public void addEdge2(int u, int v, int weight) {
        if (u >= 0 && u < numVertices && v >= 0 && v < numVertices) {
            adjMatrix[u][v] = weight;
        }
    }

    // Weighted Undirected
    public void addEdge3(int u, int v, int weight) {
        if (u >= 0 && u < numVertices && v >= 0 && v < numVertices) {
            adjMatrix[u][v] = weight;
            adjMatrix[v][u] = weight;
        }
    }

    public void show() {
        System.out.println("Adjacency Matrix:");
        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                System.out.print(adjMatrix[i][j] + "\t");
            }
            System.out.println();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Press '1' for Unweighted Undirected, '2' for Weighted Directed, '3' for Weighted Undirected: ");
        String option = input.nextLine();

        Adjacent graph = new Adjacent(5);

        switch (option) {
            case "1":
                graph.addEdge1(0, 1);
                graph.addEdge1(0, 4);
                graph.addEdge1(1, 2);
                graph.addEdge1(1, 3);
                graph.addEdge1(1, 4);
                graph.addEdge1(2, 3);
                graph.addEdge1(3, 4);
                break;

            case "2":
                graph.addEdge2(0, 1, 2);
                graph.addEdge2(0, 4, 3);
                graph.addEdge2(1, 2, -3);
                graph.addEdge2(1, 3, 4);
                graph.addEdge2(1, 4, 5);
                graph.addEdge2(2, 3, -5);
                graph.addEdge2(3, 4, 6);
                break;

            case "3":
                graph.addEdge3(0, 1, 3);
                graph.addEdge3(0, 4, -10);
                graph.addEdge3(1, 2, -5);
                graph.addEdge3(1, 3, 10);
                break;

            default:
                System.out.println("Invalid Option");
                return;
        }
        graph.show();
    }
}
