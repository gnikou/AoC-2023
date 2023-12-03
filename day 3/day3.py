import re
from collections import defaultdict

file = "input_d3"
with open(file) as f:
    inp = f.read().strip().splitlines()

matrix = {}
sum_num = 0
sum_gear = 0
gear_list = defaultdict(int)
for idx1, line in enumerate(inp):
    for idx2, i in enumerate([*line]):
        matrix[idx1, idx2] = i

for idx1, line in enumerate(inp):
    num = re.findall('\d+', line)
    dims = [(m.start(0), m.end(0) - 1) for m in re.finditer('\d+', line)]
    prev_line = None
    next_line = None
    if idx1 != 0:
        prev_line = inp[idx1 - 1]

    if idx1 != len(inp) - 1:
        next_line = inp[idx1 + 1]

    for idx2, (i, j) in enumerate(dims):
        match = False
        if i == 0:
            if re.match('[^(\w.)|_]', matrix[idx1, j + 1]):
                match = True
            if re.match('[*]', matrix[idx1, j + 1]):
                if gear_list[idx1, j + 1]:
                    sum_gear += gear_list[idx1, j + 1] * num[idx2]
                else:
                    gear_list[idx1, j + 1] = num[idx2]

            if next_line:
                for x in range(i, j + 2):
                    if re.match('[^(\w.)|_]', matrix[idx1 + 1, x]):
                        match = True
                    if re.match('[*]', matrix[idx1 + 1, x]):
                        if gear_list[idx1 + 1, x]:
                            sum_gear += gear_list[idx1 + 1, x] * num[idx2]
                        else:
                            gear_list[idx1 + 1, x] = num[idx2]

            if prev_line:
                for x in range(i, j + 2):
                    if re.match('[^(\w.)|_]', matrix[idx1 - 1, x]):
                        match = True
                    if re.match('[*]', matrix[idx1 - 1, x]):
                        if gear_list[idx1 - 1, x]:
                            sum_gear += gear_list[idx1 - 1, x] * num[idx2]
                        else:
                            gear_list[idx1 - 1, x] = num[idx2]

        elif j == len(line) - 1:
            if re.match('[^(\w.)|_]', matrix[idx1, i - 1]):
                match = True
                if re.match('[*]', matrix[idx1, i - 1]):
                    if gear_list[idx1, i - 1]:
                        sum_gear += gear_list[idx1, i - 1] * num[idx2]
                    else:
                        gear_list[idx1, i - 1] = num[idx2]

            if next_line:
                for x in range(i - 1, j + 1):
                    if re.match('[^(\w.)|_]', matrix[idx1 + 1, x]):
                        match = True
                    if re.match('[*]', matrix[idx1 + 1, x]):
                        if gear_list[idx1 + 1, x]:
                            sum_gear += gear_list[idx1 + 1, x] * num[idx2]
                        else:
                            gear_list[idx1 + 1, x] = num[idx2]

            if prev_line:
                for x in range(i - 1, j + 1):
                    if re.match('[^(\w.)|_]', matrix[idx1 - 1, x]):
                        match = True
                    if re.match('[*]', matrix[idx1 - 1, x]):
                        if gear_list[idx1 - 1, x]:
                            sum_gear += gear_list[idx1 - 1, x] * num[idx2]
                        else:
                            gear_list[idx1 - 1, x] = num[idx2]
        else:
            if (re.match('[^(\w.)|_]', matrix[idx1, i - 1]) or
                    re.match('[^(\w.)|_]', matrix[idx1, j + 1])):
                match = True

            if (re.match('[*]', matrix[idx1, i - 1]) or
                    re.match('[*]', matrix[idx1, j + 1])):
                if gear_list[idx1, i - 1]:
                    sum_gear += gear_list[idx1, i - 1] * num[idx2]
                elif gear_list[idx1, j + 1]:
                    sum_gear += gear_list[idx1, j + 1] * num[idx2]
                else:
                    if re.match('[*]', matrix[idx1, i - 1]):
                        gear_list[idx1, i - 1] = num[idx2]
                    else:
                        gear_list[idx1, j + 1] = num[idx2]

            if next_line:
                for x in range(i - 1, j + 2):
                    if re.match('[^(\w.)|_]', matrix[idx1 + 1, x]):
                        match = True
                    if re.match('[*]', matrix[idx1 + 1, x]):
                        if gear_list[idx1 + 1, x]:
                            sum_gear += gear_list[idx1 + 1, x] * num[idx2]
                        else:
                            gear_list[idx1 + 1, x] = num[idx2]
            if prev_line:
                for x in range(i - 1, j + 2):
                    if re.match('[^(\w.)|_]', matrix[idx1 - 1, x]):
                        match = True
                    if re.match('[*]', matrix[idx1 - 1, x]):
                        if gear_list[idx1 - 1, x]:
                            sum_gear += gear_list[idx1 - 1, x] * num[idx2]
                        else:
                            gear_list[idx1 - 1, x] = num[idx2]

        if match:
            sum_num += int(num[idx2])

print(sum_num)
print(sum_gear)
