'''
나이가 10보다 작으면 어린이 출력
20보다 작으면 10대 출력
30보다 작으면 20대 출력
40보다 작으면 30대 출력
'''

age = int(input("나이를 입력하시오:"))

if age < 10 :
    print("어린이")

if 10 <= age < 20 :
    print("10대")

if 20 <= age < 30 :
    print("20대")

if 30 <= age < 40 :
    print("30대")

else:
    print("40대 이상입니다")

