# The problem can be solved by solving smaller problems
# Recurrence
# Minimum path sum [level] = min(level_i + level - 1_i, level_i + level-1_i-1)
# Minimum path sum [0] = level_0

# If level 0, return the element there, since is
# minum sum path

# Otherwise, return the minimum of either path [level - 1][i] or path [level - 1][ i - 1]
from typing import List, Union
from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> Union[int, float]:
        """
        Called function to evaluate solution
        """
        top: int = 0
        @lru_cache(None)
        def dp(level: int, index: int) -> Union[int, float]:
            """
            Recursive dp algorithm
            """
            if level == top:
                return triangle[top][0]
            if index >= len(triangle[level]) or index < 0:
                return float("inf")

            current_element = triangle[level][index]

            return min(current_element + dp(level - 1, index),
                       current_element + dp(level - 1, index - 1))

        return min([dp(len(triangle) - 1, index)
                    for index in range(len(triangle[-1]))])
