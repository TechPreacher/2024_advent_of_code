from collections import defaultdict


def find_order(numbers, rules):
    # Create a graph representation
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for all numbers
    for num in numbers:
        in_degree[num] = 0
    
    # Build the graph and calculate in-degrees
    for first, second in rules:
        if first in numbers and second in numbers:
            graph[first].append(second)
            in_degree[second] += 1
    
    # Find numbers with no dependencies
    stack = [n for n in numbers if in_degree[n] == 0]
    result = []
    
    while stack:
        current = stack.pop()
        result.append(current)
        
        # Update neighbors
        for neighbor in graph[current]:
            if neighbor in numbers:  # Only process numbers in our list
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
    
    # If we couldn't order all numbers, return None
    return result if len(result) == len(numbers) else None


def verify_order(order, rules):
    if not order:
        return False
    
    # Check each rule
    for first, second in rules:
        if first in order and second in order:
            if order.index(first) > order.index(second):
                return False
    return True


def get_center_page(page_row) -> int:
    center_page = page_row[int((len(page_row) ) / 2)]
    return center_page


if __name__ == "__main__":
    with open("input/day5.txt", "r", encoding="UTF-8") as file:
        lines = []
        rules_raw = []
        rules = []
        page_rows_raw = []
        page_rows = []

        for line in file:
            lines.append(line)
          # Split the list
        for line in lines:
            if line in ["", "\n"]:
                break
            rules_raw.append(line.strip())
        for line in lines:
            if line in ["", "\n"] or "|" in line:
                continue
            page_rows_raw.append(line.strip())

    for rule_raw in rules_raw:
        rules.append( [int(x) for x in rule_raw.split("|")])

    for page_row in page_rows_raw:
        # Convert CSV sting to list of integers
        page_rows.append( [int(x) for x in page_row.split(",")])

    print(f"Rules: {rules}")
    print(f"Page Rows: {page_rows}")

    center_pages = 0

    for page_row in page_rows:
        print(f"\nPage Row: {page_row}")
        if verify_order(page_row, rules):
            print("Page is in order. Not processing.\n")
        else:
            result = find_order(page_row, rules)
            
            print(f"Found ordering: {result}")
            
            if result:
                is_valid = verify_order(result, rules)
                print(f"Order is {'valid' if is_valid else 'invalid'}")
                
                if is_valid:
                    center_page = get_center_page(result)
                    print(f"Center page: {center_page}\n")
                    center_pages += center_page
                else:
                    print("\nRule violations:\n")
                    for first, second in rules:
                        if first in result and second in result:
                            if result.index(first) > result.index(second):
                                print(f"{first} should come before {second}\n")
                                break
            else:
                print("\nNo valid ordering found\n")
                break
    
    print (f"Sum of center pages: {center_pages}")


