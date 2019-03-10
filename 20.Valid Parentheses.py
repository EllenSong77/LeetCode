"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


# TODO: Not None.
class Solution:
  def isValid(self, s: str) -> bool:
    start = 0
    end = len(s) - 1
    m = {
      '(': ')',
      '{': '}',
      '[': ']'
    }
    rev_m = {
      ')': '(',
      '}': '{',
      ']': '['
    }
    find = False
    while start < len(s) - 1:
      if not s[start] in m:
        start += 1
        continue
      find = True
      while start < end:
        if s[end] != m.get(s[start]):
          if s[end] in rev_m:
            return False
          end -= 1
          continue
        find = False
        end -= 1
        start += 1
    if find:
      return False
    return True


if __name__ == '__main__':
  s = Solution()
  print(s.isValid("()"))
  print(s.isValid("()[]{}"))
  print(s.isValid("(]"))
  print(s.isValid("([)]"))
  print(s.isValid("{[]}"))
