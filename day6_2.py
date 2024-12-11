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


def update_map(map: list, x: int, y: int, new_value: str) -> list:
    row = list(map[x])  # Convert the row to a list of characters
    row[y] = new_value  # Update the character at the specified position
    map[x] = ''.join(row)  # Convert the list of characters back to a string
    return map

def move_guard(map: list, location: list, direction: Direction) -> (list, bool):
    x = location[0]
    y = location[1]
    guard_on_map = True
    

    if direction == Direction.UP and x-1 >= 0:
        if map[x-1][y] == ".":
            update_map(map, x, y, ".")
            update_map(map, x-1, y, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    elif direction == Direction.DOWN and x+1 < len(map):
        if map[x+1][y] == ".":
            update_map(map, x, y, ".")
            update_map(map, x+1, y, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    elif direction == Direction.LEFT and y-1 >= 0:
        if map[x][y-1] == ".":
            update_map(map, x, y, ".")
            update_map(map, x, y-1, direction.value)
        else:
            map, guard_on_map = move_guard(map, location, turn_right(direction))
    elif direction == Direction.RIGHT and y+1 < len(map[x]):
        if map[x][y+1] == ".":
            update_map(map, x, y, ".")
            update_map(map, x, y+1, direction.value)
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
    with open("input/day6_test.txt") as file:
        map = []
        locations_visited = []

        for line in file:
            map.append(line.strip())

    successful_loops = 0
    guard_left_map = 0
    # Loop through each position on the map
    for i in range(len(map)):
        for j in range(len(map[i])):
            map_test = map.copy()
            if map_test[i][j] != ".":
                continue
            else:
                map_test = update_map(map_test, i, j, "#")

                guard_on_map = True
                while guard_on_map:
                    # print_map(map, guard_on_map, locations_visited)
                    x, y, direction, guard_on_map = locate_guard(map_test)
                    location =[x, y]
                    if location is not None:
                        locations_visited.append(location)
                        map_test, guard_on_map = move_guard(map_test, location, direction)
                    
                    # Check if there are 2 duplicates in the locations_visited list
                    if len(unique_locations(locations_visited)) <= 2:
                        print(f"Obstacle at {x},{y}: The guard is in a loop.")
                        successful_loops += 1
                guard_left_map += 1    
                print(f"The guard has left the map: {guard_left_map}")
    print(f"Total, successful loops: {successful_loops}")
