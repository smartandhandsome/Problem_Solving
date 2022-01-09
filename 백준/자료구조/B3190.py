N = int(input())
board = [[0] * N for _ in range(N)]
snake = [[0, 0]]
turn = {}
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
my_direction = 0

K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1

L = int(input())
for _ in range(L):
    X, C = input().split()
    turn[int(X)] = C

i = 0
j = 0
sec = 1

while True:
    i += direction[my_direction][0]
    j += direction[my_direction][1]

    if 0 <= i < N and 0 <= j < N and not ([i, j] in snake):
        snake.append([i, j])
        if board[i][j]:
            board[i][j] = 0
        else:
            snake.pop(0)

        if sec in turn.keys():
            if turn[sec] == 'L':
                my_direction = (my_direction - 1) % 4
            else:
                my_direction = (my_direction + 1) % 4
        sec += 1
    else:
        print(sec)
        break
