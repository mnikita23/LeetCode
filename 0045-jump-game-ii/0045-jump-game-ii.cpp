class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        int max_reach = 0;
        int end = 0;
        
        for (int i = 0; i < nums.size() - 1; i++) {
            max_reach = max(max_reach, i + nums[i]);
            
            if (i == end) {
                jumps++;
                end = max_reach;
            }
        }
        
        return jumps;
    }
};
