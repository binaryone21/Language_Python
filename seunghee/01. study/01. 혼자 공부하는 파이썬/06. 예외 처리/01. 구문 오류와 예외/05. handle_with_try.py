# try except 구문으로 예외를 처리합니다.
try :
    # 숫자를 변홥합니다.
    number_input = int(input("정수 입력 > "))

    # 출력합니다.
    print("원의 반지름 :", number_input)
    print("원의 둘레 :", 2 * 3.14 * number_input)
    print("원의 넓이 :", 3.14 * number_input ** 2)
except :
    print("무언가 잘못되었습니다.")