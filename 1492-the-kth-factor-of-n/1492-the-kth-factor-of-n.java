class Solution {
    public int kthFactor(int n, int k) {
        // Initialize the count of factors to 0
        int count = 0;
        
        // Iterate from 1 to n
        for (int i = 1; i <= n; i++) {
            // If n is divisible by i, increment the count of factors
            if (n % i == 0) {
                count++;
                // If the count of factors is equal to k, return i
                if (count == k) {
                    return i;
                }
            }
        }
        
        // If the count of factors is less than k, return -1
        return -1;
    }
}