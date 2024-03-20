# 자리수 합 리턴
def sum_digit(num):
    # 여기에 코드를 작성하세요
    str_num = str(num)
    sum = 0
    i = len(str_num)
    for count in range(0, i):
        sum += int(str_num[count])
    return sum
# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 여기에 코드를 작성하세요
sum = 0

for i in range(1, 1001):
    sum += sum_digit(i)
print(sum)