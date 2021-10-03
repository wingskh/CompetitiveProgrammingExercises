// https://leetcode.com/problems/non-decreasing-array/
class Solution {
    public boolean checkPossibility(int[] nums) {
        boolean changed = false;

        for (int i = 0; i < nums.length-1; i++) {
            if(nums[i+1] != nums[i]){
                if(nums[i] > nums[i+1]){
                    if(changed){
                        return false;
                    }
                    changed = true;

                    if(i-1<0 || nums[i-1] <= nums[i+1]){
                        // 1, 5, 3, 4
                        // 1, 3, 3, 4
                        nums[i] = nums[i+1];
                    }else{
                        // 5, 7, 1, 8
                        // 5, 7, 7, 8
                        nums[i+1] = nums[i];
                    }
                }
            }
        }
        return true;
    }
}