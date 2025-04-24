# 572. Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def searchRootTree(node1, node2):
            if isIdentical(node1, node2):
                return True
            if node1==None: return False
            lChild = searchRootTree(node1.left, node2)
            rChild = searchRootTree(node1.right, node2)
            return lChild or rChild
        def isIdentical(lTree, rTree):
            if lTree==None and rTree==None: return True
            elif lTree!=None and rTree!=None:
                if lTree.val == rTree.val:
                    l = isIdentical(lTree.left, rTree.left)
                    r = isIdentical(lTree.right, rTree.right)
                    return l and r
            return False
        return searchRootTree(root, subRoot)