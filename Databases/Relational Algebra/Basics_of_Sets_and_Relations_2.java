import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Set<Integer> set_A = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        Set<Integer> set_B = new HashSet<>(Arrays.asList(2, 3, 4, 5, 6, 7, 8));
        Set<Integer> set_C = new HashSet<>();
        for (Integer number : set_A) {
            if (set_B.contains(number)) {
                set_C.add(number);
            }
        }
        
        System.out.print(set_C.size());
    }
}