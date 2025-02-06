class Solution(object):
  def maxLevelSum(self, root):
      if not root:
          return 0

      max_sum = float('-inf')
      max_level = 1
      current_level = 1
      queue = deque([root])

      while queue:
          level_sum = sum(node.val for node in queue)

          if level_sum > max_sum:
              max_sum = level_sum
              max_level = current_level

          for _ in range(len(queue)):
              node = queue.popleft()
              if node.left:
                  queue.append(node.left)
              if node.right:
                  queue.append(node.right)

          current_level += 1

      return max_level