#나머지가 1이 되는 수 찾기
def prime_list(n):
    sieve = [True] * n
    
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


def solution(n):
    listPrime = prime_list(1000000)
    for i in listPrime:
        if n % i == 1:return i
    
    return 0

print(solution(10))