# 637. Average of Levels in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        totalSum = []
        count = []
        def inorder(node, level):
            if not node: return
            if level == len(totalSum):
                totalSum.append(node.val)
                count.append(1)
            else:
                totalSum[level] += node.val
                count[level] += 1
            inorder(node.left, level + 1)
            inorder(node.right, level + 1)
        inorder(root, 0)
        return [sum / length for sum, length in zip(totalSum, count)]