class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int temp = 0;
        for(int j = 0; j < gas.size(); j++)
        {
            int sum = 0;
            for(int i = 0; i < gas.size(); i++)
            {
                sum += gas[i];
                sum -= cost[i];
                if(sum < 0)
                {
                    gas.push_back(gas[0]);
                    gas.erase(gas.begin());
                    cost.push_back(cost[0]);
                    cost.erase(cost.begin());
                    temp += 1;
                    break;
                }
            }
            if(sum >= 0)
            {
                return temp;
                break;
            }
        }
        return -1;
    }
};
