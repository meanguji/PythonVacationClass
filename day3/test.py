'''
1. and : 연산자를 기준으로 왼쪽과 오른쪽 값이 모두 true 일때만 True를 반환
2. or : 연산자를 기준으로 왼쪽과 오른쪽 값 중에 하나라도 True 이면 True를 반환
3. not : 뒤에 따라오는 논리값이 True이면 False를 반환(반대로 출력)
         True라면 False를 Flase라면 True를 반환 (단항연산자)
'''

num1 = 10
num2 = 20
num3 = 30

num_result = num1 < num2 and num2 < num3
print(num_result)

num_result2 = num1 > num2 and num2 < num3
print(num_result2)

num_result3 = num1 > num2 or num2 < num3
print(num_result3)

num_result4 = num1 > num2 or num2 > num3
print(num_result4)

false = False
print(false)
print(not false)
print(false) #변수 false의 값은 바뀌지 않으나 'not' 연산자에 의해서 값이 바뀌어 출력된다

'''
빈 문자열을 선언 후
해당 문자열이 비어있다면 True를 출력하는 프로그램 만들기
'''

name = ""
print (not name)
print (name)

'''
15라는 숫자가 10 이상 20 이하 인지 확인
'''

number = 15
number_result = 10<= number <=20
print(number_result)
