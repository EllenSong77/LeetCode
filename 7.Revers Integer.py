class Solution:
  def reverse(self, x: int) -> int:
    if x < -1 * 2 ** 31 or x > 2 ** 31 - 1:
      return 0
    res = 0
    positive = 1 if x >= 0 else -1
    x = abs(x)
    while True:
      digit = x % 10
      x = x // 10
      res = res * 10 + digit
      if res < -1 * 2 ** 31 or res > 2 ** 31 - 1:
        return 0
      if x == 0:
        res *= positive
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))