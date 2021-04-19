class Solution:   
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._d = 0
        self._dfs(root)
        return self._d
    
    def _dfs(self, root):
        if root is None:
            return 0
        ld = self._dfs(root.left)
        rd = self._dfs(root.right)
        self._d = max(self._d, ld+rd)
        
        return 1 + max(ld, rd)