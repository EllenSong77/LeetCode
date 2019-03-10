# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    p = l1,
    q = l2,
    cur = head
    carry = 0
    while p is not None or q is not None:
      x = 0 if p is None else p.val
      y = 0 if q is None else q.val
      sum = carry + x + y
      carry = sum // 10
      cur.next = ListNode(sum % 10)
      cur = cur.next
      if p is not None:
        p = p.next
      if q is not None:
        q = q.next
    if carry > 0:
      carry.next = ListNode(carry)
    return head.next


if __name__ == '__main__':
  s = Solution()
  print(s.addTwoNumbers([2, 4, 3], [5, 6, 4]))
