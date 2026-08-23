class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> unq;
        unq.insert(nums.begin(), nums.end());

        return unq.size() != nums.size();
    }
};