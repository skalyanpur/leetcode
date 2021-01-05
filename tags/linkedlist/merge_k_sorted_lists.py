from heapq import heapify, heappush, nsmallest
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def merge_k_sorted_list(lists: List[ListNode]) -> Optional[ListNode]:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapify(heap)
        for node in lists:
            while node:
                val = node.val
                node = node.next
                heappush(heap, val)

        dummy = ListNode()
        current = dummy

        for val in nsmallest(len(heap), heap):
            current.next = ListNode(val)
            current = current.next

        return dummy.next
