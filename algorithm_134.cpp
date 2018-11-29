class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        for(int i = 0; i < gas.size(); i++)
        {
            gas[i] -= cost[i];            
        }
        for(int i = 0; i < gas.size(); i++)
        {
            int sum = 0;
            for(int j = 0; j < gas.size(); j++)
            {
                sum += gas[j];
                if(sum < 0)
                    break;
            }
            gas.push_back(gas[0]);
            gas.erase(gas.begin());
            if(sum >= 0)
                return i;
        }
        return -1;
    }
};
