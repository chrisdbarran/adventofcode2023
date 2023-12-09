# Actual data includes negative numbers

def load_data(filename):
    report = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            readings = [int(x) for x in line.strip().split()]
            report.append(readings)
    return report

def find_next_for_row(this_row):
    # base case
    if set(this_row) == {0}:
        return 0
    next_row = [y-x for x, y in zip(this_row, this_row[1:])]
    return find_next_for_row(next_row) + this_row[-1]

def oasis_report(filename):
    report = load_data(filename)
    result = 0
    for row in report:
        result += find_next_for_row(row)
    return result


test_report = oasis_report('./day9/part1-test-input.txt')
print(f"Test Report: {test_report}")
assert test_report == 114

report = oasis_report('./day9/input.txt')
print(f"Report: {report}")

