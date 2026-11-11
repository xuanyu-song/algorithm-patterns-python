"""Sliding Window Maximum (LeetCode 239). Compare lazy heap eviction with a monotonic deque."""

from collections import deque
import heapq

class HeapSolution:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        size = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, size):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res


def max_sliding_window_deque(nums: list[int], k: int) -> list[int]:
    """Return maxima for all complete windows, keeping candidate indices in a deque."""
    candidates = deque()
    maxima = []
    for index, value in enumerate(nums):
        if candidates and candidates[0] <= index - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index >= k - 1:
            maxima.append(nums[candidates[0]])
    return maxima
