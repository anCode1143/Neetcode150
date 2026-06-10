class validPartitiontion {
    public boolean solution(int[] nums) {
        boolean[] dp = new boolean[nums.length + 1];
        dp[0] = true;
        for (int index = 1; index < dp.length; index++) {
            if (index >= 2 && nums[index - 1] == nums[index - 2]) {
                dp[index] = dp[index-2];
            }
            if (index >= 3 && nums[index - 1] == nums[index - 2] && nums[index - 2] == nums[index - 3]) {
                dp[index] = dp[index] || dp[index-3];
            }
            if (index >= 3 && nums[index - 1] == nums[index - 2]+1 && nums[index-2] == nums[index-3]+1) {
                dp[index] = dp[index] || dp[index-3];
            }
        }
        return dp[dp.length - 1];
    }
}