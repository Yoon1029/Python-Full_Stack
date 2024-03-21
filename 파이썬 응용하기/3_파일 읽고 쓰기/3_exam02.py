# 여기에 코드를 작성하세요
sum = 0
changing_list = []

with open("data/chicken.txt", "r") as f:
    for line in f:
        new_list = (line.strip().split("일: "))
        sum += int(new_list[1])
        changing_list += new_list
    days = len(changing_list) // 2
    print(sum / days)