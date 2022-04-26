def solution(board, moves):
    answer = 0
    
    rlist = []
    
    board = list(zip(*board))
    
    for idx in range(len(board)):
        board[idx] = [i for i in board[idx] if i != 0]

    for i in [j-1 for j in moves]:
        if len(board[i]) == 0:
            continue
        
        sel = board[i].pop(0)
        
        if len(rlist) !=0 and rlist[-1] == sel:
            rlist.pop(-1)
            answer +=1
        else:
            rlist.append(sel)
        
    return answer * 2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))