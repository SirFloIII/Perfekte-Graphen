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

def MCS(G: Graph) -> list:
    cardinality = {v : 0 for v in G.vertices}
    order = []
    for _ in range(len(G.vertices)):
        u = max(cardinality, key=cardinality.get)
        order.append(u)
        del cardinality[u]
        for w in G.adj(u):
            if w in cardinality:
                cardinality[w] += 1
    return reversed(order)

def MCS2(G: Graph) -> list:
    cardinality = {v : 0 for v in G.vertices}
    vertices_by_cardinality = defaultdict(set)
    vertices_by_cardinality[0] = set(G.vertices)
    max_cardinality = 0
    order = []
    for _ in range(len(G.vertices)):
        while len(vertices_by_cardinality[max_cardinality]) == 0:
            max_cardinality -= 1
        u = vertices_by_cardinality[max_cardinality].pop()
        order.append(u)
        del cardinality[u]
        for w in G.adj(u):
            if w in cardinality:
                c = cardinality[w]
                cardinality[w] += 1
                vertices_by_cardinality[c].remove(w)
                vertices_by_cardinality[c+1].add(w)
                max_cardinality = max(max_cardinality, c+1)
    return reversed(order)


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

    G1 = GraphWithAdj([1, 2, 3, 4, 5],
                    [
                        (1, 2),
                        (1, 3),
                        (1, 4),
                        (1, 5),
                        (2, 5),
                        (3, 4),
                        (3, 5),
                        (4, 5),
                    ])
                

    print(list(MCS(G)))