"""
Simplest solution, use a stack of stacks if a dictorinary of frequencies.
https://leetcode.com/problems/maximum-frequency-stack/discuss/1862029/python-O(1)-solution-list-of-stacks
"""
from typing import List, Dict


class FreqStack:
    """
    The FreqStack will two lists, one where the numbers are stored in
    the stack, other list were we track the amount of each number of its
    position on the list, and a dictionary, where the indices of
    the positions of the numbers are located
    """

    def __init__(self):
        self.numbers_stack: List[int] = []
        self.amount_stack: List[Dict[int, int]] = [{}]
        self.indices: Dict[int, List[int]] = {}

    def __ammount_stack_append(self, val: int, index: int) -> None:
        val_amount = len(self.indices[val])

        prev_amount = val_amount - 1

        if val in self.amount_stack[prev_amount]:
            del self.amount_stack[prev_amount][val]

        if val_amount == len(self.amount_stack):
            self.amount_stack.append({})

        self.amount_stack[val_amount][val] = index

    def push(self, val: int) -> None:
        index = len(self.numbers_stack)
        self.numbers_stack.append(val)
        self.indices[val] = self.indices.get(val, []) + [index]
        self.__ammount_stack_append(val, index)

    def __get_near_top(self) -> int:
        max_index = -1
        max_val = -1

        for val, index in self.amount_stack[-1].items():
            if max_index < index:
                max_index = index
                max_val = val
        return max_val

    def __ammount_stack_pop(self, val: int) -> None:
        self.amount_stack[-1].pop(val)

        if not self.amount_stack[-1] and self.indices[val]:
            self.amount_stack.pop()
            self.amount_stack[-1][val] = self.indices[val][-1]

        elif self.indices[val]:
            self.amount_stack[-2][val] = self.indices[val][-1]

    def pop(self) -> int:
        val = self.__get_near_top()
        top_index = self.indices[val].pop()
        self.__ammount_stack_pop(val)
        return self.numbers_stack[top_index]




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
