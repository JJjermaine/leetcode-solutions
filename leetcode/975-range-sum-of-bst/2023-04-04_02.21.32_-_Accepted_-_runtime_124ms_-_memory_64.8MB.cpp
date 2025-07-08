/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
int sum=0;
void help(TreeNode* root, int low, int high){
    if(root==nullptr) return;
    if(root->val<=low){
        if(root->val==low){
            sum+=root->val;
        }
        help(root->right,low,high);
    }
    else if(root->val>=high){
        if(root->val==high){
            sum+=root->val;
        }
        help(root->left,low,high);
    }
    else{
      sum+=root->val;
        help(root->left,low,high);
        help(root->right,low,high);
    }
}
    int rangeSumBST(TreeNode* root, int low, int high) {
        help(root,low,high);
        return sum;
    }
};