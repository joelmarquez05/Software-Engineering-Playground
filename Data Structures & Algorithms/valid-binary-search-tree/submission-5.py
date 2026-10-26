# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def DFS_solution(root, min_allowed, max_allowed):
            if not root:
                return True

            if root.val <= min_allowed:
                return False
            if root.val >= max_allowed:
                return False
            
            return DFS_solution(root.left, min_allowed, root.val) and DFS_solution(root.right, root.val, max_allowed)
        return DFS_solution(root, float("-inf"), float("inf"))


# min(root, root.right)
# max(root, root.left)
#               0
#       -1000       1000
#    null   null   0
#