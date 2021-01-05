class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def is_palindrome(head: ListNode) -> bool:
        """
        Brute force method
        Time complexity: O(n)
        Space complexity: O(n)
        :param head:
        :return:
        """
        l = []
        while head:
            l += [head.val]
            head = head.next

        return l == l[::-1]
