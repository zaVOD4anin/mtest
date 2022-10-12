def is_in_list(lst: list, obj: any) -> bool:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if obj == lst[mid]:
            return True
        elif obj < lst[mid]:
            high = mid - 1
        elif obj > lst[mid]:
            low = mid + 1
    return False


if __name__ == '__main__':
    print(is_in_list([1, 2, 5, 8, 9], 5))
