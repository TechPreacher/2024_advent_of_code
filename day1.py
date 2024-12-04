def sort_list(list: list) -> list:
    return sorted(list)  # Remove the key parameter to sort strings lexicographically


def get_distance(int1: int, int2: int) -> int:
    return abs(int1 - int2)


def calculate_similarity_score(value1: int, list2: list) -> int:
    return list2.count(value1) * value1


if __name__ == "__main__":
    list1 = []
    list2 = []
    distances = []
    similarity_scores = []

    with open("./input/day_01_1.txt", "r", encoding="UTF-8") as file:
        for line in file:
            list1.append(int(line[:5]))
            list2.append(int(line[8:13]))

    sorted_list1 = sort_list(list1)
    sorted_list2 = sort_list(list2)

    for i in range(len(sorted_list1)):
        distance = get_distance(sorted_list1[i], sorted_list2[i])
        print(f"Dataset {i}: distance between {sorted_list1[i]} and {sorted_list2[i]} is {distance}")
        distances.append(distance)

    print("Total distance: ", sum(distances))

    for i in range(len(sorted_list1)):
        similarity_score = calculate_similarity_score(sorted_list1[i], sorted_list2)
        print(f"Dataset {i}: similarity score between {sorted_list1[i]} and sorted_list2 is {similarity_score}")
        similarity_scores.append(similarity_score)

    print("Total similarity score: ", sum(similarity_scores))