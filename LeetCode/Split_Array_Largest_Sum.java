// https://leetcode.com/problems/split-array-largest-sum/
class Solution {
    public int splitArray(int[] nums, int m) {
        int[] sum_array = new array[nums.length];
        sum_array[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            sum_array[i] = nums[i] + sum_array[i - 1];
        }
 
        
        int[][] min_largest_sum_dp = new int[nums.length][nums.length]; 
        for(int[] row : min_largest_sum_dp){
            Arrays.fill(row, sum_array[nums.length]);
        }

        for (int i = 0; i < nums.length; i++) {
            min_largest_sum_dp[i][0] = pfxSum[i];
        }
        
        for(int i = 0; i < nums.length; i++){
            for(int j = 1; j < Math.min(i + 1, m); j++){
                for(int k = 0; k < i; k++){
                    min_largest_sum_dp[i][j] = Math.min(
                        min_largest_sum_dp[i][j],
                        Math.max(min_largest_sum_dp[k][j - 1], pfxSum[i] - pfxSum[k])
                    );
                }
            }
        }
    }
}
