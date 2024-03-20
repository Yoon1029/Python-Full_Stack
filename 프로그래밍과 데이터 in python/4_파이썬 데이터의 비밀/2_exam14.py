def is_palindrome(word):
    # 여기에 코드를 작성하세요
    count = len(word) // 2
    j = 0

    for i in range(count):
        if word[i] == word[j - 1]:
            true_or_false = True
        else:
            return False
        j -= 1
    return True


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))