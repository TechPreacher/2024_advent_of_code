
def check_rules(page_row: list, rules: list) -> (bool, list):
    page_no = len(page_row)
    print (f"Analyzing page row: {page_row}")
    for  i in range(page_no):
        for rule in rules:
            if page_row[i] == rule[0]:
                x = i
                while x >= 0:
                    if page_row[x] == rule[1]:
                        print(f"  Rule violated: {rule}. Page: {page_row[i]}, rule: {rule}")
                        return False, rule
                    x -= 1 
            if page_row[i] == rule[1]:
                x = i
                while x < page_no:
                    if page_row[x] == rule[0]:
                        print(f"  Rule violated: {rule}. Page: {page_row[i]}, rule: {rule}")
                        return False, rule
                    x += 1
    print(f"  Pages: {page_row}, no violation")
    return True, None


def get_center_page(page_row) -> int:
    center_page = page_row[int((len(page_row) ) / 2)]
    print(f"    Center page: {center_page}")
    return center_page


def swap_bad_pages(page_row: list, rule: list) -> list:
    fixed_page_row = []
    counter = 0
    while counter < len(page_row):
        if page_row[counter] == rule[1]:
            # Swap the pages
            fixed_page_row.append(page_row[counter+1])
            fixed_page_row.append(page_row[counter])
            counter += 1
        else:
            # No swap needed
            fixed_page_row.append(page_row[counter])
        counter += 1
    print(f"    Swapped page row: {fixed_page_row}")
    return fixed_page_row


if __name__ == "__main__":
    with open("input/day5_test.txt", "r", encoding="UTF-8") as file:
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

    center_page_sum = 0
    for page_row in page_rows:
        valid, rule = check_rules(page_row, rules)
        if valid:
            center_page_sum += get_center_page(page_row)
        else:
            new_page_row = page_row.copy()
            is_fixed = False
            while not is_fixed:
                new_page_row = swap_bad_pages(new_page_row, rule)
                is_fixed, rule = check_rules(new_page_row, rules)
            print(f"      Fixed page row: {new_page_row}")
            center_page = get_center_page(new_page_row)
            center_page_sum += center_page
        print(f"Center Page Sum: {center_page_sum}")
