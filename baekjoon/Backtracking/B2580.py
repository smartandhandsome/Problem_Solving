import sys

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def search(x, y):
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s -= set(sudoku[x])
    s -= set(sudoku[i][y] for i in range(9))
    s -= set(sudoku[i][j] for j in range((y // 3) * 3, (y // 3) * 3 + 3) for i in range((x // 3) * 3, (x // 3) * 3 + 3))
    return tuple(s)


def solve(index):
    if len(zeros) == index:
        for sdk in sudoku:
            print(*sdk)
        sys.exit(0)

    i, j = zeros[index]
    candidate = search(i, j)
    for can in candidate:
        sudoku[i][j] = can
        solve(index + 1)
        sudoku[i][j] = 0


solve(0)
