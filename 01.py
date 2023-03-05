# ============================== 기본 출력

#1
print("Hello")
# 문자열은 큰 따옴표가 없으면 출력되지 않는가? -- 안됨

#2
print("He says \"It's a really simple sentence\".")
# 출력 시 필요한 큰 따옴표나 작은 따옴표가 출력과 겹치면 역슬래시 활용

#3
print("Hello\nWorld")
# 줄바꿈이 필요할 땐 print*2가 아니라 개행문자 \n을 기억하자!

#4
print(3)
# 숫자는 따옴표 없이 출력 가능 / "3" 큰 따옴표 포함해도 출력 가능하지만 문자열이 되어버린다는 것을 잊지 말자!

#5
print(3,5)
# 3 5 / ,를 사이에 둔 숫자는 공백을 두고 출력이 됨 / sep=""을 이용해 공백을 표현할 수도 있고, sep=":"등의 기호로 구분하여 출력할 수도 있다.

#6
print("Let's go LeebrosCode!")
# 한 줄 출력 연습

#7
print("Hello students!\nWelcome to LeebrosCode!")
# 두 줄 출력 연습

#8
print("Total days in Year\n365\nCircumference rate\n3.1415926535")
# 여러 줄 출력 / 숫자, 문자 혼합

# ============================================ 변수와 자료형
#9
a = 97
b = 13
print(a,'-',b,'=',a-b)
# 97 - 13 = 84 라는 값을 얻기 위해서 'a-b='까지 묶어야한다고 생각했는데 +가 아닌 ,를 통해 공백을 두고 출력할 수 있었고, 마지막 값만 연산을 통해 해결하는 거였음

#10
a = 3
b = 'C'
print(a)
print(b)
# 대문자와 소문자를 잘 보자. a\nb 'a'\n'b' 이 난리까지 갔음

#11
a = 26
b = 5
print(a,'*',b,'=',a*b)
# 9번과 같음. 연산은 +,-,*,/ 모두 가능. 하지만 문자형과 숫자형을 잘 구분지을 것.

#12
a = 7
b = 23
c = 30
print(f"{a} + {b} = {c}")
# f-string 활용하기. 띄어쓰기도 문장 내에서 적용됨.

#13
a = 3
b = 'C'
print(f"{3}...{b}")
# 중간에 ... 삽입하기. 문자열 b도 그냥 {b}를 써주면 됨.

#14
a = 3
b = 'C'
print(f"{b}!.....!{a}")
# 13번과 같음

#15
a = 1
b = 2
c = 'C'
print(f"{a}->{b}->{c}")
# 13번과 같음

#16
a = 13
b = 0.165
print(f"{a} * {b:.6f} = {a*b:.6f}")
# 실수형 소숫점 아래 몇자리까지만 반올림하여 나타내기 {변수:.nf} (n에 숫자 넣으면 됨)

#17
a = 25.352
print(f"{a:.1f}")
# 위와같음

#18
a = 30.48
b = 160934
print(f"9.2ft = {9.2*a:.1f}cm")
print(f"1.3mi = {1.3*b:.1f}cm")
# f-string {}안에서 연산도 가능하다.

#19
a = 5.26
b = 8.27
print(f"{a*b:.3f}")
# 위와 같음

#20
a = 3
a = 6
print(a)
# 변수를 다시 할당할 수 있음

#21
a = 7
a = 4
print(a)
# 위와같음

#22
a = 'C'
a = 'T'
print(a)
# 문자 변수에 할당해주기

#23
a = 5
b = 3
a = b
print(a)
print(b)
# 변수에 할당된 값을 넣을 수도 있음

#24
a = 2
b = 6
a = b
print(a)
print(b)
# 위와 같음

#25
a = 3
b = 4
b = a
print(a,b)
print(a*b)
# 연산도 가능

#26
a = 3
b = 5
a,b = b,a
print(a)
print(b)
# 5,3이 순서대로 출력되게 하는 법

#27
a = 2
b = 5
a,b = b,a
print(a)
print(b)
# 위와 같음

#28
a,b,c = 5,6,7
a = c
print(a)
a,b,c = 5,6,7
b = a
print(b)
a,b,c = 5,6,7
c = b
print(c)
# 엥두 하나씩 새로 써주는 거였음

#29
a,b,c = 1,2,3
a = b = c
print(a,b,c)
# 공백을 사이에 두고 출력/가장 마지막에 할당된 것부터 왼쪽으로 할당됨

#30
a,b,c = 5,6,7
a=b=c
print(a,b,c)
# 위와 같음

#31
a,b,c = 1,2,3
d = a+b+c
a=b=c=d
print(a,b,c)
# 세 수의 합을 동일하게 할당하여 공백을 두고 출력