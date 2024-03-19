# 여기에 코드를 작성하세요

# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

year = 2016 - 1988
bank = 50000000

while year != 0:
    bank = bank * (1 + INTEREST_RATE)
    year -= 1
if APARTMENT_PRICE_2016 > int(bank):
    change = APARTMENT_PRICE_2016 - int(bank)
    print("{}원 차이로 {} 말씀이 맞습니다.".format(change, "미란 아줌마"))
elif int(bank) > APARTMENT_PRICE_2016:
    change = int(bank) - APARTMENT_PRICE_2016
    print("{}원 차이로 {} 말씀이 맞습니다.".format(change, "동일 아저씨"))
else:
    print("두 값은 같습니다.")