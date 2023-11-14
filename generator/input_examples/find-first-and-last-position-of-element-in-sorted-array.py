def searchRange(nums, target):
    def binarySearchLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
    
    def binarySearchRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or nums[right] != target:
            return -1
        return right

    left_idx = binarySearchLeft(nums, target)
    right_idx = binarySearchRight(nums, target)
    return [left_idx, right_idx]
