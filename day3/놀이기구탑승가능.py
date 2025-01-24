'''
사용자에게 키와 나이를 입력받을 것
키가 120 이상, 나이가 10살 이상이어야만 놀기기구를 탈 수 있다.

놀이기구를 탈 수 있나요? True / False
'''

height = int(input("키를 입력하세요:"))
age = int(input("나이를 입력하세요:"))

can_ride = height >= 120 and age >= 10
print(f"놀이기구를 탈 수 있나요?{can_ride}, {height}는 가능") #f라는 의미는 포멧이라는 의미라고 인식하여 중괄호를 통해 모든 변수를 감지 할 수 있다.

