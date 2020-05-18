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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == p || root == q || root == NULL)
        {
            return root;
        }
        TreeNode *pRight = lowestCommonAncestor(root->right, p, q);
        TreeNode *pLeft = lowestCommonAncestor(root->left, p, q);
        if(pRight && pLeft)
        {
            return root;
        }
        return (pRight)?pRight:pLeft;
    }
};
