# In this example, the calibration values are
#  29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

import re
# find the first and last number on each line
# a line might only have one number so it is first and last
# combine the two numbers to make another number
# Add up all the numbers

p = re.compile(r"\d")
tr = [("one","1"),("two", "2"),("three","3"),("four","4"),("five", "5"),
      ("six","6"),("seven","7"), ("eight", "8"), ("nine","9")]

def calculate_total(filename):
    total = 0
    with open(filename, 'r') as f:
         for line in f.readlines():
                nums = []
                for i in range(0,len(line)):

                    for t in tr:
                        if line[i:].startswith(t[1]) or line[i:].startswith(t[0]):
                            nums.append(t[1])
                            break

                total += int(nums[0] + nums[-1])
    return total

print(calculate_total('./day1/part2-test-input.txt'))
assert calculate_total('./day1/part2-test-input.txt') == 281
print(calculate_total('./day1/input.txt'))
