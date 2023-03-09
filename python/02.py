#1
a = int(input())
print(a+2)
# input은 항상 문자형으로 입력받게 됨. 따라서 필요에 따라 정수형 등으로 바꿔주는 작업이 필요함.

#2
n = input()
print(f"Your score is {n} point.")
# f-string 없이 입력했는데 그냥 붙지 않음.

#3
a = int(input())
print(a*2)
# 정수형으로 변환하였기 때문에 

#4
a = int(input())
print(a*2+3)
#연산가능

#5
n = float(input())
print(f"{n:.2f}")
# 반올림하는거 f안썼네

#6
n = float(input())
print(f"{n*30.48:.1f}")
# 연산가능

#7
a = float(input())
print(f"{a+1.5:.2f}")
# 연산가능

#8
a,b = map(int,input().split())
print(a*b)
# 공백을 두고 두 수 입력받아 곱해주기

#9
a,b = map(int,input().split())
print(a+b)
# 위와 같음

#10
a,b = map(int,input().split())
a,b = b,a
print(a,b)
# 두 수 위치 바꿔주기

#11
a,b = map(int,input().split())
print(a,b,a+b)

#12
