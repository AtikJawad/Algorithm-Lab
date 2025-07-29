public class Vertex {
    String name;
    String color;
    int dist;
    Vertex parent;

    public Vertex(String v) {

        this.name=v;
        this.color = "White";
        this.dist = 9999;
        this.parent = null;
    }
}
