# 변수를 선언합니다.
list_input = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다.
output_a = map(lambda x : x**2, list_input)
print("# map() 함수의 실행결과")
print("map(power, list_input_a) :", output_a)
print("map(power, list_input_a) :", list(output_a))
print()

# filter() 함수를 사용합니다.
output_b = filter(lambda x : x<3, list_input)
print("# filter() 함수의 실행결과")
print("filter(unser_3, list_input_a): ", output_b)
print("filter(unser_3, list_input_a): ", list(output_b))