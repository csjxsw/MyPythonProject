#!/usr/bin/env python
# coding=utf-8

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 > 0

if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    num = 9
    result = s.canWinNim(num)
    print result
    #print ("------end--------")

