# ~ sec_pro=[[],[],[],[],[]]# 初始的sec_pro列表格式
# ~ sec_pro[0]=[A, Asx, Asy, Ixx, Iyy, Izz]
# ~ sec_pro[1]=[cxp, cxm, cyp, cym, Qxb, Qyb, peri_out, peri_in, xc_distance, yc_distance]
# ~ sec_pro[2]=[stress_point_location[0][0], stress_point_location[1][0], stress_point_location[2][0], stress_point_location[3][0], stress_point_location[0][1], stress_point_location[1][1], stress_point_location[2][1], stress_point_location[3][1]]
# ~ sec_pro[3]=[HT, BT, T1, T2]
# ~ sec_pro[4]=[ZZ1, ZZ3, tw]

file_name='template.mct'# 模板文件
with open(file_name, 'r') as file_template:
	data=file_template.readlines()# 读取文件字符串内容做为原始数据列表

bridge_width= 49.96# 桥面宽度
web_quantity= 10# 腹板数量
web_thickness= 0.8# 腹板厚度
beam_hight= 2# 梁高

'''# 修改节点开始'''
# 初始节点坐标
node_x=list(range(86))
node_num=len(node_x)
node_z=[0 for i in range(node_num)]
node_z[-4]=-beam_hight# 后4项为虚拟支座节点
node_z[-3]=-beam_hight
node_z[-2]=-beam_hight
node_z[-1]=-beam_hight
# 建立节点坐标字符串列表
node_insert=list(range(node_num))# 初始所有节点项
for i in range(node_num):# 逐项修改节点坐标字符串
	node_insert[i]='     {node_ser}, {node_x}, 0, {node_z}\n'.format(node_ser=i+1, node_x=node_x[i], node_z=node_z[i])
# 修改列表节点坐标项
data[28:28+node_num]=node_insert# 节点坐标始于第28项

'''# 修改节点完成'''

def ins_list(a,b,c):# 定义函数在列表c的指定位置a开始逐项插入列表b的项
	# 输入参数为：列表插入起始位置a，要插入的列表b，被修改列表c
	for i in range(len(b)):
		j=i+a
		c.insert(j,b[i])# 逐项插入
	return c# 返回修改后的列表
	
'''# 建立截面特性'''
# 初始截面特性
sec_pro=[[],[],[],[],[]]
sec_pro[0]=[10, 11, 12, 13, 14, 15]
sec_pro[1]=[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
sec_pro[2]=[30, 31, 32, 33, 34, 35, 36, 37]
sec_pro[3]=[40, 41, 42, 43]
sec_pro[4]=[51, 52, 53]
# 建立截面特性字符串列表
sec_pro_insert=['', '', '', '', '']# 初始截面特性列表块
sec_pro_insert[0]='       {AREA}, {ASy}, {ASz}, {Ixx}, {Iyy}, {Izz}\n'.format(AREA=sec_pro[0][0], ASy=sec_pro[0][1],  ASz=sec_pro[0][2], Ixx=sec_pro[0][3], Iyy=sec_pro[0][4], Izz=sec_pro[0][5])
sec_pro_insert[1]='       {Cyp}, {Cym}, {Czp}, {Czm}, {Qyb}, {Qzb}, {PERI_OUT}, {PERI_IN}, {Cy}, {Cz}\n'.format(Cyp=sec_pro[1][0], Cym=sec_pro[1][1],  Czm=sec_pro[1][2], Czp=sec_pro[1][3], Qyb=sec_pro[1][4], Qzb=sec_pro[1][5],PERI_OUT=sec_pro[1][6], PERI_IN=sec_pro[1][7], Cy=sec_pro[1][8], Cz=sec_pro[1][9])
sec_pro_insert[2]='       {Y1}, {Y2}, {Y3}, {Y4}, {Z1}, {Z2}, {Z3}, {Z4}\n'.format(Y1=sec_pro[2][0], Y2=sec_pro[2][1],  Y3=sec_pro[2][2], Y4=sec_pro[2][3], Z1=sec_pro[2][4], Z2=sec_pro[2][5],Z3=sec_pro[2][6], Z4=sec_pro[2][7])
sec_pro_insert[3]='       {HT}, {BT}, {T1}, {T2}\n'.format(HT=sec_pro[3][0], BT=sec_pro[3][1], T1=sec_pro[3][2], T2=sec_pro[3][3])
sec_pro_insert[4]='       YES, {ZZ1}, {ZZ3}, YES, , YES, , YES, , [tw], YES, , YES, , YES,\n'.format(ZZ1=sec_pro[4][0], ZZ3=sec_pro[4][1], tw=sec_pro[4][2])
# 插入截面特性列表
sec_pro_start=425# 截面特性首行位置
data=ins_list(sec_pro_start, sec_pro_insert, data)# 执行函数插入截面特性列表

'''# 建立截面轮廓'''
# 初始截面外轮廓
sec_opoly=[]
# 建立截面外轮廓字符串列表
sec_opoly_insert=[[],[],[],[]]
sec_opoly_insert[0]='       OPOLY={X1}, {Y1}, {X2}, {Y2}, {X3}, {Y3}, {X4}, {Y4}\n'.format(x1=sec_poly[0][0], y1=sec_poly[0][1], x2=sec_poly[1][0], y2=sec_poly[1][1], x3=sec_poly[2][0], y3=sec_poly[2][1], x4=sec_poly[3][0], y4=sec_poly[3][1])
sec_opoly_insert[1]='             {X5}, {Y5}, {X6}, {Y6}, {X7}, {Y7}\n'.format(x5=sec_poly[4][0], y5=sec_poly[4][1], x6=sec_poly[5][0], y6=sec_poly[5][1], x7=sec_poly[6][0], y7=sec_poly[6][1])
sec_opoly_insert[2]='             {X8}, {Y8}, {X9}, {Y9}, {X10}, {Y10}\n'.format(x8=sec_poly[7][0], y8=sec_poly[7][1], x9=sec_poly[8][0], y9=sec_poly[8][1], x10=sec_poly[9][0], y10=sec_poly[9][1])
sec_opoly_insert[3]='             {X11}, {Y11}, {X12}, {Y12}\n'.format(x11=sec_poly[10][0], y11=sec_poly[10][1], x12=sec_poly[11][0], y12=sec_poly[11][1])

# 修改截面内轮廓






'''# 生成.mct模型文件'''
project_name='test.mct'# 模型文件名，即midas软件的.mct文件
# ~ with open(project_name, 'w') as file_object:
	# ~ file_object.writelines(data)


'''# 以3*30m变宽现浇箱梁为例分析.mct文件'''
# 节点：主梁节点第29~110行，支座节点第111~114行，行前5个空格，每行数据：iNO, X, Y, Z
# 单元：第121~201行，可不做修改
# 截面特性：第425~465行，共41行，定义控制截面
# 			第1行：行首1个空格，名称数据：SECT=   1（编号）, PSC（类型）       , D0#0（名称）              , CT, 0, 0, 0, 0, 0, 0, YES, NO, VALU, NO, NO, 
# 			第2行：行首7个空格，特性数据1：AREA, ASy, ASz, Ixx, Iyy, Izz
# 			第3行：行首7个空格，特性数据2：Cyp, Cym, Czp, Czm, Qyb, Qzb, PERI_OUT, PERI_IN, Cy, Cz
# 			第4行：行首7个空格，特性数据3：Y1, Y2, Y3, Y4, Z1, Z2, Z3, Z4
# 			第5行：行首7个空格，特性数据4：HT, BT, T1, T2
# 			第6行：行首7个空格，特性数据5：YES, 0.42, 1.52, YES, , YES, , YES, , 0.25, YES, , YES, , YES,
# 			第7行：行首7个空格，外框数据1：OPOLY=X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第8行：行首7+6个空格，外框数据2：X5, Y5, X6, Y6, X7, Y7
#			第9行：行首7+6个空格，外框数据3：X8, Y8, X9, Y9, X10, Y10
#			第10行：行首7+6个空格，外框数据4：X11, Y11, X12, Y12
#			第11行：行首7个空格，内框1小箱数据：IPOLY=X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第12行：行首7+6个空格，内框1小箱数据：X5, Y5, X6, Y6, X7, Y7
#			第13行：行首7个空格，内框2数据：IPOLY=X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第14行：行首7+6个空格，内框2数据：X5, Y5, X6, Y6, X7, Y7
#			第15行：行首7+6个空格，内框2数据：X8, Y8
#			第16行：行首7个空格，内框3数据：IPOLY=X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第17行：行首7+6个空格，内框3数据：X5, Y5, X6, Y6, X7, Y7
#			第18行：行首7+6个空格，内框3数据：X8, Y8
# 			》》》
#			第40行：行首7个空格，内框-1小箱数据：IPOLY=X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第41行：行首7+6个空格，内框-1小箱数据：X5, Y5, X6, Y6, X7, Y7
# 截面特性：第1~14控制截面,共14个	
# 			》》》
# 截面特性：第999~1077行，共79行，定义变截面
# 			第1行：行首1个空格，名称数据：SECT=   15（编号）, TAPERED（类型）       , D0#0（名称）           , CT, 0, 0, 0, 0, 0, 0, 0, 0, YES, NO, VALU, 1, 1, NO, NO, 
# 			第2行：行首7个空格，首端特性数据1：AREA, ASy, ASz, Ixx, Iyy, Izz
# 			第3行：行首7个空格，首端特性数据2：Cyp, Cym, Czp, Czm, Qyb, Qzb, PERI_OUT, PERI_IN, Cy, Cz
# 			第4行：行首7个空格，首端特性数据3：Y1, Y2, Y3, Y4, Z1, Z2, Z3, Z4
# 			第5行：行首7个空格，尾端特性数据1：AREA, ASy, ASz, Ixx, Iyy, Izz
# 			第6行：行首7个空格，尾端特性数据2：Cyp, Cym, Czp, Czm, Qyb, Qzb, PERI_OUT, PERI_IN, Cy, Cz
# 			第7行：行首7个空格，尾端特性数据3：Y1, Y2, Y3, Y4, Z1, Z2, Z3, Z4
# 			第8行：行首7个空格，特性数据4：首端HT, BT, T1, T2， 尾端HT, BT, T1, T2
# 			第9行：行首7个空格，特性数据5：首端YES, 0.42, 1.52, YES, , YES, , YES, , 0.25, YES, , YES, , YES, 尾端YES, 0.42, 1.52, YES, , YES, , YES, , 0.25, YES, , YES, , YES,
# 			第10行：行首7个空格，首端外框数据1：OPOLY=YES, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第11行：行首7+6个空格，首端外框数据2：X5, Y5, X6, Y6, X7, Y7
#			第12行：行首7+6个空格，首端外框数据3：X8, Y8, X9, Y9, X10, Y10
#			第13行：行首7+6个空格，首端外框数据4：X11, Y11, X12, Y12
#			第14行：行首7个空格，首端内框1小箱数据：IPOLY=YES, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第15行：行首7+6个空格，首端内框1小箱数据：X5, Y5, X6, Y6, X7, Y7
#			第16行：行首7个空格，首端内框2数据：IPOLY=YES, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第17行：行首7+6个空格，首端内框2数据：X5, Y5, X6, Y6, X7, Y7
#			第18行：行首7+6个空格，首端内框2数据：X8, Y8
#			第19行：行首7个空格，首端内框3数据：IPOLY=YES, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第20行：行首7+6个空格，首端内框3数据：X5, Y5, X6, Y6, X7, Y7
#			第21行：行首7+6个空格，首端内框3数据：X8, Y8
# 			》》》
#			第43行：行首7个空格，首端内框-1小箱数据：IPOLY=YES, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第44行：行首7+6个空格，首端内框-1小箱数据：X5, Y5, X6, Y6, X7, Y7
# 			第45行：行首7个空格，尾端框数据1：OPOLY=N0, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第46行：行首7+6个空格，尾端外框数据2：X5, Y5, X6, Y6, X7, Y7
#			第47行：行首7+6个空格，尾端外框数据3：X8, Y8, X9, Y9, X10, Y10
#			第48行：行首7+6个空格，尾端外框数据4：X11, Y11, X12, Y12
#			第49行：行首7个空格，尾端内框1小箱数据：IPOLY=N0, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第50行：行首7+6个空格，尾端内框1小箱数据：X5, Y5, X6, Y6, X7, Y7
#			第51行：行首7个空格，尾端内框2数据：IPOLY=N0, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第52行：行首7+6个空格，尾端内框2数据：X5, Y5, X6, Y6, X7, Y7
#			第53行：行首7+6个空格，尾端内框2数据：X8, Y8
#			第54行：行首7个空格，尾端内框3数据：IPOLY=N0, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第55行：行首7+6个空格，尾端内框3数据：X5, Y5, X6, Y6, X7, Y7
#			第56行：行首7+6个空格，尾端内框3数据：X8, Y8
# 			》》》
#			第78行：行首7个空格，尾端内框-1小箱数据：IPOLY=N0, X1, Y1, X2, Y2, X3, Y3, X4, Y4
#			第79行：行首7+6个空格，尾端内框-1小箱数据：X5, Y5, X6, Y6, X7, Y7
# 截面特性：第15~27变截面，共13个
