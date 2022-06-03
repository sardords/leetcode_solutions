class Solution:
    def mySqrt(self, x: int) -> int:
        return binary_search_int(0, x + 1, x)


def binary_search_int(left: int, right: int, target: int) -> int:
    if left >= right:
        return left-1
    mid = (left + right) // 2
    if mid * mid == target:
        return mid
    elif mid * mid > target:
        return binary_search_int(left, mid, target)
    else:
        return binary_search_int(mid + 1, right, target)