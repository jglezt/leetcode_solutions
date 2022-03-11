# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Find the tail of the linked list, and capture the size of it.
# Keep a pointer to the head
# Find the position of the new head by adding k to the size of the list.
# Move up to the position in the list that refers the head,
# Put a None in node.next and return the temp value holding next.
from typing import Tuple
class Solution:
    def find_tail(self, head: ListNode) -> Tuple[int, ListNode]:
        next_: ListNode = head.next
        node: ListNode = head
        total: int = 1
        while next_:
            node = next_
            next_ = next_.next
            total += 1

        return total, node

    def find_new_head(self, head: ListNode,
                           pos: int) -> ListNode:
        tail: ListNode = head
        head: ListNode = head.next

        for _ in range(pos - 1):
            tail = head
            head = head.next

        tail.next = None
        return head

    def rotateRight(self,
                    head: Optional[ListNode],
                    k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        list_size, tail = self.find_tail(head)

        # Make it a circular list
        tail.next = head

        new_head_index_reverse: int = (
            - ((list_size + k) % list_size)
        )

        new_head_index: int = list_size + new_head_index_reverse

        if not new_head_index or new_head_index == list_size:
            tail.next = None
            return head

        new_head: ListNode = self.find_new_head(
            head,
            new_head_index
        )

        return new_head
