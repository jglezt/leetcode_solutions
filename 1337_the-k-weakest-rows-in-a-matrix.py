# Use of heap is faster for bigger numbers

import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        total_numbers = []
        for i, row in enumerate(mat):
            heapq.heappush(total_numbers, (sum(row), i))

        return [heapq.heappop(total_numbers)[1] for _ in range(k)]
