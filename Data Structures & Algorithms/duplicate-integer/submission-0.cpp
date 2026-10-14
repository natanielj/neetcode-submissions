class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int>b;
        bool res;
        for (int i : nums) {
            for (int j : b) {
                if (i == j) {
                    res = true;
                }
            }
            b.push_back(i);
        }
        if (res == true) {
            return true;
        } else {
            return false;
        }
    }
};
