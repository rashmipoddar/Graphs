"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
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
        else:
            # print('ERROR: The vertex does not exist')
            raise ValueError('The vertex does not exist')

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            print('ERROR: The vertex does not exist')
            raise ValueError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError('The vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a Queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store the visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size():
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it has been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all of its neighbors
                # print(self.get_neighbors(v))
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a Stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store the visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size():
            # Pop the first vertex
            v = s.pop()
            # Check if it has been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all of its neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Check if the node has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            print(starting_vertex)
            visited.add(starting_vertex)
            # print('visited', visited)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        BFS will always return the shortest path
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size():
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the vertex from the end of THE PATH
            last_vertex = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if last_vertex not in visited:
                # Mark it as visited
                visited.add(last_vertex)
                # Check if it is the target
                if last_vertex == destination_vertex:
                    # If so, return the path
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(last_vertex):
                    # Make a copy of the path
                    copy = path.copy()
                    # Add the neighbor to the copy
                    copy.append(neighbor)
                    # Enqueue the copy
                    # q.enqueue([*path, neighbor])
                    # Line 155 uses the splat(*) operator. *path creates a new array with all the items in original path and adds neighbor to it
                    # The splat operator is like destructuring in JS
                    q.enqueue(copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size():
            # Pop the first PATH
            path = s.pop()
            # Grab the vertex from the end of THE PATH
            last_vertex = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if last_vertex not in visited:
                # Mark it as visited
                visited.add(last_vertex)
                # Check if it is the target
                if last_vertex == destination_vertex:
                    # If so, return the path
                    return path
                # Push A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(last_vertex):
                    # Make a copy of the path
                    copy = path.copy()
                    # Add the neighbor to the copy
                    copy.append(neighbor)
                    # Enqueue the copy
                    s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = []
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        path_copy = path.copy()
        path_copy.append(starting_vertex)
        if destination_vertex in visited:
            return path_copy
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path:
                    return new_path
        return None

        # Alternate solution
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # if starting_vertex not in visited:
        #     visited.add(starting_vertex)
        #     path_copy = path.copy()
        #     path_copy.append(starting_vertex)
        #     if starting_vertex == destination_vertex:
        #         return path_copy
        #     for neighbor in self.get_neighbors(starting_vertex):
        #         new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
        #         if new_path is not None:
        #             return new_path
        # return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2) 
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    # graph.add_edge(4, 8)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
