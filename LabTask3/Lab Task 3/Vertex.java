public class Vertex {
    String name;
    String color;
    int dist;
    Vertex parent;

    public Vertex(String name) {
        this.name = name;
        this.color = "White";
        this.dist = Integer.MAX_VALUE;
        this.parent = null;
    }
}
