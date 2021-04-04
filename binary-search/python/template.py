
def lower_bond(A, target):
    left = 0
    right = len(A) - 1
    while left < right:
        middle = (left + right) // 2
        if A[middle] >= target:
            right = middle
        else:
            left = middle + 1
    return left

def upper_bond(A, target):
    left = 0
    right = len(A) - 1
    while left < right:
        middle = (left + right) // 2
        if A[middle] > target:
            right = middle
        else:
            left = middle + 1
    return left

if __name__ == "__main__":
    nums = [1,3,5,5,5,5,7,9]
    print(upper_bond(nums, 5))
    print(lower_bond(nums, 5))