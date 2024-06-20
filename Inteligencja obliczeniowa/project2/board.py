BOARD = [
    [0, 0, 9, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 16],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 12, 0, 8, 0, 11, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [7, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 0],
]

CHROMOSOME_LENGTH = sum(sum(cell == 0 for cell in row) for row in BOARD)
INITIAL_SOLUTION = [0] * CHROMOSOME_LENGTH