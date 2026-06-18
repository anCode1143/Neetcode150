class MinSteps {
    public long solution(String s) {
        int left = 0;
        while (s.charAt(left) == '0') {
            left++;
            if (left == s.length()) return 0;
        }
        int right = left;
        long answer = 0;
        while (right < s.length()) {
            while (s.charAt(right) != '0') {
                right++;
                if (right == s.length()) return answer;
            }
            answer += right - left;
            left++; right++;
        }
        return answer;
    }
}