'''
시리즈 사칙연산
'''

import pandas as pd

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})

print(student1, '\n')
print(student2, '\n')


# 두 학생의 과목별 점수로 사칙연산 수행
addition = student1 + student2          # 덧셈
subtraction = student1 - student2       # 뺄셈
multiplication = student1 * student2    # 곱셈
division = student1 / student2          # 나눗셈
print(type(division), '\n')

# 사칙연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)