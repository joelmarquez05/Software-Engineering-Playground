# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return (p == None and q == None)
        left_is_equal = self.isSameTree(p.left, q.left)
        right_is_equal = self.isSameTree(p.right, q.right)
        return p.val == q.val and left_is_equal and right_is_equal