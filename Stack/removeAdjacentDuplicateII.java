import java.util.Stack;

class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<String[]> stack = new Stack<>();
        for (int index = 0; index < s.length(); index++) {
            char currChar = s.charAt(index);
            if (stack.size() == 0) {
                stack.push(new String[] {String.valueOf(currChar), "1"});
                continue;
            }
            String[] prev = stack.peek();
            if (currChar == prev[0].charAt(0)) {
                stack.push(new String[] {prev[0], String.valueOf(Integer.parseInt(prev[1])+1)});
                if (Integer.parseInt(prev[1]) + 1 == k) {
                    for (int i = 0;  i < k; i++) {
                        stack.pop();
                    }
                }
            }
            else stack.push(new String[] {String.valueOf(currChar), "1"});
        }
        StringBuilder currString = new StringBuilder();
        for (int index = 0; index < stack.size(); index++) {
            char currChar = stack.get(index)[0].charAt(0);
            currString.append(currChar);
        }
        String answer = currString.toString();
        return answer;
    }
}