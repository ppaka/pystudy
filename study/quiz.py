_question = ["대한민국의 수도는?", "중국의 수도는?", "미국의 수도는?", "호주의 수도는?"]
_rightAnswer = ["서울", "베이징", "워싱턴", "캔버라"]

for i in range(4):
    x = input(f"{_question[i]}: ")

    if x == _rightAnswer[i]:
        print("정답입니다")
    else:
        print("오답입니다")
