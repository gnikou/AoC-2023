file = "input_d8"


def lcm(a, b):
    i = a
    while 1:
        if i % b == 0:
            return i
        i += a


with open(file) as f:
    lines = f.read().strip().splitlines()

instructions = lines[0]
map = dict()
path = lines[2:]
for i in path:
    map[i.split("=")[0].strip()] = (i.split("=")[1].strip()[1:4], i.split("=")[1].strip()[-4:-1])
cur_location = 'AAA'
destination = 'ZZZ'
count = 0
while cur_location != destination:
    for idx, turn in enumerate(instructions):
        count += 1
        cur_location = map[cur_location][0] if turn == "L" else map[cur_location][1]
print(count)

## AAA reaching end every 16579 turns, XQA every 16579 turns, so we take the LCM
starts = []
for i in path:
    tmp = i.split("=")[0].strip()
    if tmp[-1] == 'A':
        starts.append(tmp)
map = dict()
for i in path:
    map[i.split("=")[0].strip()] = (i.split("=")[1].strip()[1:4], i.split("=")[1].strip()[-4:-1])
    
turns = []
for idx, cur_location in enumerate(starts):
    count = 0
    while 1:
        if starts[idx][-1] == 'Z':
            turns.append(count)
            break

        for turn in instructions:
            count += 1
            starts[idx] = map[starts[idx]][0] if turn == "L" else map[starts[idx]][1]

            if starts[idx][-1] == 'Z':
                break
turns = sorted(turns, reverse=True)
lcm_num = turns[0]
for idx, count in enumerate(turns[1:]):
    lcm_num = lcm(lcm_num, count)
print(lcm_num)
