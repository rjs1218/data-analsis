'''
특정 열을 행 인덱스로 설정
'''

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}


df = pd.DataFrame(exam_data)
print(df, '\n')

# 특정 열을 데이터프레임의 행 인덱스로 설정
ndf = df.set_index(['이름'])
print(ndf, '\n')

ndf2 = ndf.set_index('음악')
print(ndf2, '\n')

ndf3 = ndf.set_index(['수학', '음악'])
print(ndf3)