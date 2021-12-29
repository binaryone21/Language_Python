# 숫자를 입력받습니다.
user_input = input("정수 입력 > ")

# 사용자 입력이 숫자로만 구성되어 있을 때
if user_input.isdigit() :
    # 숫자로 변환합니다.
    number_input = int(user_input)

    # 출력합니다.
    print("원의 반지름 :", number_input)
    print("원의 둘레 :", 2 * 3.14 * number_input)
    print("원의 넓이 :", 3.14 * number_input ** 2)
else :
    print("정수를 입력하지 않았습니다.")