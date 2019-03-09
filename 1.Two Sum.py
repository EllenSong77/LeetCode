from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    res = dict()
    for i in range(len(nums)):
      diff = target - nums[i]
      if res.get(diff) is not None:
        if res.get(diff) != i:
          return ([i, res.get(diff)])
      res[nums[i]] = i
    return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
