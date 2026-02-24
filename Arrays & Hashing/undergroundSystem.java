import java.util.HashMap;

class UndergroundSystem {
    HashMap<Integer, String[]> travelling = new HashMap<>();
    HashMap<String, int[]> journeyInfo = new HashMap<>();
    
    public UndergroundSystem() {

    }
    
    public void checkIn(int id, String stationName, int t) {
        travelling.put(id, new String[] {stationName, String.valueOf(t)});
    }
    
    public void checkOut(int id, String stationName, int t) {
        String entrStation = travelling.get(id)[0];
        int entrTime = Integer.parseInt(travelling.get(id)[1]);
        if (journeyInfo.containsKey(entrStation+","+stationName)) {
            journeyInfo.get(entrStation+","+stationName)[0] += t - entrTime;
            journeyInfo.get(entrStation+","+stationName)[1]++;
        }
        else {journeyInfo.put(entrStation+","+stationName, new int[] {t - entrTime, 1});}
    }
    
    public double getAverageTime(String startStation, String endStation) {
        return (double) journeyInfo.get(startStation+","+endStation)[0] / journeyInfo.get(startStation+","+endStation)[1];
    }
}   