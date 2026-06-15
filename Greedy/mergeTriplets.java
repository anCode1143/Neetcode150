class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int[] answer = new int[3];
        for (int triplet = 0; triplet < triplets.length; triplet++) {
            if (triplets[triplet][0] <= target[0] && 
                triplets[triplet][1] <= target[1] && 
                triplets[triplet][2] <= target[2]) {
                answer[0] = Math.max(triplets[triplet][0], answer[0]);
                answer[1] = Math.max(triplets[triplet][1], answer[1]);
                answer[2] = Math.max(triplets[triplet][2], answer[2]);
                }
        }
        if (answer[0] == target[0] && answer[1] == target[1] && answer[2] == target[2]) return true;
        else return false;
    }
}