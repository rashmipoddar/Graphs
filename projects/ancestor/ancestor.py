from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError('The vertex does not exist')

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])
    max_path_length = 1
    earliest_ancestor = -1
    q = Queue()
    q.enqueue([starting_node])
    while q.size():
        path = q.dequeue()
        last_vertex = path[-1]
        if (len(path) >= max_path_length and last_vertex < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = last_vertex
            max_path_length = len(path)
        for neighbor in graph.vertices[last_vertex]:
            # list(path) creates a new list with all the path elements
            # it is same as path.copy()
            copy = list(path)
            copy.append(neighbor)
            q.enqueue(copy)
    return earliest_ancestor

    # This has to be a breadth first traversal
    # Searching for the longest path from the starting node
    # While there is a parent node for a starting node
    # Find the parents of the starting node
    # Store the parents and the depth level of the parent in a new array
    # Repeat the process till the node has no parent
    # Check the array with the highest depth and return the smaller parent

relationships = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(relationships, 6)
