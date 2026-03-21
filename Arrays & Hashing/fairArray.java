class Solution {
    public int waysToMakeFair(int[] nums) {
        // calculate prefix and suffix sum for odd and even
        // for i element in nums, evenSum = evenPrefix[i] + oddSufix[i]
        int[] evenPrefix = new int[nums.length];
        int[] oddPrefix = new int[nums.length];
        evenPrefix[0] = nums[0];
        oddPrefix[0] = 0;
        for (int arrIndex = 1; arrIndex < nums.length; arrIndex++) {
            if (arrIndex % 2 == 0) {
                evenPrefix[arrIndex] = evenPrefix[arrIndex - 1] + nums[arrIndex];
                oddPrefix[arrIndex] = oddPrefix[arrIndex-1];
            }
            else {
                oddPrefix[arrIndex] = oddPrefix[arrIndex - 1] + nums[arrIndex];
                evenPrefix[arrIndex] = evenPrefix[arrIndex-1];
            }
        }

        int[] evenSuffix = new int[nums.length];
        int[] oddSuffix = new int[nums.length];
        for (int arrIndex = nums.length - 1; arrIndex >= 0; arrIndex--) {
            if (arrIndex == nums.length - 1) {
                if (arrIndex % 2 == 0) {
                    evenSuffix[arrIndex] = nums[arrIndex];
                    oddSuffix[arrIndex] = 0;
                }
                else {
                    oddSuffix[arrIndex] = nums[arrIndex];
                    evenSuffix[arrIndex] = 0;
                }
            }
            else if (arrIndex % 2 == 0) {
                evenSuffix[arrIndex] = evenSuffix[arrIndex + 1] + nums[arrIndex];
                oddSuffix[arrIndex] = oddSuffix[arrIndex + 1];
            }
            else {
                oddSuffix[arrIndex] = oddSuffix[arrIndex + 1] + nums[arrIndex];
                evenSuffix[arrIndex] = evenSuffix[arrIndex + 1];
            }
        }

        int answer = 0;
        for (int numsIndex = 0; numsIndex < nums.length; numsIndex++) {
            int evenSumBefore = (numsIndex > 0) ? evenPrefix[numsIndex - 1] : 0;
            int oddSumBefore = (numsIndex > 0) ? oddPrefix[numsIndex - 1] : 0;

            int evenSumAfter = (numsIndex < nums.length - 1) ? evenSuffix[numsIndex + 1] : 0;
            int oddSumAfter = (numsIndex < nums.length - 1) ? oddSuffix[numsIndex + 1] : 0;

            int newEvenSum = evenSumBefore + oddSumAfter;
            int newOddSum = oddSumBefore + evenSumAfter;

            if (newEvenSum == newOddSum) {
                answer++;
            }
        }

        return answer;
    }
}