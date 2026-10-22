# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        maintain global result res, initialized with root's value
        define dfs(node):
                if the node is None:
                    return 0
                Recursively compute:
                    - leftMax = dfs(node.left)
                    - rightMax = dfs(node.right)
                
                ignore negative downward paths:
                    - leftMax = max(leftMax, 0)
                    - rigthMax = max(rightMax, 0)
                update global result with the best path through node:
                    res = max(res, node.val + leftmax + rightmax)
                return the best "extendable" downward path:
                    node.val + max(leftMax, rightMax)
        call  dfs(root) and return res
        """

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]