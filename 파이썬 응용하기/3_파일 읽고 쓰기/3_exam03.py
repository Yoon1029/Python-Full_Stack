with open("data/vocabulary.txt", "a") as f:

    while 1:
        english_word = input("영어 단어를 입력하세요: ")
        if english_word == 'q':
            break
        mean = input("한국어 뜻을 입력하세요: ")
        if mean == 'q':
            break
        f.write("{}: {} \n".format(english_word, mean))

