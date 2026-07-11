memo = {}
def memoCount(n):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    result = memoCount(n-1) + memoCount(n-2)
    memo[n] = result
    return result

def tabCount(n):
    if n <= 2:
        return n
    
    tab = [0] * n
    tab[0] = 1
    tab[1] = 2

    for i in range(2,n):
        tab[i] = tab[i-1] + tab[i-2]

    return tab[n-1]

if __name__ == '__main__':
    n = int(input("Enter the number of stairs : "))

    print(memoCount(n), '\n' ,tabCount(n))
    


