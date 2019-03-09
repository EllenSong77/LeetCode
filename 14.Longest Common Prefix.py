from typing import List


class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
      return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
      while strs[i].find(prefix) != 0:
        prefix = prefix[:len(prefix) - 1]
        if prefix == "":
          return ""
    return prefix


  def longestCommonPrefixEllen(self, strs: List[str]) -> str:
    prefix = ""
    if len(strs) == 0:
      return prefix
    if len(strs) == 1:
      return strs[0]
    for i in range(len(strs) - 1):
      tmp = ""
      for j in range(i + 1, len(strs)):
        check = prefix if prefix != "" else strs[i]
        for s in range(len(check)):
          if strs[j].startswith(check[:s + 1]):
            tmp = check[:s + 1]
          else:
            break
        if len(tmp) == 0:
          break
        else:
          prefix = tmp
      if len(tmp) == 0:
        return ""
      else:
        prefix = tmp
    return prefix

if __name__ == '__main__':
    s = Solution()
    # print(s.longestCommonPrefix(["flower","flow","flight"]))
    # print(s.longestCommonPrefix([]))
    # print(s.longestCommonPrefix(["a"]))
    # print(s.longestCommonPrefix(["a","b","c"]))
    # print(s.longestCommonPrefix(["ab","a","c"]))
    # print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["c","acc","ccc"]))