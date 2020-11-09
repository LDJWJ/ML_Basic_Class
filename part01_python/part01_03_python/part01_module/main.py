# -*- coding: utf-8 -*-

 # seaborn을 불러와서 약자 sns라 쓰겠다.
# import seaborn as sns 
# data = sns.load_dataset("tips") # 데이터 불러오기()
# print( data )

#%%  # 주피터 노트북의 셀을 만들겠다.
import mod_a
p_loc = 0
p_loc = mod_a.forward(p_loc,5)
p_loc = mod_a.backward(p_loc, 4)
print("현재 위치는 ", p_loc)

#%% 다른 방법으로 불러와 보기
from mod_a import forward, backward

p_loc = 0
p_loc = forward(p_loc, 5) # 앞으로 5만큼 이동
p_loc = backward(p_loc, 4) # 뒤로 4만큼 이동.

print("현재 위치는 :", p_loc)

#%% 2-2 실행해 보기 (mod_b.py)를 불러오기.
## 현재위치 추가 present_loc(loc)
from mod_b import forward, backward

p_loc = 0
p_loc = forward(p_loc, 10) # 앞으로 10만큼 이동
p_loc = backward(p_loc, 8) # 뒤로 8만큼 이동.

print("현재 위치는 :", p_loc)

#%%
## (추가) 좌, 우 몇도 변경하겠냐?











