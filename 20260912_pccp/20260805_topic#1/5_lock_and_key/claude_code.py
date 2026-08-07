def solution(key, lock):
    M = len(key)
    N = len(lock)
    board_size = N + 2 * (M - 1)
    # place lock in the center of an expanded board
    def make_board():
        board = [[0] * board_size for _ in range(board_size)]
        for i in range(N):
            for j in range(N):
                board[i + M - 1][j + M - 1] = lock[i][j]
        return board
    def rotate_90(k):
        # rotate M x M matrix 90 degrees clockwise
        return [[k[M - 1 - c][r] for c in range(M)] for r in range(M)]
    def check(board):
        # the original lock region must be filled with exactly 1s
        for i in range(M - 1, M - 1 + N):
            for j in range(M - 1, M - 1 + N):
                if board[i][j] != 1:
                    return False
        return True

    current_key = key
    for _ in range(4):
        current_key = rotate_90(current_key)
        board = make_board()

        for x in range(board_size - M + 1):
            for y in range(board_size - M + 1):
                # place key
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] += current_key[i][j]

                if check(board):
                    return True

                # remove key (undo)
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] -= current_key[i][j]

    return False
