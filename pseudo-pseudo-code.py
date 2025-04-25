from typing import Dict, Set, Iterable
import random
from itertools import permutations
import networkx as nx
from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt

class DirectedGraph:
    def __init__(self) -> None:
        # Adjacency list for outgoing edges
        self.outgoing: Dict['Vertex', Set['Vertex']] = {}
        # Adjacency list for incoming edges
        self.incoming: Dict['Vertex', Set['Vertex']] = {}
        # Dictionary to map names to Vertex objects
        self.name_to_vertex: Dict[str, 'Vertex'] = {}

    def add_vertex(self, name: str) -> 'Vertex':
        if name in self.name_to_vertex:
            raise ValueError(f"Vertex with name {name} already exists.")
        vertex = Vertex(self, name)
        self.outgoing[vertex] = set()
        self.incoming[vertex] = set()
        self.name_to_vertex[name] = vertex
        return vertex

    def add_vertices(self, names: Iterable) -> None:
        for name in names:
            self.add_vertex(name)

    def add_edge(self, from_vertex: 'Vertex | str', to_vertex: 'Vertex | str') -> None:
        if not isinstance(from_vertex, Vertex):
            from_vertex = self.get_vertex_by_name(from_vertex)
        if not isinstance(to_vertex, Vertex):
            to_vertex = self.get_vertex_by_name(to_vertex)
        if from_vertex not in self.outgoing or to_vertex not in self.outgoing:
            raise ValueError("Both vertices must be added to the graph before adding an edge.")
        self.outgoing[from_vertex].add(to_vertex)
        self.incoming[to_vertex].add(from_vertex)

    def remove_edge(self, from_vertex: 'Vertex', to_vertex: 'Vertex') -> None:
        if from_vertex in self.outgoing and to_vertex in self.outgoing[from_vertex]:
            self.outgoing[from_vertex].remove(to_vertex)
        if to_vertex in self.incoming and from_vertex in self.incoming[to_vertex]:
            self.incoming[to_vertex].remove(from_vertex)

    def get_out_neighbors(self, vertex: 'Vertex') -> Set['Vertex']:
        if vertex not in self.outgoing:
            raise ValueError(f"Vertex {vertex} does not exist in the graph.")
        return self.outgoing[vertex]

    def get_in_neighbors(self, vertex: 'Vertex') -> Set['Vertex']:
        if vertex not in self.incoming:
            raise ValueError(f"Vertex {vertex} does not exist in the graph.")
        return self.incoming[vertex]

    def remove_vertex(self, vertex: 'Vertex') -> None:
        if vertex in self.outgoing:
            for neighbor in self.outgoing[vertex]:
                self.incoming[neighbor].remove(vertex)
            del self.outgoing[vertex]
        if vertex in self.incoming:
            for neighbor in self.incoming[vertex]:
                self.outgoing[neighbor].remove(vertex)
            del self.incoming[vertex]
        if vertex.name in self.name_to_vertex:
            del self.name_to_vertex[vertex.name]

    def get_vertex_by_name(self, name) -> 'Vertex':
        if name not in self.name_to_vertex:
            raise ValueError(f"Vertex with name {name} does not exist.")
        return self.name_to_vertex[name]

    @property
    def vertices(self) -> Set['Vertex']:
        return set(self.name_to_vertex.values())

class Vertex:
    def __init__(self, graph: DirectedGraph, name) -> None:
        self.graph: DirectedGraph = graph
        self.name = name

    def add_outgoing_edge(self, to_vertex: 'Vertex') -> None:
        self.graph.add_edge(self, to_vertex)

    def add_incoming_edge(self, from_vertex: 'Vertex') -> None:
        self.graph.add_edge(from_vertex, self)

    def remove_outgoing_edge(self, to_vertex: 'Vertex') -> None:
        self.graph.remove_edge(self, to_vertex)

    def remove_incoming_edge(self, from_vertex: 'Vertex') -> None:
        self.graph.remove_edge(from_vertex, self)

    @property
    def out_neighbors(self) -> Set['Vertex']:
        return self.graph.get_out_neighbors(self)

    @property
    def in_neighbors(self) -> Set['Vertex']:
        return self.graph.get_in_neighbors(self)
    
    @property
    def outdegree(self) -> int:
        return len(self.out_neighbors)

    @property
    def indegree(self) -> int:
        return len(self.in_neighbors)
    
    def remove(self) -> None:
        self.graph.remove_vertex(self)

    def __repr__(self) -> str:
        return f"Vertex({self.name})"



def generate_random_graph(num_vertices: int, num_edges: int) -> DirectedGraph:
    if num_edges > num_vertices * (num_vertices - 1):
        raise ValueError("Too many edges for the given number of vertices.")

    graph = DirectedGraph()
    vertices = [graph.add_vertex(f"v{i}") for i in range(num_vertices)]

    all_possible_edges = [(v1, v2) for v1 in vertices for v2 in vertices if v1 != v2]
    random.shuffle(all_possible_edges)

    for from_vertex, to_vertex in all_possible_edges[:num_edges]:
        graph.add_edge(from_vertex, to_vertex)

    return graph


def generate_random_comparability_graph(num_vertices: int, density_parameter: int) -> DirectedGraph:
    vertices = [tuple(random.randint(0, 100) for _ in range(density_parameter)) for _ in range(num_vertices)]
    graph = DirectedGraph()
    graph.add_vertices(vertices)

    for from_vertex, to_vertex in permutations(vertices, 2):
        if all(from_vertex[k] < to_vertex[k] for k in range(density_parameter)):
            graph.add_edge(from_vertex, to_vertex)

    return graph

def compute_height(G: DirectedGraph) -> dict[Vertex, int]:
    h = dict()
    unset_inneighbor_count = {u: u.indegree for u in G.vertices}
    
    def DFS(u: Vertex):
        unset_inneighbor_count[u] -= 1
        if unset_inneighbor_count[u] == 0:
            h[u] = max(h[v] for v in u.in_neighbors) + 1
            for w in u.out_neighbors:
                DFS(w)
        
    for u in G.vertices:
        if u.indegree == 0:
            h[u] = 0
            for v in u.out_neighbors:
                DFS(v)
    
    return h

def find_path(G: DirectedGraph) -> list[Vertex]:
    h = compute_height(G)

    max_vertex = max(h, key=h.get)
    
    current_vertex = max_vertex
    path = [max_vertex]
    while h[current_vertex] > 0:
        for neighbor in current_vertex.in_neighbors:
            if h[neighbor] == h[current_vertex] - 1:
                current_vertex = neighbor
                break
        path.append(current_vertex)

    path.reverse()
    return path


if __name__ == "__main__":
    num_vertices = 50
    density_parameter = 2
    graph = generate_random_comparability_graph(num_vertices, density_parameter)
    


    # Compute the height of the graph
    height = compute_height(graph)

    # Find the path in the graph
    path = find_path(graph)
    print("Path:", [v.name for v in path])

    # Convert DirectedGraph to a NetworkX DiGraph for visualization
    nx_graph = nx.DiGraph()
    for vertex in graph.name_to_vertex.values():
        for neighbor in vertex.out_neighbors:
            nx_graph.add_edge(vertex.name, neighbor.name)
            if abs(height[vertex] - height[neighbor]) == 1:
                nx_graph[vertex.name][neighbor.name]['color'] = 'black'

    # Color the edges in the path red
    for i in range(len(path) - 1):
        nx_graph[path[i].name][path[i + 1].name]['color'] = 'red'

    # Draw the graph
    cmap = plt.cm.viridis
        
    pos = {vertex.name: (vertex.name[0], vertex.name[1]) for vertex in graph.vertices}
    node_colors = [height[graph.get_vertex_by_name(node)] for node in nx_graph.nodes]
    edge_colors = [nx_graph[u][v]['color'] if 'color' in nx_graph[u][v] else 'gray' for u, v in nx_graph.edges]
    edge_widths = [2 if 'color' in nx_graph[u][v] else 0.5 for u, v in nx_graph.edges]
    nx.draw(
        nx_graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        width=edge_widths,
        node_size=2000,
        font_size=10,
        cmap=cmap
    )
    plt.title("Directed Graph")
    # Add a color legend
    # Define discrete boundaries for the color bar
    levels = list(range(min(height.values()), max(height.values()) + 2))  # Add 1 to include the upper bound
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Associate the ScalarMappable with the colorbar
    cbar = plt.colorbar(sm, ax=plt.gca(), shrink=0.8)  # Scale down the color bar
    cbar.set_label('Height')
    cbar.set_ticks([level + 0.5 for level in levels[:-1]])  # Shift ticks to the center of each color
    cbar.set_ticklabels(levels[:-1])  # Set tick labels to match the levels
    
    plt.show()










    


















