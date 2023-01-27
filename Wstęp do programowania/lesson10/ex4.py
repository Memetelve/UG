# bubble sort
def bubble_sort(list):
    for _ in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort(['x']) == ['x']
    assert bubble_sort([1, 2, 2]) == [1, 2, 2]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort(['b', 'a']) == ['a', 'b']
