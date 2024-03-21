import random

dict = {}
total_problem_list = []

with open("data/vocabulary.txt", 'r') as f:
    for line in f:
        problem_list = (line.strip().split(": "))
        problem = problem_list[1]
        answer = problem_list[0]
        total_problem_list.append(problem)
        dict[problem] = answer

while True:
    random_problem_num = random.randint(0, len(total_problem_list) - 1)
    random_problem = total_problem_list[random_problem_num]
    input_str = input("{}: ".format(random_problem))
    if input_str == dict[random_problem]:
        print("정답입니다.")
    elif input_str == 'q':
        break
    else:
        print("틀렸습니다. 정답은 {}입니다.".format(dict[random_problem]))