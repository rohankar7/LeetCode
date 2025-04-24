# 589. N-ary Tree Preorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            for i in node.children[::-1]:
                stack.append(i)
        return result