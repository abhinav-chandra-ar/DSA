memo = {}
def memoFib(n):
    if n in memo :
        return memo[n]
    
    if n == 1:
        return 0

    if n == 2:
        return 1
    
    result = memoFib(n-1) + memoFib(n-2)
    memo[n] = result

    return result

def tabFib(n):

    if n == 1:
        return 0

    if n == 2:
        return 1
    
    fib = [0] * n
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2,n):
        fib[i] = fib[i-1] + fib[i-2]

    return fib

if __name__ ==  '__main__' :
    n = int(input())

    for i in range(1, n + 1):
        print(memoFib(i), end=" ")
    
    print('\r')

    print(*tabFib(n))