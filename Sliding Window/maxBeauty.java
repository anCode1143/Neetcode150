import java.util.Arrays;

class maxBeauty {
    public int maximumBeauty(int[] nums, int k) {
        if (nums.length == 1) {
            return 1;
        }
        Arrays.sort(nums);
        int left = 0;
        int right = 0;
        int answer = 1;
        while (right < nums.length) {
            if (nums[right] - nums[left] <= 2*k) {
                right++;
                answer = Math.max(answer, right - left);
            } else {
                left++;
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        maxBeauty sol = new maxBeauty();  // Create an instance of your class
        int[] nums = {4, 6, 1, 2};
        int k = 2;
        
        System.out.println(sol.maximumBeauty(nums, k));
    }
}