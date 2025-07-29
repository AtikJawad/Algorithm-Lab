import java.util.LinkedList;
import java.util.Queue;

public class BFS {

    Queue<Vertex>queue=new LinkedList<>();


    public void doBFS(Vertex[] vertices,int[][] adjMatrix,int sIndex) {
        Vertex s = vertices[sIndex];
        s.color="Grey";
        s.dist=0;
        s.parent=null;

        queue.add(s);

        while(!queue.isEmpty()){

            Vertex u = queue.remove();
            int uIndex= getIndex(vertices,u);

            for(int vIndex = 0;vIndex<adjMatrix.length; vIndex++){
                if (adjMatrix[uIndex][vIndex] == 1){

                    Vertex v = vertices[vIndex];
                    if (v.color.equalsIgnoreCase("White")){
                        v.color= "Grey";
                        v.dist= u.dist+1;
                        v.parent= u;

                        queue.add(v);
                    }
                }
            } // end of inner loop
        u.color="Black";
        }
    }
    public static int getIndex(Vertex[] vertices, Vertex v){
        for (int i=0;i<vertices.length; i++){
            if(vertices[i] == v ) return i;
        }
        return -1;
    }
}
