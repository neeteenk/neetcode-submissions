class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mpp = defaultdict(int)
        for i in range(len(numbers)):
            remTarget = target - numbers[i]
            if mpp[remTarget]:
                return [mpp[remTarget], i+1]
            mpp[numbers[i]] = i + 1
        return []