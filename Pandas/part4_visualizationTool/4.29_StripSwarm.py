'''
범주형 데이터의 산점도
'''

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 스타일 테마 설정
sns.set_style('whitegrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 이산형 변수의 분포 - 데이터 분산 미고려(중복 표시 O)
sns.stripplot(x='class',        # x축 변수
            y='age',            # y축 변수
            data=titanic,       # 데이터셋 - 데이터프레임
            ax=ax1)             # axe 객체 - 1번째 그래프

# 이산형 변수의 분포 - 데이터 분산 고려(중복 표시 X)
sns.swarmplot(x='class',
            y='age',
            data=titanic,
            ax=ax2)

ax1.set_title('Strip Plot')
ax2.set_title('Swarm Plot')

plt.show()