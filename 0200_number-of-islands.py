# We can treat each land mass as anode in the graph having as value
# the coordinates in the matrix, we build our graph by adding
# each connection vertically and horizontally. We run a BFS on each
# disconnected node to count the number of islands.

from typing import Set, List, Tuple, Deque
from collections import deque

class Solution:
    def find_land_masses(self, grid: List[List[str]]) -> Set:
        land_masses = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    land_masses.add((i, j))

        return land_masses

    def bfs(self, root: Tuple[int, int]) -> None:
        queue: Deque[Tuple[int, int]] = deque()
        queue.append(root)

        while queue:
            coordinate = queue.popleft()

            adjacents_coordinates = [
                (coordinate[0], coordinate[1] + 1),
                (coordinate[0], coordinate[1] - 1),
                (coordinate[0] + 1, coordinate[1]),
                (coordinate[0] - 1, coordinate[1]),
            ]

            for adjacent_coordinate in adjacents_coordinates:
                if adjacent_coordinate in self.land_masses:
                    self.land_masses.remove(adjacent_coordinate)
                    queue.append(adjacent_coordinate)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.land_masses = self.find_land_masses(grid)

        counter = 0

        while self.land_masses:
            self.bfs(self.land_masses.pop())
            counter += 1

        return counter
