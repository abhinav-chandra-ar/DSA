def costStair(cost):
    n = len(cost)
    if n <= 2:
        return min(cost)
    
    mincost = [0] * n
    mincost[0] = cost[0]
    mincost[1] = cost[1]

    for i in range(2,n):
        mincost[i] = min(mincost[i-1],mincost[i-2]) + cost[i]

    return min(mincost[n-1],mincost[n-2])

if __name__ == '__main__':
    cost = list(map(int, input("Enter the cost of n stairs : ").split()))
    print(costStair(cost))