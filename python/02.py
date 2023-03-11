#입출력
#1
a = int(input())
print(a+2)
# input은 항상 문자형으로 입력받게 됨. 따라서 필요에 따라 정수형,실수형 등으로 바꿔주는 작업이 필요함.

#2
n = input()
print(f"Your score is {n} point.")
# f-string 없이 입력했는데 그냥 붙지 않음.
#아니면 다 따로 따로 " " + " " + " " 해야 함.

#3
a = int(input())
print(a*2)
# 정수형으로 변환하였기 때문에 숫자 2와 바로 곱할 수 있음

#4
a = int(input())
print(a*2+3)

#5
n = float(input())
print(f"{n:.2f}")

#6
n = float(input())
print(f"{n*30.48:.1f}")

#7
a = float(input())
print(f"{a+1.5:.2f}")

#8
a,b = map(int,input().split())
print(a*b)
# 공백을 두고 두 수 입력받아 곱해주기

#9
a,b = map(int,input().split())
print(a+b)

#10
a,b = map(int,input().split())
a,b = b,a
print(a,b)

#11
a,b = map(int,input().split())
print(a,b,a+b)

#12
a = int(input())
b = int(input())
print(a*b)

#13
a = int(input())
b = int(input())
print(a,b)

#14
a = float(input())
b = float(input())
print(f"{a+b:.2f}")

#15
a = float(input())
b = float(input())
c = float(input())
print(f"{a:.3f}")
print(f"{b:.3f}")
print(f"{c:.3f}")

#16
a,b = map(int,input().split())
c = int(input())
print(a,b,c)

#17
c = input()
print(c)
#문자열 입력받아 그대로 출력하기/""등 기호 필요없음

#18
s = input()
print(s)

#19
c = input()
a = float(input())
b = float(input())
print(c)
print(f"{a:.2f}")
print(f"{b:.2f}")

#20
s = input()
t = input()
print(t)
print(s)

#21
h,m = map(int(input().split(":")))
print(h+1,m sep=":")

#22
inp = input()
arr = inp.split(":")
h = int(arr[0])
m = int(arr[1])
print(f"{h+1}:{m}")
# 문자열 자체를 입력받아 split("기호")를 기준으로 나눠주면 리스트처럼 각 인덱스가 생긴다. 각 인덱스에 변수를 부여해주고 정수형인 값들과 문자인 기호를 f-string으로 한 번에 출력시킨다.

#23
inp = input()
arr = inp.split("-")
mm = int(arr[0])
dd = int(arr[1])
yyyy = int(arr[2])
print(f"{yyyy}.{mm}.{dd}")

#24
inp = input()
arr = inp.split("-")
a = int(arr[0])
b = int(arr[1])
print(f"{a}{b}")
#이어서 출력하기

#25
inp = input()
arr = inp.split(".")
yyyy = int(arr[0])
mm = int(arr[1])
dd = int(arr[2])
print(f"{mm}-{dd}-{yyyy}")

#26
inp = input()
arr = inp.split("-")
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
print(f"0{a}-{c}-{b}")
#해설은 출력 때 {a}대신 010 자체를 써줬는데
# 왜 {a}가 아니라 0{a}를 써줘야지? 0이 안되나? 그냥 오류인가?