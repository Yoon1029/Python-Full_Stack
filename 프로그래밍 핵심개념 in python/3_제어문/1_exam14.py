# 여기에 코드를 작성하세요

basis_num = 1
second_num = 1
new_num = 0
i = 0
while i < 50:
    if i < 2:
        print(basis_num)
    else:
        new_num = basis_num + second_num
        print(new_num)
        if i % 2 != 0:
            basis_num = new_num
        else:
            second_num = basis_num + second_num
    i += 1

# 모범 답안
"""previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1"""
