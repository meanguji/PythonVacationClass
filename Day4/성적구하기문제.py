'''
점수 입력받기
90점 이상이면 A학점 참 잘했어요!
80점 이상이면 B
70점 이상이면 C
그렇지 않다면 F학점으로 재시험
'''

score = int(input("점수를 입력하시오:"))

if score > 90:
    print(f"{score}점수는 학점 참 잘했어요!")
elif 80 < score :
    print(f"{score}점수는 B학점")
elif 70 < score :
    print(f"{score}점수는 C학점")
else :
    print(f"{score}점수는 재시험")




'''
사용자가 좋아하는 달을 입력받음
3,4,5 = 봄
6,7,8 = 여름
9,10,11 = 가을
12,1,2 = 겨울
'''

month = int(input("사용자가 좋아하는 달은?"))

if  3<= month <=5 :
    print(f"{month}월은 봄")
elif 6 <= month <= 8 :
    print(f"{month}월은 여름")
elif 9 <= month <= 11:
    print(f"{month}월은 가을")
else :
    print(f"{month}월은 겨울")


