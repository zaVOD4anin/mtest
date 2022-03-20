from random import randint


def method_1(k: int):
    '''
    вернуть 2 числа сумма которых равна либо приближена к введенному числу
    ineration mode
    :param k: integer number
    :return: tuple 2 numbers
    '''
    nums = []
    near_nums = []
    difference = 30
    for i in range(5):
        nums.append(randint(-15, 15))
    print(nums)
    for i in range(3):
        for j in range(i + 1, 5):
            if sum_num == nums[i] + nums[j]:
                return (nums[i], nums[j])
            else:
                counter_sum_near = nums[i] + nums[j]
                if abs(counter_sum_near - sum_num) < difference:
                    difference = counter_sum_near < 0 and -counter_sum_near or counter_sum_near
                    near_nums = (nums[i], nums[j], difference)
    return near_nums


def recurs_bin_search(array: list, elem: int, start: int, end: int, i: int):
    '''
    binary search to method 2 with recourse
    :param array: initial array numbers
    :param elem: recuired number to find
    :param start: start position
    :param end: finish position
    :param i: initial num for create return turple
    :return: turple or ()
    '''
    if start > end: return ()
    mid = (end - start) // 2
    if elem == array[mid] or elem == array[start] or elem == array[end]:
        return (array[i], elem)
    elif elem > array[mid]:
        return recurs_bin_search(array, elem, mid + 1, end - 1, i)
    else:
        return recurs_bin_search(array, elem, start + 1, mid - 1, i)


def method_2(k):
    '''
    method 2 to find with binary search without nearby sum numbers
    :param k: int
    :return:
    '''
    nums = []
    for i in range(5):
        nums.append(randint(-15, 15))
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        low, max = i + 1, len(nums) - 1
        num1 = k - nums[i]
        #      while low <= max:
        #          mid = (max - low) // 2
        #          if num1 == nums[mid] or num1 == nums[low] or num1 == nums[max]:
        #              return (nums[i], num1)
        #          elif k > nums[mid] + nums[i]:
        #              low = mid + 1
        #              max -= 1
        #          else:
        #              max = mid - 1
        #              low += 1
        # iteration method to find numbers
        ir = recurs_bin_search(nums, num1, i + 1, max, i)
        if ir:
            return ir
    return ()


if __name__ == '__main__':
    print(method_2(5))
