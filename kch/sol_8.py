def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        for line in board:
            if (line[move - 1] != 0):
                stack.append(line[-1])

                if(len(stack) > 1):
                    if (stack[-2] == stack[-1]):
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                
                line[move-1] = 0
                break

    return answer

print(solution([[0, 0, 0, 0, 0],[0, 0, 1, 0, 3],[0, 2, 5, 0, 1],[4, 2, 4, 4, 2],[3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))