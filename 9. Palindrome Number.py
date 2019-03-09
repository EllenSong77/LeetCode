class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
      return False
    rev = 0
    while x > rev:
      rev = rev * 10 + x % 10
      x = x // 10
    return x == rev or x == rev // 10

  def isPalindromeEllen(self, x: int) -> bool:
    s = str(x)
    l = len(s)

    if l == 1:
      return True

    if s.startswith('-') or s.endswith('0'):
      return False

    for i in range(l):
      head = s[i]
      tail = s[l - 1 - i]
      if head != tail:
        return False
    return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(0))
    print(s.isPalindrome(10))