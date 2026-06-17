import java.util.ArrayDeque;
import java.util.Deque;

class StockSpanner {
     Deque<int[]> stack = new ArrayDeque<>(); // [price, span]

    public StockSpanner() {

    }
    
    public int next(int price) {
        int span = 1;
        while (stack.size() > 0 && stack.peek()[0] <= price) {
            span = stack.peek()[1] + span;
            stack.pop();
        }
        stack.push(new int[] {price, span});
        return stack.peek()[1];
    }
}