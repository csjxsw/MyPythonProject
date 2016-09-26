#!/usr/bin/env python
# coding=utf-8

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                i = i+1
                j = j+1
            else:
                i = i+1
        while j < len(nums):
            nums[j]=0
            j = j+1



if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    nums = [2, 7, 0, 0, 11, 15]
    reults = s.moveZeroes(nums)
    print nums
    #print ("------end--------")

