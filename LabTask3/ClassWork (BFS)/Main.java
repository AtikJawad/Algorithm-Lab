//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Vertex a = new Vertex("A");
        Vertex b = new Vertex("B");
        Vertex c = new Vertex("C");
        Vertex d = new Vertex("D");

        Vertex[] vertices = {a,b,c,d};
        int [][] adjMatrix = {
                //A B C D
                {0,1,1,1}, //A
                {1,0,0,1},//B
                {1,0,0,0},//C
                {0,1,0,0} //D
        };

        new BFS().doBFS(vertices,adjMatrix,0);

        for (int i=0; i< vertices.length;i++){
            Vertex v = vertices[i];
            String parentName= (v.parent != null) ? v.parent.name : "null";

            System.out.println("Vertex = "+v.name+": distance = "+v.dist+ " Parent= " +parentName);
        }


        }
    }
