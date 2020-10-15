# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3493/
# For Checking Purpose
def print_linked_list(head):
    sol_sorted_list = []
    while head != None:
        sol_sorted_list.append(head.val)
        head = head.next
    print(sol_sorted_list)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            left_center_node = self.find_the_center(head)
            right_center_node = left_center_node.next
            left_center_node.next = None

            left_nodes_head = self.sortList(head)
            right_nodes_head = self.sortList(right_center_node)
            result = self.merge_sort(left_nodes_head, right_nodes_head)
        return result

    def find_the_center(self, head):
        one_step_pointer = head
        two_step_pointer = head

        while two_step_pointer.next != None and two_step_pointer.next.next != None:
            one_step_pointer = one_step_pointer.next
            two_step_pointer = two_step_pointer.next.next

        return one_step_pointer

    def merge_sort(self, left_sorted_head, right_sorted_head):
        if left_sorted_head == None:
            return right_sorted_head
        if right_sorted_head == None:
            return left_sorted_head

        if left_sorted_head.val <= right_sorted_head.val:
            result = left_sorted_head
            result.next = self.merge_sort(left_sorted_head.next, right_sorted_head)
        else:
            result = right_sorted_head
            result.next = self.merge_sort(left_sorted_head, right_sorted_head.next)
        return result



test_list = ListNode(val=4, next=ListNode(val=2))
test_val_list = [-1,5,3,4,0]
list_node_list = []
for i in test_val_list:
    list_node_list.append(ListNode(val=i))

test_head = None
previous = None
for node in list_node_list:
    if test_head == None:
        test_head = node
        previous = test_head
    else:
        previous.next = node
        previous = node

print_linked_list(test_head)
sol = Solution()
sol_head = sol.sortList(test_head)
print_linked_list(sol_head)
