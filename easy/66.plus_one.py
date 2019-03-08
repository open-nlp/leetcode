#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-08 18:17
"""

"""

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution(object):
    def plus_one(self,digits):
        """
        :param digits: List[int]
        :return: List[int]
        """
        sum = 0
        for x in digits:
            sum = sum*10+x
        return [int(res) for res in str(sum+1)]

if __name__ == '__main__':
    digits = [1,1,1,2]
    solution = Solution()
    result = solution.plus_one(digits)
    print(result)