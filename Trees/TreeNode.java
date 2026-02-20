package Trees;
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
 
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        return traverse(root1, root2);
    }

    public static TreeNode traverse(TreeNode root1, TreeNode root2) {
        // root
        if (root1 != null && root2 != null) {
            root1.val += root2.val;
        }
        else if (root1 == null && root2 != null) {
            root1 = new TreeNode(root2.val);
        }
        else if (root2 == null) {
            return root1;
        } 
        // root2 will always be something from this point
        
        if (root2.left != null && root1.left == null) {
            root1.left = new TreeNode();
        }
        if (root2 != null && root2.left !=null) traverse(root1.left, root2.left);

        if (root1.right == null && root2.right !=null) {
            root1.right = new TreeNode();
        }
        if (root2 != null && root2.right !=null) traverse(root1.right, root2.right);

        return root1;
    }
}