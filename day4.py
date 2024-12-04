def check_xmas(lines: list) -> int:
    count_total = 0
    height = len(lines)
    width = len(lines[0].strip())  # Strip to remove newline characters

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'X':
                # XMAS written left to right
                if x + 3 < width:  # Check boundary first
                    if lines[y][x+1] == 'M' and lines[y][x+2] == 'A' and lines[y][x+3] == 'S':
                        count_total += 1

                # XMAS written right to left
                if x - 3 >= 0:  # Check boundary first
                    if lines[y][x-1] == 'M' and lines[y][x-2] == 'A' and lines[y][x-3] == 'S':
                        count_total += 1

                # XMAS written down
                if y + 3 < height:  # Check boundary first
                    if lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
                        count_total += 1

                # XMAS written up
                if y - 3 >= 0:  # Check boundary first
                    if lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S':
                        count_total += 1

                # XMAS written down and right
                if y + 3 < height and x + 3 < width:  # Check both boundaries
                    if lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
                        count_total += 1

                # XMAS written up and right
                if y - 3 >= 0 and x + 3 < width:  # Check both boundaries
                    if lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
                        count_total += 1

                # XMAS written down and left
                if y + 3 < height and x - 3 >= 0:  # Check both boundaries
                    if lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
                        count_total += 1

                # XMAS written up and left
                if y - 3 >= 0 and x - 3 >= 0:  # Check both boundaries
                    if lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
                        count_total += 1

    return count_total


def check_xmas_optimized(lines: list) -> int:
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (-1, -1)  # up-left
    ]
    height = len(lines)
    width = len(lines[0].strip())
    total_count = 0
    
    lines = [line.strip() for line in lines]
    for y in range(height):
        for x in range(width):
            if lines[y][x] != 'X':
                continue
                
            for dy, dx in directions:
                positions = [(y + (i+1)*dy, x + (i+1)*dx) for i in range(3)]
                
                if any(not (0 <= ny < height and 0 <= nx < width) for ny, nx in positions):
                    continue
                
                if (lines[positions[0][0]][positions[0][1]] == 'M' and
                    lines[positions[1][0]][positions[1][1]] == 'A' and
                    lines[positions[2][0]][positions[2][1]] == 'S'):
                    total_count += 1

    return total_count


def check_x_mas(lines: list) -> int:
    count_total = 0

    height = len(lines)
    width = len(lines[0].strip())  # Strip to remove newline characters

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'A':
                # Check all 4 boundaries
                if y + 1 < height and x + 1 < width and y - 1 >= 0 and x - 1 >= 0:
                    # M S
                    #  A
                    # M S
                    if (lines[y-1][x-1] == 'M' and 
                        lines[y-1][x+1] == 'S' and
                        lines[y+1][x-1] == 'M' and
                        lines[y+1][x+1] == 'S'): 
                        count_total += 1

                    # S M
                    #  A
                    # S M
                    elif (lines[y-1][x-1] == 'S' and 
                        lines[y-1][x+1] == 'M' and
                        lines[y+1][x-1] == 'S' and
                        lines[y+1][x+1] == 'M'): 
                        count_total += 1

                    # S S
                    #  A
                    # M M
                    elif (lines[y-1][x-1] == 'S' and 
                        lines[y-1][x+1] == 'S' and
                        lines[y+1][x-1] == 'M' and
                        lines[y+1][x+1] == 'M'): 
                        count_total += 1

                    # M M
                    #  A
                    # S S
                    elif (lines[y-1][x-1] == 'M' and 
                        lines[y-1][x+1] == 'M' and
                        lines[y+1][x-1] == 'S' and
                        lines[y+1][x+1] == 'S'): 
                        count_total += 1

    return count_total


if __name__ == "__main__":
    lines = []
    xmas = 0
    with open("./input/day4.txt", "r", encoding="UTF-8") as file:
        for line in file:
            lines.append(line)

    print ("XMAS found: ", check_xmas(lines))
    print ("XMAS found (optimized): ", check_xmas_optimized(lines))
    print ("X-MAS found: ", check_x_mas(lines))
