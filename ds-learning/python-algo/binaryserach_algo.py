def binary_search(list_search, item):
    low = 0
    high = len(list_search) - 1

    while low <= high:
        # 5/2=2.5 --- 5//2=2 ---- 5%2 = 1 --- -(-5//2)=3 --- int(5/2)+(5%2 >0)=3
        # (numerator + denominator - 1) // denominator
        # import math
        # math.ceil(5.4) = 6
        mid = (low + high + 1) // 2
        guess = list_search[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(my_list, 1))
