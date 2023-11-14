def maxSlidingWindow(nums, k):
    output = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        output.append(max(window))
    return output
