with open("data/vocabulary.txt", 'r') as f:
    for line in f:
        problem_list = (line.strip().split(": "))
        problem = problem_list[1]
        answer = problem_list[0]
        input_str = input("{}: ".format(problem))
        if input_str == answer:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(answer))