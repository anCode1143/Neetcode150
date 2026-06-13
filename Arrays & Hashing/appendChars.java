class Solution {
    public int appendCharacters(String s, String t) {
        // index keeps track of t while iterating through s
        // if t[index] == s[iterator], index++
        // return len(t) - index
        int tIndex = 0;
        for (int sIndex = 0; sIndex < s.length(); sIndex++) {
            if (s.charAt(sIndex) == t.charAt(tIndex)) {
                tIndex++;
            }
            if (tIndex == t.length()) return 0;
        }
        return t.length() - tIndex;
    }
}