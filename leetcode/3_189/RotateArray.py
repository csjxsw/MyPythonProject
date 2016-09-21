#!/usr/bin/env python
# coding=utf-8

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numslen = len(nums)
        array = []
        for index in range(numslen):
            newindex = (index+numslen-k)%numslen
            array.append(nums[newindex])
        for index in range(numslen):
            nums[index] = array[index]

    def rotate(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start = start + 1
            end = end - 1

    def rotate_better(self, nums, k):
        numlen = len(nums)
        k = k % numlen
        self.rotate(nums,0,numlen-1)
        self.rotate(nums, 0, k-1)
        self.rotate(nums,k,numlen-1)

if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    num = [1,2,3,4,5,6,7]
    target = 3
    s.rotate_better(num, target)
    print num
    #print ("------end--------")

