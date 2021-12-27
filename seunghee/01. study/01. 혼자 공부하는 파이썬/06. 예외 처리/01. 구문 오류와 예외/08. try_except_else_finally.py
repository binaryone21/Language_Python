# try except else 구문으로 예외를 처리합니다.
try :
    # 숫자로 변환합니다.
    number_input = int(input("정수 입력 > "))

    # 출력합니다.
    print("원의 반지름 :", number_input)
    print("원의 둘레 :", 2 * 3.14 * number_input)
    print("원의 넓이 :", 3.14 * number_input ** 2)
except :
    print("정수를 입력하지 않았습니다.")
else :
    print("예외가 발생하지 않았습니다.")
finally :
    print("프로그램이 종료되었습니다.")