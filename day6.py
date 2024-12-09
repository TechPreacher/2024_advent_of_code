from enum import Enum
import time


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


def turn_right(direction: Direction) -> Direction:
    if direction == Direction.UP:
        return Direction.RIGHT
    elif direction == Direction.DOWN:
        return Direction.LEFT
    elif direction == Direction.LEFT:
        return Direction.UP
    elif direction == Direction.RIGHT:
        return Direction.DOWN


def locate_guard(map: list) -> (int, int, Direction, bool):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in [Direction.UP.value, Direction.DOWN.value, Direction.LEFT.value, Direction.RIGHT.value]:
                return i, j, Direction(map[i][j]), True
    return None, None, None, False


def unique_locations(locations_visited: list) -> list:
    # Assuming locations_visited is a list of tuples (x, y)
    unique_locations = []
    seen = []
    for location in locations_visited:
        if location not in seen:
            unique_locations.append(location)
        seen.append(location)
    locations_visited = unique_locations
    return locations_visited


def move_guard(map: list, location: list, direction: Direction) -> (list, bool):
    x = location[0]
    y = location[1]
    guard_on_map = True
    
    def update_map(x, y, new_value):
        row = list(map[x])  # Convert the row to a list of characters
        row[y] = new_value  # Update the character at the specified position
        map[x] = ''.join(row)  # Convert the list of characters back to a string

    if direction == Direction.UP and x-1 >= 0:
        if map[x-1][y] == ".":
            update_map(x, y, ".")
            update_map(x-1, y, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    elif direction == Direction.DOWN and x+1 < len(map):
        if map[x+1][y] == ".":
            update_map(x, y, ".")
            update_map(x+1, y, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    elif direction == Direction.LEFT and y-1 >= 0:
        if map[x][y-1] == ".":
            update_map(x, y, ".")
            update_map(x, y-1, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    elif direction == Direction.RIGHT and y+1 < len(map[x]):
        if map[x][y+1] == ".":
            update_map(x, y, ".")
            update_map(x, y+1, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    else:
        guard_on_map = False

    return map, guard_on_map


def print_map(map: list, guard_on_map: bool, locations_visited: list):
    for line in map:
        print(line)
    
    print("\nGuard on map:", guard_on_map)
    print("Unique Locations visited:", len(unique_locations(locations_visited)))
    # Wait 0.2 seconds
    time.sleep(0.2)


if __name__ == "__main__":
    # Populate the map
    with open("input/day6.txt") as file:
        map = []
        locations_visited = []

        for line in file:
            map.append(line.strip())

    guard_on_map = True
    while guard_on_map:
        # print_map(map, guard_on_map, locations_visited)
        x, y, direction, guard_on_map = locate_guard(map)
        location =[x, y]
        if location is not None:
            locations_visited.append(location)
            map, guard_on_map = move_guard(map, location, direction)
    
    print("The guard has left the map.")
    print("Places visited: ", len(unique_locations(locations_visited)))
