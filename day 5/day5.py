file = "input_d5"

with open(file) as f:
    text = f.read().strip()


def find_next_value(mapping, prev_value):
    next_value = prev_value
    for _ in mapping:
        nums = [int(a) for a in _.strip().split()]
        if prev_value in range(nums[1], nums[1] + nums[2]):
            next_value = prev_value + (nums[0] - nums[1]) if nums[0] > nums[1] else prev_value - (nums[1] - nums[0])

    return next_value


seeds = [int(a) for a in text.strip().splitlines()[0].split(":")[1].strip().split()]
map_seed_to_soil = (text.split("seed-to-soil map:")[1]
                    .split("soil-to-fertilizer map:")[0].strip().splitlines())
map_soil_to_fertilizer = (text.split("soil-to-fertilizer map:")[1]
                          .split("fertilizer-to-water map:")[0].strip().splitlines())
map_fertilizer_to_water = (text.split("fertilizer-to-water map:")[1]
                           .split("water-to-light map:")[0].strip().splitlines())
map_water_to_light = (text.split("water-to-light map:")[1]
                      .split("light-to-temperature map:")[0].strip().splitlines())
map_light_to_temperature = (text.split("light-to-temperature map:")[1]
                            .split("temperature-to-humidity map:")[0].strip().splitlines())
map_temperature_to_humidity = (text.split("temperature-to-humidity map:")[1]
                               .split("humidity-to-location map:")[0].strip().splitlines())
map_humidity_to_location = (text.split("humidity-to-location map:")[1].strip().splitlines())

min_loc = float('inf')
for seed in seeds:
    soil = find_next_value(map_seed_to_soil, seed)
    fertilizer = find_next_value(map_soil_to_fertilizer, soil)
    water = find_next_value(map_fertilizer_to_water, fertilizer)
    light = find_next_value(map_water_to_light, water)
    temperature = find_next_value(map_light_to_temperature, light)
    humidity = find_next_value(map_temperature_to_humidity, temperature)
    location = find_next_value(map_humidity_to_location, humidity)
    min_loc = min(min_loc, location)

print(min_loc)
