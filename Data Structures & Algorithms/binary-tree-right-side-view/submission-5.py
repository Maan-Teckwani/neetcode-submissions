from collections import deque

class Solution:
    def rightSideView(self, root):
        res = []
        q = deque([root]) if root else deque()

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level[-1])

        return res