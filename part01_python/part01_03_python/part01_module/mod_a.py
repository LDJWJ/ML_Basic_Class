# -*- coding: utf-8 -*-

# 전진, 후진
# mod_a.py
# 모듈.

# 일정 거리만큼 전진 
def forward(loc, d):
    return loc + d

# 일정 거리만큼 후진
def backward(loc, d):
    return loc - d



## 3만큼 전진
p_loc = forward(0, 3)
print( "현재 위치 : ", p_loc ) # 3만큼 전진