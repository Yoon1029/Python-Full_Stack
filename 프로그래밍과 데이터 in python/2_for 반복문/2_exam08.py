numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 여기에 코드를 작성하세요
i = int(len(numbers) / 2)
k = 0
for j in range(0, i):
    temp = numbers[j]
    numbers[j] = numbers[k - 1]
    numbers[k - 1] = temp
    k -= 1

print("뒤집어진 리스트: " + str(numbers))