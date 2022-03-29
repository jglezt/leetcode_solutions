# DFS topological sort only works when the root is kwon
# Append to the queue after processing the tree down there
# Things that i have to look a lot should I take note.
# There is no root for a circular graph
# For thouse cases, the processed list is my ally
from typing import List, Dict
from collections import deque


class Solution:
    def build_graph(
        self, num_courses: int, prerequisites: List[List[int]]
    ) -> List[List[int]]:
        graph = [[] for _ in range(num_courses)]
        root = [True] * num_courses

        for (next_, pre) in prerequisites:
            graph[pre].append(next_)
            root[next_] = False

        print(graph, root)
        return graph, root

    def topological_sort(self, graph: List[List[int]], root: int) -> None:
        self.discovered[root] = True
        print(root)
        for next_course in graph[root]:

            if self.discovered[next_course] and not self.processed[next_course]:
                raise KeyError()

            if not self.discovered[next_course]:
                self.topological_sort(graph, next_course)

        self.queue.appendleft(root)
        self.processed[root] = True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, root = self.build_graph(numCourses, prerequisites)
        self.queue = deque()
        self.discovered = [False] * numCourses
        self.processed = [False] * numCourses

        for course, _ in enumerate(graph):
            if root[course] and not self.discovered[course]:
                try:
                    self.topological_sort(graph, course)
                except KeyError:
                    return []

        if not all(self.processed):
            return []
        return list(self.queue)
