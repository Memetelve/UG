import pytest

def is_triangle_possible(x, y, z):
    if x + y <= z:
        return False
    if x + z <= y:
        return False
    if y + z <= x:
        return False
    return True


@pytest.mark.parametrize("test_input,expected", [((1, 2, 3), False), ((4, 5, 6), True), ((10, 10, 11), True)])
def test_triangle_possible(test_input, expected):
    assert is_triangle_possible(*test_input) == expected
