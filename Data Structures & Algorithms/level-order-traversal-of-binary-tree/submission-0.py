from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([[root]])
        res = []

        while queue:
            curr_level = queue.popleft()
            next_level = []

            for element in curr_level:
                if element.left is not None:
                    next_level.append(element.left)
                if element.right is not None:
                    next_level.append(element.right)

            if next_level:
                queue.append(next_level)

            res.append([node.val for node in curr_level])

        return res