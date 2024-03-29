
def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120