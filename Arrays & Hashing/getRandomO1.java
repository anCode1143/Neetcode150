import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

class RandomizedSet {
    ArrayList<Integer> list = new ArrayList<>();
    HashMap<Integer, Integer> valueToIndex = new HashMap<>();

    public RandomizedSet() {
        
    }
    
    public boolean insert(int val) {
        if (!valueToIndex.containsKey(val)) {
            list.add(val);
            valueToIndex.put(val, list.size()-1);
            return true;
        }
        else {
            return false;
        }
    }
    
    public boolean remove(int val) {
        if (valueToIndex.containsKey(val)) {
            int valIndex = valueToIndex.get(val);
            int lastVal = list.get(list.size()-1);
            list.set(valIndex, lastVal);
            valueToIndex.put(lastVal, valIndex);
            valueToIndex.remove(val);
            list.remove(list.size() - 1);
            return true;
        }
        else {
            return false;
        }
    }
    
    public int getRandom() {
        Random rand = new Random();
        return list.get(rand.nextInt(list.size()));
    }
}