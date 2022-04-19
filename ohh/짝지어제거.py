
#짝지어 제거하기
def solution(s):
    stack = []
    for ch in s:
        top = ''
        if len(stack) > 0:
            top=stack[-1]    
            
        if (top == ch):
            stack.pop()
        else:
            stack.append(ch)
        
    if len(stack) == 0:
        return 1
    return 0

print(solution('baabaa'))