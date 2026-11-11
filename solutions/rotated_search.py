"""Search in Rotated Sorted Array (LeetCode 33). Identify the sorted half before shrinking the search range."""

class Solution:

    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
