"""Trapping Rain Water (LeetCode 42). Compare a monotonic stack with a two-pointer scan."""

class StackSolution:

    def trap(self, height: list[int]) -> int:
        stack = []
        size = len(height)
        ans = 0
        for i in range(size):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)
                if stack:
                    left = stack[-1]
                    right = i
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ans += (right - left - 1) * high
                else:
                    break
            stack.append(i)
        return ans

class TwoPointerSolution:

    def trap(self, height: list[int]) -> int:
        ans = 0
        left, right = (0, len(height) - 1)
        leftMax = rightMax = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
