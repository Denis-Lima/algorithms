from timeit import timeit


def binary_search(array: list, search_item):
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index) // 2
        item = array[middle_index]
        if item == search_item:
            return middle_index
        if item < search_item:
            low_index = middle_index + 1
        else:
            high_index = middle_index - 1
    return -1


if __name__ == "__main__":
    import utils

    array = list(range(1_000_000))
    utils.test(array, binary_search)
