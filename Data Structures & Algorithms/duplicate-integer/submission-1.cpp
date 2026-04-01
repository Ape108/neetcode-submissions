class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> seen;
        for (const int& i : nums) {
            for (const int& j : seen) {
                if (i == j) {
                    return true;
                }
            }
            seen.push_back(i);
        }
        return false;
    }
};