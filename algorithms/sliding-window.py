
    def minSubArrayLen(target,nums):
        left=0
        right=0
        summ=0
        minimum=[]

        while right<len(nums):
            summ+=nums[right]

            while summ>=target:
                minimum.append(right-left+1)
                summ-=nums[left]
                left+=1

            right+=1
        return 0 if(len(minimum)==0) else min(minimum)

