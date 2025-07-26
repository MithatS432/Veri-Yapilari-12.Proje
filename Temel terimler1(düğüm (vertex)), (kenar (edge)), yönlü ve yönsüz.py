class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)  # Yönsüz olduğu için tersini de ekliyoruz

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")

# Kullanım
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

print("Yönsüz Graf:")
g.print_graph()
