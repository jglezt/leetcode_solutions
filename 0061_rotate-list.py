# Definition for singly-linked list.

# Find the tail of the linked list, and capture the size of it.
# Keep a pointer to the head
# Find the position of the new head by adding k to the size of the list.
# Move up to the position in the list that refers the head,
# Put a None in node.next and return the temp value holding next.
from typing import Tuple, Optional


class ListNode:
    def __init__(self, val=0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution
    """
    @staticmethod
    def __find_tail(head: ListNode) -> Tuple[int, ListNode]:
        next_: ListNode = head.next
        node: ListNode = head
        total: int = 1
        while next_:
            node = next_
            next_ = next_.next
            total += 1

        return total, node

    @staticmethod
    def __find_new_head(head: ListNode, pos: int) -> ListNode:
        tail: ListNode = head
        head_: ListNode = head.next

        for _ in range(pos - 1):
            tail = head_
            head = head_.next

        tail.next = None
        return head

    def rotate_right(self,
                     head: Optional[ListNode], k: int
                     ) -> Optional[ListNode]:
        """Solution"""
        if not head or not head.next:
            return head

        list_size, tail = self.__find_tail(head)

        # Make it a circular list
        tail.next = head

        new_head_index_reverse: int = -((list_size + k) % list_size)

        new_head_index: int = list_size + new_head_index_reverse

        if not new_head_index or new_head_index == list_size:
            tail.next = None
            return head

        new_head: ListNode = self.__find_new_head(head, new_head_index)

        return new_head
