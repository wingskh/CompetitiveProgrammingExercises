# https://leetcode.com/problems/sort-list/
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
