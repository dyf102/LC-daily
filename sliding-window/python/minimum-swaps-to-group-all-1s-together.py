
def minSwaps(data: list)-> int:
    """[summary]

    Args:
        data (list): [description]

    Returns:
        int: [description]
    """
    n = len(data)
    total_num_one = sum(data)
    window = data[:total_num_one]
    num_zero = total_num_one - sum(window)
    res = num_zero
    for i in range(total_num_one, n):
        num_zero -= 1 if data[i - total_num_one] == 0 else 0
        num_zero += 1 if data[i] == 0 else 0
        res = min(num_zero, res)
    return res

if __name__ == "__main__":
    print(minSwaps([1,0,0,1,0,0,1])) # 2
    print(minSwaps([0,0,0,1,0])) # 0
    print(minSwaps([1,0,1,0,1,0,0,1,1,0,1])) # 0