# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        use dfs, but utilize a hashmap from the values to their indices in inorder

        build  a hashmap out of inorder
        """

        indices = {val: idx for idx, val in enumerate(inorder)}

        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None
            rootValue = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootValue)
            mid = indices[rootValue]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)