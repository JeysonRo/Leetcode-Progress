class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> found;
        for(auto it = nums.begin(); it != nums.end(); ++it) 
        {
            if(found.count(*it) == 1)
            {
                return true;
            };
            found.insert(*it);
        };
        return false;
    };
};