#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftnum = 1+self.maxDepth(root.left)
        rightnum = 1+self.maxDepth(root.right)
        return leftnum if leftnum>rightnum else rightnum


if __name__ == '__main__':
    #print ("------begin--------")
    s = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left2 = TreeNode(4)
    right2 = TreeNode(5)
    root.left = left
    root.right = right
    left.left = left2
    left2.left = right2

    result = s.maxDepth(root)
    print result
    #print ("------end--------")

