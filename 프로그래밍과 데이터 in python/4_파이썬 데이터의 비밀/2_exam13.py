def mask_security_number(security_number):
    # 여기에 코드를 작성하세요
    if len(security_number) == 13:
        new_number = security_number[: -4]
        new_number += "****"
        return new_number
    else:
        new_number = security_number[: -4]
        new_number += "****"
        return new_number


# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))