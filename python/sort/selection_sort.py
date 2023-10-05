def selection_sort(array: list):
    sorted_array = []

    def find_minor(inner_array: list):
        minor = inner_array[0]
        for item in inner_array:
            if item < minor:
                minor = item
        return minor
