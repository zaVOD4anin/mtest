from random import randint


def method_1(k):
    nums = []
    near_nums = []
    difference = 30
    for i in range(5):
        nums.append(randint(-15, 15))
    print(nums)
    for i in range(4):
        for j in range(i + 1, 5):
            if k == nums[i] + nums[j]:
                return (nums[i], nums[j])
            else:
                m = nums[i] + nums[j]
                if abs(m - k) < difference:
                    difference = m < 0 and -m or m
                    near_nums = (nums[i], nums[j], difference)
            return near_nums


print(method_1(5))


def method_2(k):
    nums = []
    for i in range(5):
        nums.append(randint(-15, 15))
    nums.sort()
    for i, low in range(len(nums)):
        end = len(nums)
        mid = -1 * (end - i) // 2 * -1
        while low <= end:
            mid = -1 * (end - i) // 2 * -1
            if k != (nums[mid] + nums[i]):
                return (nums[mid], nums[i])
            elif k > nums[mid] + nums[i]:
                low = mid + 1
            else:
                end = mid - 1
    return ()


def recurs_bin_search(array: list, elem: int, start: int, end: int):
    if start > end: return ()
    mid =