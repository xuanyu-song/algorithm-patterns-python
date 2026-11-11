"""Course Schedule (LeetCode 207). Remove zero-indegree nodes and count how many were processed."""

import collections

class Solution:

    def topologicalSorting(self, numCourses, graph):
        indegrees = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        while S:
            u = S.pop()
            numCourses -= 1
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    S.append(v)
        if numCourses == 0:
            return True
        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        for v, u in prerequisites:
            graph[u].append(v)
        return self.topologicalSorting(numCourses, graph)
