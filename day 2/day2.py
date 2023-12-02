def first_half(inp):
    max_red = 12
    max_green = 13
    max_blue = 14
    sum_id = 0
    for i in inp:
        game_id = int(i.split(":")[0].split(" ")[1])
        sets = i.split(":")[1].strip().split(";")
        flag = 0
        for idx, balls in enumerate(sets):
            balls = balls.split(",")
            for ball in balls:
                ball = ball.strip()
                if ball.split(" ")[1] == "red":
                    red = int(ball.split(" ")[0])
                    if red > max_red:
                        flag = 1
                        break
                elif ball.split(" ")[1] == "green":
                    green = int(ball.split(" ")[0])
                    if green > max_green:
                        flag = 1
                        break
                else:
                    blue = int(ball.split(" ")[0])
                    if blue > max_blue:
                        flag = 1
                        break
        if flag == 0:
            sum_id += game_id
    print(sum_id)


def second_half(inp):
    sum_prod = 0
    for i in inp:
        min_red = min_green = min_blue = 0
        sets = i.split(":")[1].strip().split(";")
        for idx, balls in enumerate(sets):
            balls = balls.split(",")
            for ball in balls:
                ball = ball.strip()
                if ball.split(" ")[1] == "red":
                    red = int(ball.split(" ")[0])
                    if red > min_red:
                        min_red = red
                elif ball.split(" ")[1] == "green":
                    green = int(ball.split(" ")[0])
                    if green > min_green:
                        min_green = green
                else:
                    blue = int(ball.split(" ")[0])
                    if blue > min_blue:
                        min_blue = blue
        sum_prod += min_red * min_green * min_blue
    print(sum_prod)


if __name__ == "__main__":
    file = "input_d2"
    with open(file) as f:
        inp = f.read().splitlines()

    first_half(inp)
    second_half(inp)
