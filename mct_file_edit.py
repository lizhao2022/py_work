# ~ sec_pro=[[],[],[],[],[]]
# ~ sec_pro[0]=[A, Asx, Asy, Ixx, Iyy, Izz]
# ~ sec_pro[1]=[cxp, cxm, cyp, cym, Qxb, Qyb, peri_out, peri_in, xc_distance, yc_distance]
# ~ sec_pro[2]=[stress_point_location[0][0], stress_point_location[1][0], stress_point_location[2][0], stress_point_location[3][0], stress_point_location[0][1], stress_point_location[1][1], stress_point_location[2][1], stress_point_location[3][1]]
# ~ sec_pro[3]=[HT, BT, T1, T2]
# ~ sec_pro[4]=[ZZ1, ZZ3, tw]

bridge_width= 49.96# 桥面宽度
web_quantity= 10# 腹板数量
web_thickness= 0.8# 腹板厚度
beam_hight= 2# 梁高

def ins_file
ins_start=425# 文件修改起始行
ins_line_num=5# 文件修改行数
for i in range(ins_line_num):
	j=i+ins_start
	data.insert(j,sec_insert[i])# 逐行插入修改
	del data[j+1]# 删除被修改的原行

sec_pro=[[],[],[],[],[]]
sec_pro[0]=[10, 11, 12, 13, 14, 15]
sec_pro[1]=[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
sec_pro[2]=[30, 31, 32, 33, 34, 35, 36, 37]
sec_pro[3]=[40, 41, 42, 43]
sec_pro[4]=[51, 52, 53]



node_line_start=28
node_num1=86
node_x=list(range(86))
node_z=[0 for i in range(86)]
node_z[82]=-beam_hight
node_z[83]=-beam_hight
node_z[84]=-beam_hight
node_z[85]=-beam_hight
node_insert=list(range(node_num1))
# 修改节点x坐标
for i in range(node_num1):
	node_insert[i]='     1, {node_x}, 0, {node_z}\n'.format(node_x=node_x[i], node_z=node_z[i])
	print(node_insert[i])


file_name='template.mct'# 模板文件
with open(file_name, 'r') as file_template:
	data=file_template.readlines()# 读取文件字符串内容做为原始数据列表
	
	
sec_insert=['', '', '', '', '']# 初始截面特性列表块
sec_insert[0]='       {AREA}, {ASy}, {ASz}, {Ixx}, {Iyy}, {Izz}\n'.format(AREA=sec_pro[0][0], ASy=sec_pro[0][1],  ASz=sec_pro[0][2], Ixx=sec_pro[0][3], Iyy=sec_pro[0][4], Izz=sec_pro[0][5])
sec_insert[1]='       {Cyp}, {Cym}, {Czp}, {Czm}, {Qyb}, {Qzb}, {PERI_OUT}, {PERI_IN}, {Cy}, {Cz}\n'.format(Cyp=sec_pro[1][0], Cym=sec_pro[1][1],  Czm=sec_pro[1][2], Czp=sec_pro[1][3], Qyb=sec_pro[1][4], Qzb=sec_pro[1][5],PERI_OUT=sec_pro[1][6], PERI_IN=sec_pro[1][7], Cy=sec_pro[1][8], Cz=sec_pro[1][9])
sec_insert[2]='       {Y1}, {Y2}, {Y3}, {Y4}, {Z1}, {Z2}, {Z3}, {Z4}\n'.format(Y1=sec_pro[2][0], Y2=sec_pro[2][1],  Y3=sec_pro[2][2], Y4=sec_pro[2][3], Z1=sec_pro[2][4], Z2=sec_pro[2][5],Z3=sec_pro[2][6], Z4=sec_pro[2][7])
sec_insert[3]='       {HT}, {BT}, {T1}, {T2}\n'.format(HT=sec_pro[3][0], BT=sec_pro[3][1], T1=sec_pro[3][2], T2=sec_pro[3][3])
sec_insert[4]='       YES, {ZZ1}, {ZZ3}, YES, , YES, , YES, , [tw], YES, , YES, , YES,\n'.format(ZZ1=sec_pro[4][0], ZZ3=sec_pro[4][1], tw=sec_pro[4][2])







project_name='test.mct'# 模型文件名，即midas软件的.mct文件
with open(project_name, 'w') as file_object:
	file_object.writelines(data)

# 以3*30m变宽现浇箱梁为例分析.mct文件
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
