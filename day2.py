def calculate_safe(number_line: list, is_dampened: bool = False) -> (bool, str):
    is_increasing = None
    is_safe = True
    dampened = None

    for i in range(len(number_line)):
        current_value = number_line[i]
        next_value = -1 if i == len(number_line) - 1 else number_line[i + 1]

        if not is_safe:
            if not is_dampened:
                is_dampened = True
                dampened = None
                for j in range(len(number_line)):
                    try_number_line = number_line.copy()
                    try_number_line.pop(j)
                    is_safe_try, _ = calculate_safe(try_number_line, is_dampened)

                    if is_safe_try:
                        dampened = number_line[j]
                        is_safe = True
                        break

                return is_safe, dampened
            
        if not is_safe:
            continue

        if next_value == -1:
            continue
                
        if i == 0:
            if current_value < next_value:
                is_increasing = True
            elif current_value > next_value:
                is_increasing = False
            else:
                is_safe = False
                continue

        if current_value == next_value:
            is_safe = False
            continue

        if is_increasing and current_value > next_value:
            is_safe = False
            continue

        if not is_increasing and current_value < next_value:
            is_safe = False
            continue

        if abs(current_value - next_value) > 3:
            is_safe = False
            continue 

    return is_safe, dampened


if __name__ == "__main__":
    number_line_list = []
    safe_measures = 0
    lines_processed = 0
    
    with open("./input/day2.txt", "r", encoding="UTF-8") as file:
        for line in file:
            number_line = list(map(int, line.split()))
            number_line_list.append(number_line)

    for number_line in number_line_list:
        lines_processed += 1
        is_safe, dampened = calculate_safe(number_line, False)
        if is_safe:
            safe_measures += 1
        print(f"{lines_processed} number line {number_line} is safe: {is_safe}. Dampened: {dampened}")

    print("Total safe number lines: ", safe_measures)
