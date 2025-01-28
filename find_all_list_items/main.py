def find_all_list_items(iterable, value):
    result = []
    for i, item in enumerate(iterable):
        if isinstance(item, list):
            for j in find_all_list_items(item, value):
                result.append([i] + j)
        elif item == value:
            result.append([i])
    return result
            

if __name__ == "__main__":
    assert find_all_list_items([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2) == [[0, 0, 1], [0, 1], [1, 1]]