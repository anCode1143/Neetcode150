import java.util.HashSet;
import java.util.Set;

public class countIfVowel {
    public int[] vowelStrings(String[] words, int[][] queries) {
    // indexIsVowel = {}
    // for query in queries:
    //  for index in range(query[0], query[1]+1):
    //       if indexIsVowel[index]: queryAnswer += 1
        HashSet<Character> vowels = new HashSet<>(Set.of('a', 'e', 'i', 'o', 'u'));
        int[] prefixCount = new int[words.length];

        if (vowels.contains(words[0].charAt(0)) && 
        vowels.contains(words[0].charAt(words[0].length() - 1))) {
            prefixCount[0] = 1;
        }
        else {
            prefixCount[0] = 0;
        }

        for (int wordIndex = 1; wordIndex < words.length; wordIndex++) {
            if (vowels.contains(words[wordIndex].charAt(0)) && 
            vowels.contains(words[wordIndex].charAt(words[wordIndex].length() - 1))) {
                prefixCount[wordIndex] = prefixCount[wordIndex-1] + 1;
            }
            else {
                prefixCount[wordIndex] = prefixCount[wordIndex-1];
            }
        }

        int[] answer = new int[queries.length];
        for (int queryIndex = 0; queryIndex < queries.length; queryIndex++) {
            int queryCount = 0;
            if (queries[queryIndex][0] == 0) {
                queryCount = prefixCount[queries[queryIndex][1]];
            }
            else {
                queryCount = prefixCount[queries[queryIndex][1]] - prefixCount[queries[queryIndex][0]-1];
            }
            answer[queryIndex] = queryCount;
        }
        return answer;
    
    }
}
