"""
If the total sum of the array does not equal to total sum of
non repeated numbers, Is guaranteed to have at least one repeated number
O(2N) ~= O(N)

I was trying to know if by summing the array, I could guess the
duplicated number

[1, 1]
Total without repetition equals to 3 - 1 -1 = 1
Total of the array 2
[2, 2]
Total of the array 4 3 -2 -2

3, 3, 3, 4, 2

Not possible, there is no guarantee that the numbers in range [1, n]
appear ordered.

The brute force solution is by searching for every number, a replicate
in the rest of the array.
If we did not were constrained to constant time, a hash map could be use
full to detect repeated numbers.


"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        past_rabit = 0

        rabit = nums[nums[0]]
        tortuise = nums[0]

        while True:
            rabit = nums[nums[rabit]]
            tortuise = nums[tortuise]

            if rabit == tortuise:
                current = 0
                while current != tortuise:
                    current = nums[current]
                    tortuise = nums[tortuise]

                return tortuise
