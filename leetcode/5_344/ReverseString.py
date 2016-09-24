#!/usr/bin/env python
# coding=utf-8

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for c in s:
            res = c+res
        return res


if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    str = "hello"
    result = s.reverseString(str)
    print result
    #print ("------end--------")

