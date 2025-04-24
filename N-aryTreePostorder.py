# 590. N-ary Tree Postorder
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.result = []
        def postN(node):
            if not node: return
            for i in node.children:
                postN(i)
            self.result.append(node.val)
        postN(root)
        return self.result