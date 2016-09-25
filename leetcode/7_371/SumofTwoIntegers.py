#!/usr/bin/env python
# coding=utf-8

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)

if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    a = -8
    b = -12
    result = s.getSum(a, b)
    print result
    #print ("------end--------")

