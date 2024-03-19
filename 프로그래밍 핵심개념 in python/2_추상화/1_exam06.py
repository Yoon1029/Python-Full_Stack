def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈
    if change >= 50000:
        chage_50000 = change // 50000
        change = change % 50000
    else:
        change_50000 = 0
    if change >= 10000:
        change_10000 = change // 10000
        change = change % 10000
    else:
        change_10000 = 0
    if change >= 5000:
        change_5000 = change // 5000
        change = change % 5000
    else:
        change_5000 = 0
    if change >= 1000:
        change_1000 = change // 1000
        change = change % 1000
    else:
        change_1000 = 0
    print("{}원 지폐: {}장".format(50000, chage_50000))
    print("{}원 지폐: {}장".format(10000, change_10000))
    print("{}원 지폐: {}장".format(5000, change_5000))
    print("{}원 지폐: {}장".format(1000, change_1000))


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)