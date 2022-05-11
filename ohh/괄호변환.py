def isCorrGawl(u):
    temp =0
    
    for str in u:
        if str == "(":
            temp +=1
        else:
            temp -=1
            
        if temp < 0:
            return False;
        
    return True

def divGawl(p):
    temp = 0
    
    for i in range(0,len(p)):
        if p[i] == "(":
            temp +=1
        else:
            temp -=1
        
        if temp == 0:
            break
    
    return p[0:i+1], p[i+1:]

def trimAndRevers(u):
    temp = u.replace(")","1").replace("(","2")
    temp = temp.replace("1","(").replace("2",")")
    return temp[1:-1]

def solution(p):
    
    if p == "": return ""
    
    u, v = divGawl(p)
    
    if isCorrGawl(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + trimAndRevers(u)
    
        
print(solution("()))((()"))