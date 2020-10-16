def get_missing(nums):
    maxInt = max(nums)
    real_sum = sum(nums)
    fake_sum = (maxInt * (maxInt + 1)) / 2
    return int(fake_sum - real_sum)


arr = [1, 2, 4, 6, 3, 7, 8]
print(get_missing(arr))