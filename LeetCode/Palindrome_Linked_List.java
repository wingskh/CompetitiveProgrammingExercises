// https://leetcode.com/problems/palindrome-linked-list/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public static boolean isPalindrome(ListNode head) {
        ListNode middlePoint;
        if(head.next == null){
            return true;
        }else{
            middlePoint = findMiddlePoint(head);
        }
        
        ListNode prevPoint = null;
        while(middlePoint != null){
            ListNode temppoint = new ListNode(middlePoint.val);
            temppoint.next = prevPoint;
            middlePoint = middlePoint.next;
            prevPoint = temppoint;
        }
        
        while(prevPoint != null){
            if(prevPoint.val == head.val){
                prevPoint = prevPoint.next;
                head = head.next;
            }else{
                return false;
            }
        }
        return true;
    }
    
    static ListNode findMiddlePoint(ListNode head){
        ListNode slow = head;
        ListNode fast = head.next.next;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}