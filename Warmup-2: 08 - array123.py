# CODING BAT > Warmup-2 > array123

def array123(nums):
    for i in range(len(nums)):
        if i <= len(nums) - 3:
            if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
                return True
            else:
                continue
    return False
