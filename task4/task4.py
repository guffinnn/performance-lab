def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


def min_moves(nums):
    median = find_median(nums)
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves


def read_nums_from_file(filename):
    with open(filename, "r") as file:
        nums = [int(line.strip()) for line in file]
    return nums


if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    nums = read_nums_from_file(filename)
    result = int(min_moves(nums))
    print(result)
