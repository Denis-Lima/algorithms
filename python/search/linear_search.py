def linear_search(array: list, search_item):
    for index in range(len(array)):
        if array[index] == search_item:
            return index
    return -1


if __name__ == "__main__":
    import utils

    array = list(range(1_000_000))
    utils.test(array, linear_search)
