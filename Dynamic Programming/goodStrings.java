class GoodStrings {
    public int solution(int low, int high, int zero, int one) {
        long[] dp = new long[high + 1];
        dp[0] = 1;
        for (int index = 0; index < dp.length; index++) {
            if (index + zero < dp.length) dp[index + zero] = (dp[index + zero] + dp[index]) % 1_000_000_007;
            if (index + one < dp.length) dp[index + one] = (dp[index + one] + dp[index]) % 1_000_000_007;
        }
        long answer = 0;
        for (int i = low; i <= high; i++) {
            answer = (answer + dp[i]) % 1_000_000_007;
        }
        return (int) answer;
    }
}