import regex as re


def first_half(calibration_document):
    calibration_value = 0
    for line in calibration_document:
        digits = re.findall("\d", line)
        if len(digits) == 0:
            continue
        num = int(digits[0] + digits[-1])
        calibration_value += num
    print(calibration_value)


def second_half(calibration_document):
    numbers = enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    calibration_value = 0
    nums = [e[1] for e in numbers]
    for line in calibration_document:
        digits = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line,
                            overlapped=True)  # fucking bullshit
        if len(digits) == 0:
            continue
        for idx, number in enumerate(digits):
            if number in nums:
                digits[idx] = str(nums.index(number) + 1)
        num = int(digits[0] + digits[-1])
        calibration_value += num
    print(calibration_value)


def first_half_remastered(calibration_document):
    calibration_value = 0
    for line in calibration_document:
        num = int(re.search("\d", line).group(0) + re.search("\d", line[::-1]).group(0))
        calibration_value += num
    print(calibration_value)


if __name__ == "__main__":
    file_input = "input_d1"
    with open(file_input) as f:
        calibration_document = f.read().splitlines()

    first_half(calibration_document)
    second_half(calibration_document)
    first_half_remastered(calibration_document)
