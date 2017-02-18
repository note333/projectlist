import random



# question()

list_A=["오복한식당", "김밥천국", "라면사랑"]
list_B=["양평관", "북경반점", "니하오"]
list_C=["스시박사", "아리가또", "고자이마스"]

while True:
    answer=input("한식,중식,일식 중 한가지를 입력하세요")
    if answer=="한식":
        print(random.choice(list_A))
        break
    elif answer=="중식":
        print(random.choice(list_B))
        break
    elif answer=="일식":
        print(random.choice(list_C))
        break
    else:
        continue
