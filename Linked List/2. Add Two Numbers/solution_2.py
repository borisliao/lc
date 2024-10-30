# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list = []

        def addToList(ln: ListNode, list: 'list'):
            list.append(ln.val)
            if (ln.next):
                addToList(ln.next, list)

        addToList(self, list)

        return str(list)

    def __repr__(self) -> str:
        return f"{self}"

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    result = ListNode()
    head = result
    carry = 0

    while l1 or l2 or carry:
        if l1:
            n1 = l1.val
            l1 = l1.next
        else:
            n1 = 0

        if l2:
            n2 = l2.val
            l2 = l2.next
        else:
            n2 = 0

        if carry:
            c = carry
            carry = 0
        else:
            c = 0

        nodeResult = n1 + n2 + c

        if nodeResult > 9:
            carry = nodeResult // 10
            nodeResult -= 10

        result.next = ListNode(nodeResult, None)
        result = result.next

    return head.next


def review1(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Anki 12-6-23
    Used: Debugger (5)
    Time: 15:02
    Against the spirit of the problem, solved using string manipulation
    """
    l1_num = ''
    while l1 and l1.val != None:  # d1
        l1_num += str(l1.val)
        l1 = l1.next

    l2_num = ''
    while l2 and l2.val != None:  # d1, d2
        l2_num += str(l2.val)  # d3
        l2 = l2.next

    result = str(int(l1_num[::-1]) + int(l2_num[::-1]))[::-1]  # d4

    result_node = ListNode()
    result_start = result_node
    for r in result:
        result_node.next = ListNode(val=int(r))  # d4, # d5
        result_node = result_node.next  # d4

    return result_start.next


def review2(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Anki 12-6-23
    Time: 34 min
    Used: debugger (5)
    """

    node = ListNode()
    result = node

    carry = 0

    while l1 != None or l2 != None or carry:
        v1 = l1.val if l1 and l1.val != None else 0  # d2 "l1 and"
        v2 = l2.val if l2 and l2.val != None else 0  # d2 "l2 and"
        l1 = l1.next if l1 else None  # d1, d3
        l2 = l2.next if l2 else None  # d1, d3, d4 used l1 instead of l2

        sum = v1 + v2
        value = (sum + carry) % 10  # d5 (sum + carry)
        carry = (sum + carry) // 10  # d5 (sum + carry)

        node.next = ListNode(val=value)
        node = node.next

    return result.next


def review3(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Anki 12-11-23
    Time: 29:30
    Used: Debugger (2)
    """
    dummy = ListNode()
    node = dummy
    carry = 0

    while l1 or l2 or carry:  # d2
        v1 = l1.val if l1 else 0  # d1
        v2 = l2.val if l2 else 0  # d1

        sum = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10
        node.next = ListNode(sum)
        node = node.next
        l1 = l1.next if l1 else None  # d1
        l2 = l2.next if l2 else None  # d1

    return dummy.next


def review4(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Anki 12-21-23
    Used: debugger 1
    Time: 13:08
    """

    head = ListNode()  # d1
    dummy = head
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        sum = v1+v2+carry
        remainder = sum % 10
        carry = sum // 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        dummy.next = ListNode(remainder)
        dummy = dummy.next

    return head.next  # d1


def review5(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Anki 1-9-24
    Time: 20 min
    Used debugger 2
    """
    dummy = ListNode()
    result = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = (carry + val1 + val2) % 10
        carry = (carry + val1 + val2) // 10

        dummy.next = ListNode(total)
        l1 = l1.next if l1 else None  # d1, d2 if l1 else None
        l2 = l2.next if l2 else None  # d1, d2 if l2 else None
        dummy = dummy.next  # d1

    return result.next


def review6(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Mochi 4-15-24
    """
    dummy = ListNode()
    node = dummy
    carry = 0
    while l1 or l2 or carry:  # s1 or carry
        l = l1.val if l1 else 0
        r = l2.val if l2 else 0

        sum = (l+r+carry) % 10
        carry = (l+r+carry) // 10
        node.next = ListNode(sum)
        node = node.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


def review7(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Mochi 10-29-24
    """
    dummy = ListNode()
    node = dummy

    carry = 0

    while l1 or l2 or carry:
        l = r = 0
        if l1:
            l = l1.val
            l1 = l1.next
        if l2:
            r = l2.val
            l2 = l2.next

        val = (l+r+carry) % 10
        carry = (l+r+carry)//10

        node.next = ListNode(val)
        node = node.next

    return dummy.next
