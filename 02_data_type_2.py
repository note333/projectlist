#리스트타입
# print("list")
# list_a=[1,2,3]
# print(list_a)
#
# # index=0부터시작
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
#
# print(type([1,2,3]))
#
# # slice
# print(list_a[0:2])
#
# # append
# list_a.append(4)
# print(list_a)
#
# # remove
# list_a.remove(2)
# print(list_a)
#
# #clear
# list_a.clear()
# print(list_a)
#
#
# #tuple타입
# print("tuple")
# tuple_a=(1,2,3)
# print(tuple_a)
# print(type(tuple_a))
# tuple_a.append(4)


#dict(map) {}
#key : value

# dict_a={"apple" : "a type of fruits",
#     "pen" : "a thing to write"
# }
# print(dict_a)
# print(dict_a["apple"])
# #edit value
# dict_a["pen"]="something to write"
# print(dict_a)


#set set([])
set_a=set([1,2,3])
set_b=set([2,4,6])
print(set_a)
print(set_b)

#집합 - 교집합(&), 합집합(|), 차집합(-), 여집합
#중복 제거
print(set_a&set_b)
print(set_a|set_b)
print(set_a-set_b)
