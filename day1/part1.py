import re
# find the first and last number on each line
# a line might only have one number so it is first and last
# combine the two numbers to make another number
# Add up all the numbers

p = re.compile(r"\d")


def calculate_total(filename):
    total = 0
    with open(filename,'r') as f:
        for line in f.readlines():
            nums = p.findall(line)
            total += int(nums[0] + nums[-1])
    return total


assert calculate_total('./day1/part1-test-input.txt') == 142

print(calculate_total('./day1/input.txt'))