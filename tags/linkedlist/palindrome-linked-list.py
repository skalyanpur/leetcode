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

    @staticmethod
    def is_palindrome_smart(head: ListNode) -> bool:
        """

        :param head:
        :return:
        """
        rev = None
        slow, fast = head, head
        while head and head.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev
