from timeit import timeit


def test(array, search_func, max_execution=1):
    print("Results for:", search_func.__name__)

    def inner_test(item):
        result = []

        exec_time = timeit(
            lambda: result.append(search_func(array, item)), number=max_execution
        )
        return f"{result[0]:<10}| time for {max_execution} executions: {exec_time:.10f} sec"

    test_cases = [
        (0, 0),
        (-200, -1),
        (len(array) - 1, len(array) - 1),
        ((len(array) - 1) // 2, (len(array) - 1) // 2),
    ]
    for test_case, expected_index in test_cases:
        print(
            f"Search for item {test_case:<10}| expected index: {expected_index:<10}| got ",
            inner_test(test_case),
            sep="",
        )
