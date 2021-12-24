list = [0, 1, 2, 3, 4, 5]
print("#리스트의 요소 하나 제거하기")

# 제거 방법[1] - del
del list[1]
print("del list[1] :", list)

# 제거 방법[2] - pop
list.pop(2)
print("list.pop(2) :", list)
