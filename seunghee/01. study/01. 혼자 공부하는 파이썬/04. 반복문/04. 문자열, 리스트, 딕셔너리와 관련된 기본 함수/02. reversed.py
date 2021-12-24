# 리스트를 선언하고 뒤집습니다.
arr = [1, 2, 3, 4, 5]
arr_reversed = reversed(arr)

# 출력합니다.
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]) :", arr_reversed)
print("list(reversed([1, 2, 3, 4, 5]) :", list(arr_reversed))

# 반복문을 적용해 봅니다.
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]) : ")
for i in reversed(arr) :
    print("-", i)