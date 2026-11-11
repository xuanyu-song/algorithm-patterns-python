"""Rotting Oranges (LeetCode 994). Start BFS from all sources and track time in layers."""

import collections


class Solution:

    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = (len(grid), len(grid[0]))
        queue = collections.deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        if fresh_count == 0:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < m and 0 <= ny < n and (grid[nx][ny] == 1):
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
            if queue:
                minutes += 1
        return minutes if fresh_count == 0 else -1
