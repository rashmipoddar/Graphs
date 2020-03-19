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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
# print('room_graph: ', room_graph)
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def create_graph(player):
    vertices = {}
    reverse_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    visited = set()
    
    while len(vertices) < 500:
        current_room = player.current_room.name
        # print('Current room :', current_room)
        current_room_name = current_room.split(' ')[1]
        exits_available = player.current_room.get_exits()
        if current_room_name not in vertices:
            vertices[current_room_name] = {k:'?' for k in exits_available}
        move_direction = random.choice(exits_available)
        # print('Move Direction :', move_direction)
        traversal_path.append(move_direction)
        # print('Traversal path :', traversal_path)

        player.travel(move_direction)
        new_current_room = player.current_room.name
        # print('new_current_room after travelling ', new_current_room)
        new_current_room_name = new_current_room.split(' ')[1]
        new_exits_available = player.current_room.get_exits()
        if new_current_room_name not in vertices:
            vertices[new_current_room_name] = {k:'?' for k in new_exits_available}
        vertices[current_room_name][move_direction] = new_current_room_name
        vertices[new_current_room_name][reverse_direction[move_direction]] = current_room_name
        # print('Vertices: ', vertices)

create_graph(player)


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



def dft(player):
    s = Stack()
    s.push(starting_room)
    visited = set()
    while s.size():
        v = s.pop()
        if v not in visited:
            print(v)
            visited.add(v)
            for neighbor in self.get_neighbors(v):
                s.push(neighbor)




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
