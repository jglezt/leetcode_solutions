from typing import List

NOT_EXISTS = -1


class Solution:
    @staticmethod
    def binary_search(nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = int(start + (end - start) / 2)

            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                return middle

        return NOT_EXISTS

    def search(self, nums: List[int], target: int) -> int:
        return Solution.binary_search(nums, target)
