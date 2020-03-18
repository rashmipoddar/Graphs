from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        else:
            # print('ERROR: The vertex does not exist')
            raise ValueError('The vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError('The vertex does not exist')

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        if ancestor[0] not in graph.vertices:
            graph.add_vertex(ancestor[0])
        if ancestor[1] not in graph.vertices:
            graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[0], ancestor[1])
    # print(graph.vertices)

    # for k,v in graph.vertices.items():
    #     print(f'{k} {graph.get_neighbors(k)}')

    # longest_path = []
    # q = Queue()
    # q.enqueue([starting_node])
    # visited = set()
    # print(q.queue)
    # while q.size():
        
    #     print('infinite loop')
    #     path = q.dequeue()
    #     print(path)
    #     if len(path) > len(longest_path):
    #         longest_path = path.copy()
    #     last_vertex = path[-1]
    #     if last_vertex not in visited:
    #         visited.add(last_vertex)
    #     for neighbor in graph.get_neighbors(last_vertex):
    #         copy = path.copy()
    #         copy.append(neighbor)
    #         q.enqueue(copy)
    # return longest_path

    # Searching for the longest path from the starting node
    # While there is a parent node for a starting node
    # Find the parents of the starting node
    # Store the parents and the depth level of the parent in a new array
    # Repeat the process till the node has no parent
    # Check the array with the highest depth and return the smaller parent


        

relationships = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(relationships, 1)
