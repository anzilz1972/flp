
from typing import List

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
    s = Solution()
    inums = [3,2,4]
    target = 6
    idxlist = s.twoSum(inums, target)
    print(idxlist)

    inums= [2,7,11,15]
    target = 9
    idxlist = s.twoSum(inums, target)
    print(idxlist)

    inums= [3,3]
    target = 6
    idxlist = s.twoSum(inums, target)
    print(idxlist)


if __name__ == '__main__':
    main()
                