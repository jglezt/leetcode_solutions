"""
"""
from typing import Tuple, Dict, Optional


class Node:
    "# Definition for a Node."

    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    # 1. My first idea is to create ah hash map with the memory address
    # of the old linked list as key
    # 2. Populate the hash map through a while loop, adding
    # a new entry with the mem location of the new node.
    # 3. Give another pass to populate the random linked list
    # using the hash map
    # Complexity O(2N) -> O(N)
    """

    @staticmethod
    def __copy_linked_list(head: "Node") -> Tuple["Node", Dict[int, "Node"]]:
        node: "Node" = head
        new_node: "Node" = Node(node.val)
        new_head: "Node" = new_node
        memory_reference: Dict = {id(node): new_node}

        while node.next:
            new_node.next = Node(node.next.val)

            new_node = new_node.next
            node = node.next
            memory_reference[id(node)] = new_node

        return new_head, memory_reference

    @staticmethod
    def __populate_random_pointer(
        head: "Node", new_head: "Node", memory_reference: Dict[int, "Node"]
    ) -> None:
        node: "Node" = head
        new_node: "Node" = new_head
        while node:
            if node.random:
                random_new_node = memory_reference[id(node.random)]
            else:
                random_new_node = None
            new_node.random = random_new_node

            new_node = new_node.next
            node = node.next

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Function to call when solution
        """
        if not head:
            return head
        new_head, memory_reference = Solution.__copy_linked_list(head)

        Solution.__populate_random_pointer(head, new_head, memory_reference)

        return new_head
