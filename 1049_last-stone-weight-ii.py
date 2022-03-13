"""
Code solution for laststoneweightii
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def dp(index: int, total: int) -> int:
            if index == len(stones) - 1:
                return min(total + stones[index], total - stones[index])

            return min(dp(index + 1, total + stones[index]),
                       dp(index + 1, total - stones[index]))

        return sum(stones) - abs(dp(0, 0))
