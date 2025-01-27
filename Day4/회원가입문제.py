'''
아이디
비밀번호

아이디는 내 영문 이름
비밀번호는 1234
'''

ID = input("아이디를 입력하시오 : ")
PW = int(input("비밀번호를 입력하시오 : "))

if ID == "Song ji min" and PW == 1234 :
    print("로그인 되었습니다.")
elif ID != "Song ji min" and PW == 1234:
    print("아이디를 확인해주세요")
elif ID == "Song ji min" and PW != 1234:
    print("비밀번호를 확인해주세요")
else:
    print("아이디 비밀번호 불일치 회원가입하러 가기")

is_raning = input("비가 오나요? (예 / 아니오) : ")
if is_raning == "예":
    print("우산을 챙기세요")
else:
    print("우산은 필요 없습니다")