using System;
using System.Collections.Generic;
using System.IO;

class Solution {

    static int solveMeFirst(int a, int b) { 
      int total = a + b;
      return total;
    }

    static void Main(String[] args) {
        int val1 = Convert.ToInt32(Console.ReadLine());
        int val2 = Convert.ToInt32(Console.ReadLine());
        int sum = solveMeFirst(val1,val2);
        Console.WriteLine(sum);
    }
}      
