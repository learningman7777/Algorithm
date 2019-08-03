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
        over = False
        while i is not None:
            cur_node = ListNode(i.val)
            prev_node.next = cur_node

            if over:
                cur_node.val += 1
                over = False

            if j is not None:
                cur_node.val += j.val
                j = j.next

            if cur_node.val >= 10:
                over = True
                cur_node.val = cur_node.val % 10

            i = i.next
            prev_node = cur_node

        while j is not None:
            cur_node = ListNode(j.val)
            prev_node.next = cur_node

            if over:
                cur_node.val += 1
                over = False

            if cur_node.val >= 10:
                over = True
                cur_node.val = cur_node.val % 10

            j = j.next
            prev_node = cur_node

        if i is None and j is None and over == True:
            cur_node = ListNode(1)
            prev_node.next = cur_node

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

