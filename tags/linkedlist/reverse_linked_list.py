class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"val: {self.val} - Node: {self.next}"


class Solution:

    @staticmethod
    def reverse_linked_list(head: Node) -> Node:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev


if __name__ == '__main__':
    l1 = [1, 2, 3]
    head = curr = Node(l1[0])
    for i in range(1, len(l1)):
        curr.next = Node(l1[i])
        curr = curr.next

    print(head)
    print(Solution.reverse_linked_list(head))
