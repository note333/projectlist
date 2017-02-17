#사용자에게 몇단을 출력할것인지 받을것
#해당단을 곱하기1~9까지 실행할것
name=int(input("몇단을 출력하시겠습니까"))
for num in range(1,10):
    print("{}*{}={}".format(name,num,name*num))
