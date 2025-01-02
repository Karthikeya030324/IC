class Solution(object):
  def reverseWords(self, s):
      string=s.split()
      rev=' '.join(reversed(string))
      return rev