# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:35:31 2018

@author: jooho
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# matplotlib 3d              
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3d 그리기 위해 필요한 함수
import seaborn as sns
plt3d = plt.figure().gca(projection='3d') # 3d로 출력하라는 설정

# 데이터 로딩
iris = sns.load_dataset('iris')

# 데이터 플랏
plt3d.scatter(iris['sepal_length'],iris['sepal_width'], iris['petal_length'])
plt3d.set_title('3d plot')
plt3d.set_xlabel('sepal_length')
plt3d.set_ylabel('sepal_width')
plt3d.set_zlabel('petal_length')


# plotly 3d
# 웹브라우저 기반으로 3d를 회전시켜보거나, 확대 등의 기능이 있음
# spyder에서 실행하는 코드로 작성
# 쥬피터 활용 위해서는 plotly 회원 가입 등 필요
import plotly.graph_objs as go
import plotly.offline as off

# 데이터 로드
import seaborn as sns
iris = sns.load_dataset('iris')

# 3d 데이터 입력
trace = go.Scatter3d(x=iris['sepal_length'], y=iris['sepal_width'],
                    z=iris['petal_length'],
                    mode='markers',   # 이것을 삭제하면 선그래프가 함께 그려짐                    
                    marker=dict(size=2)
                    )    # 기본 사이즈가 너무 크게 나옴

# 포인트 양식 지정
# 뒤의 type과 mode 삭제하면 점이 너무 크고 선으로 점들이 이어짐
data = [trace]
layout = dict(title='Iris Dataset')
fig = dict(data=data, layout=layout)
off.plot(fig, filename='3dplot.html')

