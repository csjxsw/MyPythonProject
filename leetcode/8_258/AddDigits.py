#!/usr/bin/env python
# coding=utf-8

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return num
        return (num-1)%9+1



if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    num = 12
    result = s.addDigits(num)
    print result
    #print ("------end--------")

