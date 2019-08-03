#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode(0)
        prev_node = result_node

        i = l1
        j = l2
        carry = 0
        while i is not None or j is not None:
            i_val = i.val if i is not None else 0
            j_val = j.val if j is not None else 0
            cur_val = carry + i_val + j_val
            carry, cur_val = divmod(cur_val, 10)

            cur_node = ListNode(cur_val)
            prev_node.next = cur_node

            if i is not None: i = i.next
            if j is not None: j = j.next

            prev_node = cur_node

        if carry > 0:
            prev_node.next = ListNode(carry)

        return result_node.next

def list_to_ListNode(list):
    head = ListNode(0)
    cur_node = head
    for i in list:
        cur_node.next = ListNode(i)
        cur_node = cur_node.next

    return head.next

def ListNode_to_list(list_node):
    node = list_node
    ret = []
    while node is not None:
        ret.append(node.val)
        node = node.next

    return ret

solution = Solution()
l1 = list_to_ListNode([2,4,3])
l2 = list_to_ListNode([5,6,4])

print(ListNode_to_list(solution.addTwoNumbers(l1, l2)))

