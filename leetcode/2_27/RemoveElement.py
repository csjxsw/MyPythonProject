#!/usr/bin/env python
# coding=utf-8

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        numslen = len(nums)
        for index in range(numslen):
            num = nums[index]
            if num != val:
                nums[count] = num
                count = count+1
        return count


if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    num = [2, 2,4,3,5,4,6]
    target = 4
    reults = s.removeElement(num, target)
    print reults
    print num
    #print ("------end--------")

