# Solve for a single boat
# Find the maximum amount of people we can fit in a boat
#
# We can not reduce the problem to fitting the highest amount of people
#

# Occupie the boat the most, the problem is in regards to not leaving space
# free on each boat. Doing that, we make the best use of the inventory

# Piking a single value and searching for the complement
# Trough using hash maps, or using a two pointer apporuch
# The second one seams that is n^2, we will loop through the
# Greedy approuch, use the biggest number
# (3, 3) (5, 2) (2)
# Using the smallest number
# (2, 2, 3) (3) (5)
# (1, 1) (2) (2)
# Usu
# (5, 2)

# use the two pointer technique to get the heaviest persons in the boat
# intialize the two pointers at the beginning of the array.
from typing import List

class BestMemorySolution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        total = 0
        index = 0
        while people:
            first_people = people.pop() # people =[2, 2, 2, 3] reminder = 3

            while index >= 0 and people:
                if first_people + people[index] > limit:
                    index -= 1
                else:
                    people.pop(index)
                    break
            if index < 0:
                index = 0

            total += 1

        return total


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        total = 0
        start = 0
        end = len(people) - 1
        while start <= end:
            first_people = people[end]

            if start < end and not first_people + people[start] > limit:
                start += 1

            end -= 1

            total += 1

        return total
