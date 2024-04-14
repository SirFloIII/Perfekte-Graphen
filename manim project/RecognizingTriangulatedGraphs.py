from manim import Graph
from collections import defaultdict

def Lex_BFS(G: Graph) -> list:
    # vertex -> list[int]
    label = {v : [] for v in G.vertices}
    order = []
    for i in range(len(G.vertices), 0, -1):
        v = pick_maximal_unnumbered_vertex(label, order)
        order.append(v)
        for w in G.adj(v):
            label[w].append(i)
    return reversed(order)

def pick_maximal_unnumbered_vertex(label, order):
    max_vertex = None
    max_value = None
    for vertex, value in label.items():
        if vertex in order:
            continue
        if lexographical_order(value, max_value):
            max_vertex = vertex
            max_value = value
    return max_vertex

# True: the first is bigger
def lexographical_order(a, b):
    if b is None or len(b) == 0:
        return True
    if a is None or len(a) == 0:
        return False
    if a[0] != b[0]:
        return a[0] > b[0]
    return lexographical_order(a[1:], b[1:])



class GraphWithAdj(Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def adj(self, v):
        for w in self.vertices:
            if (v, w) in self.edges or (w, v) in self.edges:
                yield w

if __name__ == "__main__":

    G = GraphWithAdj([1, 2, 3, 4, 5, 6, 7],
                    [
                        (1, 2),
                        (2, 3),
                        (3, 4),
                        (5, 6),
                        (1, 5),
                        (2, 5),
                        (2, 6),
                        (3, 6),
                        (3, 7),
                        (4, 7),
                    ])

    print(list(Lex_BFS(G)))