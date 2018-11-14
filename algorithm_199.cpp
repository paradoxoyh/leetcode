/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode *> q;
        vector<int> res;
        int count = 1;
        if(!root)
            return res;
        q.push(root);
        res.push_back(root->val);
        while(true)
        {
            q = rightest(q, count);
            count = q.size();
            if(count)
            {
                TreeNode *temp = q.front();
                res.push_back(temp->val);
            }
            else
                break;
        }
        return res;
    }
    queue<TreeNode *> rightest(queue<TreeNode *> q, int count)
    {
        TreeNode *temp = NULL;
        for(int i = 0; i < count; i++)
        {
            temp = q.front();
            q.pop();
            if(temp->right)
                q.push(temp->right);
            if(temp->left)
                q.push(temp->left);
        }
        return q;
    }
};
