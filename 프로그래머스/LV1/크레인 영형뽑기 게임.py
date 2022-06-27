def solution(board, moves):
    answer = 0
    size = len(board)
    basket = []
    board_stack = [[] for i in range(size)]
    
    for i in range(size):
        for j in range(size):
            if board[size-i-1][j] != 0:
                board_stack[j].append(board[size-i-1][j])
    
    for move in moves:
        if board_stack[move-1]:
            grap = board_stack[move-1].pop()
            
            if basket:
                if basket[-1] == grap:
                    answer += 2
                    basket.pop()
                    continue
                    
            basket.append(grap)
    
    return answer