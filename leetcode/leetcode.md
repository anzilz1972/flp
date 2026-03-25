# Leetcode练习
# 本文档记录我配套LeeCode练习

作者：王国安

状态：最终版

类型：标准跟踪

创建日期：2026年3月23日

Python版本：3.12

所有练习题目来自 https://leetcode.cn

---

## 1. 两数之和

### 题目
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

### 示例

#### 示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

#### 示例 2：
    输入：nums = [3,2,4], target = 6
    输出：[1,2]

#### 示例 3：
    输入：nums = [3,3], target = 6
    输出：[0,1]


### 提示
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* 只会存在一个有效答案


### code:

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for num_a in nums:
            idx_a = nums.index(num_a)
            idx_b = idx_a + 1
            while idx_b < len(nums):
                if nums[idx_a] + nums[idx_b] == target:
                    result.append(idx_a)
                    result.append(idx_b)
                    return result
                idx_b += 1
        return result


def main():
    inums = [3,2,4]
    target = 6
    s = Solution()
    s.twoSum(inums, target)
if __name__ == '__main__':
    main()
               
```
