from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        return self._diameterOfBinaryTree(root)


    def _diameterOfBinaryTree(self, node):
        if node is None:
            return 0
        left = self._diameterOfBinaryTree(node.left)
        right = self._diameterOfBinaryTree(node.right)
        self.result = max(self.result, left + right)

        return max(left, right) + 1


test = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
root = to_binary_tree(test)
s = Solution()
print(s.diameterOfBinaryTree(root))