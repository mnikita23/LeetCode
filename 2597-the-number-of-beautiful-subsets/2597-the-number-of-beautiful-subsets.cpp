class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int res = 0;
        vector<bool> used(nums.size(), false);
        
        function<void(int, int)> dfs = [&](int idx, int prev) {
            res++;
            for (int i = idx; i < nums.size(); i++) {
                if (used[i] || (prev != -1 && abs(nums[i] - prev) == k)) continue;
                used[i] = true;
                dfs(i + 1, nums[i]);
                used[i] = false;
            }
        };
        
        dfs(0, -1);
        return res - 1; // subtract 1 for the empty subset
    }
};