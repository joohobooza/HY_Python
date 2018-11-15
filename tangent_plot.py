# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:28:53 2018

@author: jooho
"""

# import library
import matplotlib.pyplot as plt
import numpy as np

# x,y 값을 지정
x = np.arange(-10.0, 10.0, 0.001)
y = np.tan(x)

# tangent는 무한대 값이 있으므로 그리기 위해서
# 출력할 y값의 한도를 정한다. 
ylim = 10

# 출력할 y값보다 큰 값을 nan을 넣어준다. (데이터 삭제)
y[y > ylim] = np.nan
y[y < -ylim] = np.nan

# 출력을 한다. 
plt.plot(x, y)
