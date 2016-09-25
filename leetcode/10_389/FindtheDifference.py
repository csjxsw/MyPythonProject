#!/usr/bin/env python
# coding=utf-8

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_s = dict()
        dic_t = dict()

        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1

        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1

        for i in t:
            # print i
            try:
                if dic_t[i] != dic_s[i]:
                    return i

            except:
                return i


if __name__ == '__main__':
    #print ("------begin--------")
    ss = Solution()
    s = "abcd"
    t = "abcde"
    result = ss.findTheDifference(s, t)
    print result
    #print ("------end--------")

