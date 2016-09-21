#!/usr/bin/env python
# coding=utf-8

class Solution:
    def singleNumber(self, nums):
        numlen = len(nums)
        res = 0
        for index in range(numlen):
            res = res ^ nums[index]
        return res


if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    num = [2, 7, 11, 15,2,7,11]
    target = 18
    reults = s.singleNumber(num)
    print reults
    #print ("------end--------")

