# 여기에 코드를 작성하세요
count = 0
n = 120
i = 1
while i <= n:
    if n % i == 0:
        print(i)
        count += 1
    i += 1
print("{}의 약수는 총 {}개입니다.".format(120, count))