'''
시리즈를 숫자로 나누기
'''

import pandas as pd

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1, '\n')


# 200으로 나누기
percentage = student1/200

print(percentage, '\n')
print(type(percentage))