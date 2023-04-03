with open("input.txt", "r+") as fh:
    file = fh.read()
    input_values = file.strip().split("\n")
    input_values = [int(x) for x in input_values]


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        arr = heapify(arr, n, largest)

    return arr


# def heapify_iter(arr, n, i):
#     largest = i
#     while True:
#         l = 2 * i + 1
#         r = 2 * i + 2

#         if l < n and arr[i] < arr[l]:
#             largest = l

#         if r < n and arr[largest] < arr[r]:
#             largest = r

#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             i = largest
#         else:
#             break

#     return arr


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        arr = heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arr = heapify(arr, i, 0)

    return arr


result = heapSort(input_values)

with open("output.txt", "w+") as fh:
    result = [str(x) for x in result]
    fh.write("\n".join(result))
