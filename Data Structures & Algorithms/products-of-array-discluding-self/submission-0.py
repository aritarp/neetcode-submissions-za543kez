class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create list of products [1,1,1,1] of the same length as the length of nums
        prefix = [1] * len(nums)

        # go right to left
        # range (start = 1 and not 0, stop = length of nums, step)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            # print(prefix[i], '=', prefix[i-1], '*', nums[i-1])

        postfix = 1
        # go left to right
        # range (start = length of nums - 1, stop = -1, step = -1 keep going back one)
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= postfix
            # print(prefix[i],'=',prefix[i],'*',postfix)
            postfix *= nums[i]
            # print(postfix,'=',postfix,'*',nums[i])

        # brute force approach: 
        # product = []
        # for i in nums:
        #     prd = 1
        #     for j in nums:
        #         if j != i:
        #             prd *= j
        #     product.append(prd)
        # return product
        return prefix
        