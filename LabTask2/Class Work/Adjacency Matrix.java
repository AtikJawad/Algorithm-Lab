import java.util.Scanner;

public class GraphAdjMatrix {
private int[][] adjMatrix;
private int numVertices;

// Constructor
public GraphAdjMatrix(int numVertices) {
this.numVertices = numVertices;
adjMatrix = new int[numVertices][numVertices];
}

// Add edge
public void addEdge(int i, int j) {
adjMatrix[i][j] = 1;
adjMatrix[j][i] = 1;
}

// Print matrix
public void printMatrix() {
System.out.println(&quot;Adjacency Matrix:&quot;);
for (int i = 0; i &lt; numVertices; i++) {
for (int j = 0; j &lt; numVertices; j++) {
System.out.print(adjMatrix[i][j] + &quot; &quot;);
}
System.out.println();
}
}

// Main method
public static void main(String[] args) {
GraphAdjMatrix graph = new GraphAdjMatrix(5);

graph.addEdge(0, 1);
graph.addEdge(0, 4);
graph.addEdge(1, 2);
graph.addEdge(1, 3);
graph.addEdge(1, 4);
graph.addEdge(2, 3);
graph.addEdge(3, 4);

graph.printMatrix();
}
}
