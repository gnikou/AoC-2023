file = "input_d9"
with open(file) as f:
    sequences = f.read().strip().splitlines()


def calc(seq):
    sequence = [int(a) for a in seq]
    next_num = 0
    tmp = sequence.copy()
    while any(tmp):
        tmp2 = tmp.copy()
        tmp = []

        for idx, number in enumerate(tmp2):
            if idx != len(tmp2) - 1:
                tmp.append(tmp2[idx + 1] - tmp2[idx])
        next_num += tmp[-1]
    return sequence[-1] + next_num


sequence = [seq.strip().split() for seq in sequences]
print(sum(map(calc, sequence)))

sequence_rev = [seq.strip().split()[::-1] for seq in sequences]
print(sum(map(calc, sequence_rev)))
