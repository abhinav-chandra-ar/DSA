"""Given an array arr[] and an integer k, we need to calculate the maximum sum of a subarray having size exactly k.

Input  : arr[] = [5, 2, -1, 0, 3], k = 3
Output : 6
Explanation : We get maximum sum by considering the subaarray [5, 2 , -1]

Input  : arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
Output : 39
Explanation : We get maximum sum by adding subarray [4, 2, 10, 23] of size 4."""


def maxSum(arr, k):
    n = len(arr)

    if k > n :
        return -1
    
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)

    return max_sum

if __name__ == '__main__':
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(maxSum(arr, k))