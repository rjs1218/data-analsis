'''
빈도 그래프
'''

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 스타일 테마 지정
sns.set_style('whitegrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# 기본값
sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1)
# hue 옵션에 'who' 추가
sns.countplot(x='class', palette='Set2', hue='who', data=titanic, ax=ax2)
# dodge=False 옵션 추가(축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x='class', palette='Set3', hue='who', dodge=False, data=titanic, ax=ax3)

# 차트 제목 표시
ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(staked)')

plt.show()