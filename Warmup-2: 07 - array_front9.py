# CODING BAT > Warmup-2 > array_front9

def array_front9(nums):
    num_len = len(nums)
    if num_len > 4:
        num_len = 4
    for i in range(num_len):
        if nums[i] == 9:
            return True
    return False
