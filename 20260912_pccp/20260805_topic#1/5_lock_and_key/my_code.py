def solution(key, lock):
    M, N = len(key), len(lock)
    size = M + N + M # put the lock in the center of board 
    board = [[0] * size for _ in range(size)]
    for i in range(M, M + N):
        for j in range(M, M + N):
            board[i][j] = lock[i - M][j - M]
    
    def rotate(key):
        rotated_key = [[0] * M for _ in range(M)]
        for row in range(M):
            for col in range(M): 
                rotated_key[row][col] = key[col][M - 1 - row]
        return rotated_key
    
    def check_lock():
        # check if all cell of the lock is not empty (0) and not duplicate cell (2)
        for i in range(M, M + N):
            for j in range(M, M + N):
                if board[i][j] != 1:
                    return False
        return True
    
    for times in range(4):
        
        for i in range(size - M + 1):
            for j in range(size - M + 1):
                
                # try to apply every cell of key to an empty cell of lock
                for x in range(M):
                    for y in range(M):
                        board[x + i][y + j] += key[x][y]
                
                    
                if check_lock():
                    return True
        
                # remove key
                for x in range(M):
                    for y in range(M):
                        board[x + i][y + j] -= key[x][y]
        
        key = rotate(key)
    
    return False