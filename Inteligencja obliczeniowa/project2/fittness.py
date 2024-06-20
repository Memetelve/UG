import numpy

from board import BOARD


def combine_board_and_solution(board, solution):

    new_board = [row.copy() for row in board]
    solution = solution.copy()

    if isinstance(solution, numpy.ndarray):
        solution = solution.tolist()

    new_board = [row.copy() for row in new_board]
    for row in range(len(new_board)):
        for col in range(len(new_board[row])):
            if new_board[row][col] == 0:
                new_board[row][col] = solution.pop(0)

    return new_board


def check_visible_from(x, y, board):

    if board[y][x] <= 0:
        raise ValueError("Wrong visibility cell check")

    horizontal_visible = 0
    vertical_visible = 0

    for y1 in range((len(board))):

        if board[y1][x] == -1:
            if y1 < y:
                vertical_visible = 0
                continue
            elif y1 > y:
                break
            else:
                raise ValueError("Invalid board state")

        vertical_visible += 1

    for x1 in range((len(board[y]))):

        if board[y][x1] == -1:
            if x1 < x:
                horizontal_visible = 0
                continue
            elif x1 > x:
                break
            else:
                raise ValueError("Invalid board state")

        horizontal_visible += 1

    return vertical_visible + horizontal_visible - 1


class Fittness:

    board = BOARD

    @staticmethod
    def complicated(a, solution, b):
        board = combine_board_and_solution(Fittness.board, solution)
        score = 0

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell > 0:
                    cell_score = check_visible_from(x, y, board)
                    if cell_score != cell:
                        score -= abs(cell - cell_score)
                    else:
                        score += cell
        return score

    @staticmethod
    def simple(a, solution, b):
        board = combine_board_and_solution(Fittness.board, solution)
        score = 0

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell > 0:
                    cell_score = check_visible_from(x, y, board)
                    if cell_score == cell:
                        score += 1
        return score

    @staticmethod
    def swarm(solutions):
        results = []

        for sol in solutions:
            int_sol = [int(round(i, 0)) for i in sol]
            results.append(-1 * Fittness.complicated(0, int_sol, 0))

        return results

    @staticmethod
    def change_board(new_board):
        Fittness.board = new_board
