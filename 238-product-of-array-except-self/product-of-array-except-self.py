class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answer = []
        zeros = 0

        for i in nums:
            if i == 0:
                zeros += 1
            else:
                product = product * i

        for i in range(len(nums)):
            if zeros >= 2:
                answer.append(0)
            elif zeros == 1:
                if nums[i] == 0:
                    answer.append(int(product))
                else:
                    answer.append(0)
            else:
                if nums[i] == 0:
                    answer.append(int(product))
                else:
                    answer.append(int(product / nums[i]))


        return answer
