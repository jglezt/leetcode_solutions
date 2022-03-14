"""# Separate the string by slashes
# Create a queue
# Loop trhoug the list of directories found by the split
# Follow the next rules.
If '.', ignore and move with the next element.
If '..' ignore the string and the next one.
Else, add left to the queue
"""
from typing import List
from collections import deque


class Solution:
    """
    Solution
    """

    def simplifyPath(self, path: str) -> str:
        """
        Solution function
        """
        tokens: List[str] = path.split("/")

        index: int = -1
        queue: deque = deque()
        ignore_counter: int = 0

        while index >= -len(tokens):
            token: str = tokens[index]

            if token == "..":
                ignore_counter += 1
            elif token not in (".", ""):
                if ignore_counter:
                    ignore_counter -= 1
                else:
                    queue.appendleft(token)

            index -= 1

        return f"/{'/'.join(queue)}"
