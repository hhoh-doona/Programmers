def solution(arr) :
    total = 0
    for i in range(len(arr)) :
        total += arr[i]
    return total / len(arr)


print(solution([1,3,5]))