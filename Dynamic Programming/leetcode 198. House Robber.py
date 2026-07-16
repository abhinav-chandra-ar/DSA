def rob(nums):

    n = len(nums)
    if n == 0:
        return 0 
    if n == 1:
        return nums[n]
    if n == 2:
        return max(nums[0], nums[1])
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2,n):
        
        curr = max(prev1 , prev2 + nums[i])
        prev2 = prev1
        prev1 = curr

    return prev1

if __name__ == '__main__' :

    nums = list(map(int, input("Enter the treasure in adjacent Houses : ").split()))
    print(f'The maximum value of tresure is : {rob(nums)}')