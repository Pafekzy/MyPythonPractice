def longest_increasing_subsequence(nums):
    if not nums:
        return []
    lis = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Length of longest increasing subsequence:", longest_increasing_subsequence(numbers))


