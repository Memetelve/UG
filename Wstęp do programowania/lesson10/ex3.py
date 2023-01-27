
def is_sorted(list):  # sourcery skip: use-next
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def test_is_sorted():
    assert is_sorted([])
    assert is_sorted(['x'])
    assert is_sorted([1, 2, 2])
    assert is_sorted([3, 2, 1])
    assert not is_sorted(['b', 'a'])