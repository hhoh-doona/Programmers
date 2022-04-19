
#정수삼각형
def solution(triangle):
    for level in range(len(triangle)-1, 0, -1):        
        addlist = []
        for i in range(0,len(triangle[level])-1):
            if (triangle[level][i] < triangle[level][i+1]):
                addlist.append(triangle[level][i+1])
            else:
                addlist.append(triangle[level][i])
                
        triangle[level-1] = [x+y for x,y in zip(triangle[level-1], addlist)]
    
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))