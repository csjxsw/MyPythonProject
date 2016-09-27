#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        left = 0
        right = 0
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                left = root.left.val
            else:
                left = self.sumOfLeftLeaves(root.left)
        if root.right != None:
            right = self.sumOfLeftLeaves(root.right)
        return left + right


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
    right.left = right2

    result = s.sumOfLeftLeaves(root)
    print result
    #print ("------end--------")

