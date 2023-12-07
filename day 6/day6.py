file = "input_d6"
with open(file) as f:
    lines = f.read().strip().splitlines()

times = [int(a) for a in lines[0].strip().split(":")[1].strip().split()]
distances = [int(a) for a in lines[1].strip().split(":")[1].strip().split()]

speed = 0
prod = 1
for idx, secs in enumerate(times):
    count = 0
    for hold_time in range(secs + 1):
        speed = hold_time
        distance = speed * (secs - hold_time)
        if distance > distances[idx]:
            count += 1
    prod *= count
print(prod)

times = int(lines[0].strip().split(":")[1].strip().replace(" ", ""))
distances = int(lines[1].strip().split(":")[1].strip().replace(" ", ""))
speed = 0
count = 0
for hold_time in range(times + 1):
    speed = hold_time
    distance = speed * (times - hold_time)
    if distance > distances:
        count += 1
print(count)
