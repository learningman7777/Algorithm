class Solution:
    def twoSum(self, nums, target):
        dict_nums = {}
        for i, n in enumerate(nums):
            comp = target - n
            found = dict_nums.get(comp)
            if found is not None:
                return [found, i]

            dict_nums[n] = i

input_nums = None
target = None
with open('input.txt', 'r') as file:
    input_list = file.read().split('\n')
    input_nums = [int(x) for x in input_list[0].strip('[]').replace('"', '').replace(' ', '').split(',')]
    target = int(input_list[1])
    #print(type(s))

sol = Solution()
print(sol.twoSum( input_nums, target))