from collections import deque

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)  # Yönlü olduğu için sadece u'dan v'ye

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:")
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend([neigh for neigh in self.graph[vertex] if neigh not in visited])

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Kullanım
dg = DirectedGraph()
dg.add_edge("1", "2")
dg.add_edge("1", "3")
dg.add_edge("2", "4")
dg.add_edge("3", "4")
dg.add_edge("4", "5")

print("\nYönlü Graf:")
dg.print_graph()
dg.bfs("1")
