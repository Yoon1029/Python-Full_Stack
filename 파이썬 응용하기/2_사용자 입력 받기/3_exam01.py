import random

chance = 4
random_num = random.randint(1, 20)

for i in range(chance):
    num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(4 - i)))
    if random_num > num:
        if i == 3:
            print("아쉽습니다. 정답은 {}였습니다.".format(random_num))
        print("up")
    elif random_num < num:
        if i == 3:
            print("아쉽습니다. 정답은 {}였습니다.".format(random_num))
        print("down")
    else:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다".format(i + 1))
        break