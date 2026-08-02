def solution(board):
    count = {'X': 0, 'O': 0, '.': 0}
    for i in range(3):
        for j in range(3):
            count[board[i][j]] += 1
    
    # print(count)
    if count['O'] - count['X'] not in [0, 1] :
        return 0
    
    def check_win(signal) : 
        for i in range(3) :
            if board[i][0] == signal and board[i][1] == signal and board[i][2] == signal:
                return True
            if board[0][i] == signal and board[1][i] == signal and board[2][i] == signal:
                return True
        
        if board[0][0] == signal and board[1][1] == signal and board[2][2] == signal :
            return True
        
        if board[0][2] == signal and board[1][1] == signal and board[2][0] == signal:
            return True
        
        return False
    
    x_win, o_win = check_win('X'), check_win('O')
    if x_win and o_win :
        return 0
    if o_win and count['O'] != 1 + count['X'] :
        return 0
    if x_win and count['O'] != count['X'] :
        return 0
    
    return 1