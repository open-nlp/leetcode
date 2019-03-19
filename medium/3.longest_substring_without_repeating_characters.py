#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:junxu
@email: xujunrt@163.com
@time: 2019-03-14 17:43
"""

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}  # 记录起始位置的速查表
        startPoint, max_length = 0, 0  # startPoint记录目前的起始位置

        for i, j in enumerate(s):

            if j in table and table[j] >= startPoint:
                startPoint = table[j] + 1
                # 当j已经在table中，且j的位置大于等于start时，更新start

            else:  # 如果当先j不在table中，说明字符不重复
                max_length = max(max_length, i - startPoint + 1)
                # 根据为当前连续字符长度，更新max_length

            table[j] = i  # 更新字符起始位置

        return max_length

if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)