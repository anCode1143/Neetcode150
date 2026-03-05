class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sum = 0;
        int[] diff = new int[gas.length];
        for (int index = 0; index < gas.length; index++) {
            sum += gas[index] - cost[index];
            diff[index] = gas[index] - cost[index];
        }
        if (sum < 0) {
            return -1;
        }
        int count = 0;
        int answer = 0;
        for (int index = 0; index < gas.length; index++) {
            count += diff[index];
            if (count < 0) {
                answer = index + 1;
                count = 0;
            }
        }
        return answer;
    }
}