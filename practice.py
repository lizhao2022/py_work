f_r=[[0]+[30]*10+[0]]*5# 腹板束弯曲半径
fra=[20, 20, 15, 10, 6]
for i in range(5):
	f_r[i][3:5]=[fra[i]]*2
	f_r[i][7:9]=[fra[i]]*2
	print(f_r[i])
