def binary_search(sorted_list, item):
    low_index = 0
    high_index = len(sorted_list) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        guess = sorted_list[mid_index]
        if guess == item:
            return mid_index
        if guess > item:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return None

if __name__ == "__main__":
    test_list = [1, 3, 5, 7, 9]
    print(f"List: {test_list}")
    
    # Test cases
    targets = [3, -1, 9, 1, 10]
    for target in targets:
        result = binary_search(test_list, target)
        print(f"Searching for {target}: Found at index {result}")