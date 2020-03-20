from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
print('room_graph: ', room_graph)
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def create_graph(player):
    vertices = {}
    visited = {}
    reverse_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    # while len(vertices) < 9:
    current_room = player.current_room.name.split(' ')[1]
    exits_available = player.current_room.get_exits()
    if current_room not in vertices:
        vertices[current_room] = {k:'?' for k in exits_available}
    if current_room not in visited:
        visited[current_room] = set()
    move_direction = random.choice(exits_available)
    print('Move direction :', move_direction)
    print('Visited :', visited)
    if move_direction not in visited[current_room]:
        visited[current_room].add(move_direction)
        player.travel(move_direction)
        traversal_path.append(move_direction)
        print('Traversal path', traversal_path)
        new_available_exits = player.current_room.get_exits()
        print('New available exits', new_available_exits)
        while move_direction in new_available_exits:
            print('inside the while loop')
            player.travel(move_direction)
            traversal_path.append(move_direction)
            print(traversal_path)
            new_current_room = player.current_room.name.split(' ')[1]
            new_available_exits = player.current_room.get_exits()
        print('exited out of while loop')
    print(visited)

def dft(direction, player):
    graph = room_graph
    exits = player.current_room.get_exits()
    s = Stack()
    starting_room = int(player.current_room.name.split(' ')[1])
    s.push([starting_room])
    # print('Stack', s.stack)
    visited = set()
    while s.size() > 0:
        room_path = s.pop()
        print('Path', room_path)
        room = room_path[-1]
        if room not in visited:
            # print('Room', room)
            visited.add(room)
            print('Room ', room)
            graph_for_neighbors = room_graph[int(room)][1]
            print(graph_for_neighbors)
            neighbor_values = graph_for_neighbors.values()
            for val in neighbor_values:
                copy = room_path.copy()
                copy.append(val)
                s.push(copy)


    print(visited)

# def get_neighbors(room, player):
#     reverse_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
#     neighbors = {}
#     neighbors[room] = {}
#     exits = player.current_room.get_exits()
#     if len(exits) > 0:
#         for direction in exits:
#             player.travel(direction)
#             current_room = player.current_room.name.split(' ')[1]
#             neighbors[room][direction] = current_room  
#             player.travel(reverse_direction[direction])
#     # print('Neighbors', neighbors)
#     return neighbors

dft('e', player)

def bfs(starting_room, target_room):
    q = Queue()
    q.enqueue([starting_room])
    visited = set()
    while q.size():
        path = q.dequeue()
        last_vertex = path[-1]
        if last_vertex not in visited:
            visited.add(last_vertex)
            if last_vertex == destination_vertex:
                return path
            for neighbor in get_neighbors(last_vertex):
                copy = path.copy()
                copy.append(neighbor)
                q.enqueue(copy)


# def create_graph(player):
#     vertices = {}
#     reverse_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
#     visited = set()

#     while len(vertices) < 9:
#         current_room = player.current_room.name
#         # print('Current room :', current_room)
#         current_room_name = current_room.split(' ')[1]
#         exits_available = player.current_room.get_exits()
#         if current_room_name not in vertices:
#             vertices[current_room_name] = {k:'?' for k in exits_available}
#         move_direction = random.choice(exits_available)
#         # print('Move Direction :', move_direction)
#         traversal_path.append(move_direction)
#         # print('Traversal path :', traversal_path)

#         player.travel(move_direction)
#         new_current_room = player.current_room.name
#         # print('new_current_room after travelling ', new_current_room)
#         new_current_room_name = new_current_room.split(' ')[1]
#         new_exits_available = player.current_room.get_exits()
#         if new_current_room_name not in vertices:
#             vertices[new_current_room_name] = {k:'?' for k in new_exits_available}
#         vertices[current_room_name][move_direction] = new_current_room_name
#         vertices[new_current_room_name][reverse_direction[move_direction]] = current_room_name
#         # print('Vertices: ', vertices)

# create_graph(player)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
