import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        try {

            Scanner sc = new Scanner(System.in);

            String filePath = "C:\\Users\\Atik\\Desktop\\graph_input.txt";

            BufferedReader br = new BufferedReader(new FileReader(filePath));

            int vCount = Integer.parseInt(br.readLine().trim()); // 1st line of file
            int eCount = Integer.parseInt(br.readLine().trim()); // 2nd line of file

            HashMap<String, Integer> map = new HashMap<>(); // Initializing HashMap for storing Key,Value pairs

            String[] IndexTOVertex = new String[vCount];
            int[][] matrix = new int[vCount][vCount];
            int index = 0;

            for (int i = 0; i < eCount; i++) {
                String[] LinePart = br.readLine().split(","); //reads all the edge lines like A,B,2 and so on

                String u = LinePart[0].trim(); // e.g. saves the A from A,B,2
                String v = LinePart[1].trim(); // e.g. saves the B from A,B,2
                int weight = Integer.parseInt(LinePart[2].trim()); // // e.g. saves the integer 2 from A,B,2

                if (!map.containsKey(u)) {
                    map.put(u, index);   // Puts the key:value pair of u such as (A,0) from A,B,2
                    IndexTOVertex[index] = u;
                    index++;
                }
                if (!map.containsKey(v)) {
                    map.put(v, index); // Puts the key:value pair of v such as (B,1) from A,B,2
                    IndexTOVertex[index] = v;
                    index++;
                }
                int row = map.get(u);
                int col = map.get(v);
                matrix[row][col] = weight; // initially directed and weighted
            }

            // Reading the lines after the EdgeDescription
            String graphType = br.readLine().trim(); // reads whether the graph is Directed or Undirected (2nd last line of file)
            String weightType = br.readLine().trim(); // reads whether the graph is Weighted or Unweighted (last line of file)

            if (graphType.equalsIgnoreCase("Undirected")) {
                for (int i = 0; i < vCount; i++) {
                    for (int j = 0; j < vCount; j++) {
                        if (matrix[i][j] != 0) { //if the connection of [i][j] already exists

                            matrix[j][i] = matrix[i][j]; //put whatever value is there in [i][j] to [j][i]

                        }
                    }
                }
            }
            if (weightType.equalsIgnoreCase("Unweighted")) {
                for (int i = 0; i < vCount; i++) {
                    for (int j = 0; j < vCount; j++) {
                        if (matrix[i][j] != 0) { //if the connection of [i][j] already exists

                            matrix[i][j] = 1;

                        }
                    }
                }
            }

            // Printing The Matrix (Finally 😭)
            System.out.println("\nADJACENCY MATRIX:\n");
            System.out.print("\t");
            for (int i = 0; i < vCount; i++) {
                System.out.print("\t"+IndexTOVertex[i] + "\t");
            }
            System.out.println("\n");

            for (int i = 0; i < vCount; i++) {
                System.out.print(IndexTOVertex[i] + "\t");
                for (int j = 0; j < vCount; j++) {
                    System.out.print("\t"+matrix[i][j] + "\t");
                }
                System.out.println("\n");
            }
            br.close();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
