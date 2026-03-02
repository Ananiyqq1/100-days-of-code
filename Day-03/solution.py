# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        current = root
        while current:
            self.stack.append(current)
            current = current.left

    def next(self) -> int:
        if not self.stack: return None
        cand = self.stack.pop()
        current = cand

        if current.right:
            current = current.right
        else:
            current = None
        while current:
            self.stack.append(current)
            current = current.left

        return cand.val

    def hasNext(self) -> bool:
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()