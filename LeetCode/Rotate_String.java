package LeetCode;
// https://leetcode.com/submissions/detail/484226344/
class Solution {
    public boolean rotateString(String A, String B) {
        if(A.length() != B.length()){
            return false;
        }
        return (A+A).contains(B);
    }
}