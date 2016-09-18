#!/usr/bin/env python
# coding=utf-8

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        numslen = len(nums)
        for index in range(numslen):
            num = nums[index]
            if num in dict:
                return [dict.get(num), index]
            else:
                dict[target-num] = index



if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    num = [2, 7, 11, 15]
    target = 18
    reults = s.twoSum(num, target)
    print reults
    #print ("------end--------")

