class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        bool res = false;
        if(matrix.empty() || matrix[0].empty())
            return false;
        for(int i = 0; i < matrix.size(); i++){
            if(matrix[i][matrix[0].size()-1] < target)
                continue;
            if(matrix[i][0] > target)
                break;
            res = semiSearch(matrix[i], target);
            if(res)
                return res;
        }
        return res;
    }
private:
    bool semiSearch(vector<int>& matrix, int target){
        int temp = 0;
        int high = matrix.size() - 1;
        int low = 0;
        while(true){
            if(high - low > 1){
                temp = (high + low)/2;
                if(matrix[temp] > target)
                    high = temp;
                else
                    low = temp;
            }
            else{
                if(matrix[low] == target || matrix[high] == target)
                    return true;
                else
                    return false;
                break;
            }
        }
    }
};
