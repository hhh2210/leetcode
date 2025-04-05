"""
题目：
给你一个整数数组 `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。
解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

思路：
数学上的直觉是阶乘，如果要清晰一点的思路就是画图遍历，每一个元素进行连线。
那考虑到连线，可以尝试引入回溯法来解决这道题目，形成一个树结构。
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #最后的返回
        solution = []
        #探索路径
        current_path = []
        
        def backtrack(start_index):
            # 每次递归都将当前路径加入结果集
            solution.append(current_path[:])
            
            # 从start_index开始遍历，避免重复
            for i in range(start_index, len(nums)):
                # 选择当前元素
                current_path.append(nums[i])
                # 继续递归探索
                backtrack(i + 1)
                # 回溯，撤销选择
                current_path.pop()
        
        # 从索引0开始回溯
        backtrack(0)
        return solution