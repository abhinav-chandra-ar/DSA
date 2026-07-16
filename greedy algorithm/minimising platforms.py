def minimisePlatforms(arr,dep):
    arr = sorted(arr)
    dep = sorted(dep)

    i = 0
    j = 0

    platform = 0
    maxplatform = 0

    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platform += 1
            i += 1
            maxplatform = max(maxplatform, platform)

        else :
            platform -= 1
            j -= 1

    return maxplatform

if __name__ == '__main__':
    arr = list(map(int, input("Enter arrival time : ").split()))
    dep = list(map(int,input("Enter the departure time : ").split()))

    print(f'Maximum platforms are : {minimisePlatforms(arr,dep)}')