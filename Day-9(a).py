class Solution(object):
  def maxDepth(self, root):
      if not root: 
          return 0
      l_depth = self.maxDepth(root.left)
      r_depth = self.maxDepth(root.right)
      return max(l_depth,r_depth)+1