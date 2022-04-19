def solution(numbers):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = []

    for i in num:
        if i not in numbers:
            ans.append(i)
    
    return sum(ans)
    
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))