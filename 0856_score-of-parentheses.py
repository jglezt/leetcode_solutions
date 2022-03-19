"""
# I do not know to sole this problem
# But I think I can first know to detect if the string is a balanced
parentheses
# By using a stack, I create
# I can detect when each parentheses closes, but how can I detect if
it is nested
# Adding a flag in a second stack. Since is guaranteed that the
parenthesis closes. No better yet. We can add the operation in the
stack in the following order.

# If a parentheses closes inmediatly, that is, if the previous character
# was a opening parentheses, add 1

# The idea should be, to calculate as soon as a parentheses that encloses
# an operation is found. For example
(()())() The first enclosing parenthesis can be transalated as follows


as soon as the parentheses that closes the `2 *` operation closes, we
perform the operation up to the first 2 that we found.

Thus, the loop is as follows

1. Translate the parenthesis to numbers

If char = ( and char + 1 = (
append *
else if char = ( and char + 1 = )
append 1
else if char = ) and char - 1 = )

2. Sum all the numbers up to the first `*`

3. Continue up until the string empties.

4. Sum the left overs, if any.

"""


from typing import List, Union

STOP = "*"


class Solution:
    """
    Solution
    """
    @staticmethod
    def __sum_up_to_first_multiplication(
        stack: List[Union[str, int]]
    ) -> List[Union[str, int]]:
        current_item: Union[str, int] = stack.pop()
        total: int = 0
        while current_item != STOP:
            total += current_item
            current_item = stack.pop()

        total *= 2
        stack.append(total)
        return stack

    def scoreOfParentheses(self, s: str) -> int:
        operation_stack: List[Union[str, int]] = []

        for i, char in enumerate(s):
            if char == "(" and s[i + 1] == "(":
                operation_stack.append(STOP)
            elif char == "(" and s[i + 1] == ")":
                operation_stack.append(1)
            elif char == ")" and s[i - 1] == ")":
                operation_stack = Solution.__sum_up_to_first_multiplication(
                    operation_stack
                )

        return sum(operation_stack)
