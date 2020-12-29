class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def __init__(self, ):
        pass

    # 243
    # 564
    # 708 (answer)
    @staticmethod
    def add_two_numbers(l1: Node, l2: Node) -> Node:
        dummy = Node(0)
        current, carry = dummy, 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.value
                l1 = l1.next
            if l2:
                val2 = l2.value
                l2 = l2.next

            carry, val = divmod(val1 + val2 + carry, 10)
            current.next = Node(val)
            current = current.next

        return dummy.next


if __name__ == '__main__':
    a, a.next, a.next.next = Node(2), Node(4), Node(3)
    b, b.next, b.next.next = Node(5), Node(6), Node(4),
    answer = Solution.add_two_numbers(a, b)
    result = "{0}-{1}-{2}".format(answer.value, answer.next.value, answer.next.next.value)
    print(result)
