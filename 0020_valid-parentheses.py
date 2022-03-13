# Usign a stack, push the parenthesis that open
# If a parenthesis that closes appears, check if the top of the
# stack has the correct opening parenthesis
from typing import List, Dict

class ParenthesisStack:
    def __init__(self) -> None:
        # To make the stack return false when a closing parameters is found
        # in an empty stack
        self.__list: List = [""]

    def __push(self, parenthesis: str) -> None:
        self.__list.append(parenthesis)

    def __len__(self) -> int:
        return len(self.__list)

    def __pop(self) -> str:
        return self.__list.pop()

    def __call__(self, parentheis: str) -> bool:
        types_parenthesis: Dict = {")": "(", "}": "{", "]": "["}
        if parentheis in types_parenthesis:
            return self.__pop() == types_parenthesis[parentheis]
        self.__push(parentheis)
        is_pushing = True
        return is_pushing

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ParenthesisStack()
        for parenthesis in s:
            if not stack(parenthesis):
                return False

        return len(stack) == 1
