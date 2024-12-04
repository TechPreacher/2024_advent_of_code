import re

def capture_do(string: str) -> str:
    result = []
    capturing = True  # Flag to track when to start capturing
    i = 0  # Index for traversing the string

    while i < len(string):
        if string[i:i+4] == "do()":  # Check for "do()"
            capturing = True
            i += 3  # Skip past "do()"
        elif string[i:i+7] == "don't()":  # Check for "don't()"
            capturing = False
            i += 6  # Skip past "don't()"
        elif capturing:
            result.append(string[i])

        i += 1
    
    return ''.join(result)


if __name__ == "__main__":
    pattern = r"mul\((\d+),(\d+)\)"
    total = 0

    with open("./input/day3.txt", "r", encoding="UTF-8") as file:
        for line in file:
            matches = re.findall(pattern, line)
            for match in matches:
                num1, num2 = map(int, match)
                total += num1 * num2

    print(f"Total: {total}")

    total = 0
    with open("./input/day3.txt", "r", encoding="UTF-8") as file:
        for line in file:
            line = capture_do(line)
            matches = re.findall(pattern, line)
            for match in matches:
                num1, num2 = map(int, match)
                total += num1 * num2

    print(f"Total: {total}")