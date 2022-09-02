/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public HashMap<Integer, Double> sum = new HashMap<>();
    public HashMap<Integer, Integer> count = new HashMap<>();
    public void traverse(TreeNode root, int level){
        if(root == null) return;
        sum.put(level, sum.getOrDefault(level, 0.0) + root.val);
        count.put(level, count.getOrDefault(level, 0) + 1);
        traverse(root.left, level + 1);
        traverse(root.right, level + 1);

    }
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new LinkedList<>();
        traverse(root, 0);
        int i = 0;
        while(sum.containsKey(i)){
            res.add((double)sum.get(i) / (double)count.get(i));
            i++;
        }
        return res;
    }
}