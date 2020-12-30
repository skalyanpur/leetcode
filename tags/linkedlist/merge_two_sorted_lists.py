"""
Leetcode problem: https://leetcode.com/problems/merge-two-sorted-lists/
Values in the linked lists are sorted
l1 = [1, 2, 4]
l2 = [1, 3, 4]

output = [1, 1, 2, 3, 4, 4]
"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"val: {self.val} next: {self.next}"


class Solution(object):
    @staticmethod
    def merge_two_sorted_lists(l1: Node, l2: Node) -> Node:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = Solution.merge_two_sorted_lists(l1.next, l2)
        return l1 or l2


if __name__ == '__main__':
    a, a.next = Node(1), Node(3)
    b = Node(1)
    node = Solution.merge_two_sorted_lists(a, b)
    values = []
    while node:
        values.append(str(node.val))
        node = node.next

    print("-".join(values))
