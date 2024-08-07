# 程序用于生成单箱多室截面并计算特性
# 既定：底板厚0.22、顶板倒角1*0.2、底板倒角0.6*0.2
# 输入值：桥面宽度、腹板数量、腹板厚度、梁高
# 输出值：截面线框点坐标、截面特性
import triangle as tr
import numpy as np
import matplotlib.pyplot as plt
import math
import json

def get_peri(polygon):# 定义函数计算截面周长
	peri=math.sqrt((polygon[-1][0]-polygon[0][0])**2+(polygon[-1][1]-polygon[-1][1])**2)
	for i in range(len(polygon)-1):
		x1=polygon[i][0]
		x2=polygon[i+1][0]
		y1=polygon[i][1]
		y2=polygon[i+1][1]
		peri+=math.sqrt((x1-x2)**2+(y1-y2)**2)
	return peri

def get_property(a, b):# 定义函数计算截面特性
	# 输入参数为划分的三角形点坐标矩阵a、三角形点线顺序矩阵b
	# 输出参数为面积、对xc轴惯性矩、对yc轴惯性矩、形心yc、形心xc、形心轴yc单侧面积矩、形心轴xc单侧面积矩
	inertia_x_sum = 0# 总惯性矩
	inertia_y_sum = 0# 总惯性矩
	area_sum = 0# 总面积
	centroid_y= 0# 总形心
	centroid_x= 0# 总形心
	Sy_sum= 0# 面积矩
	Sx_sum= 0# 面积矩
	SQy= 0# 形心面积矩
	SQx= 0# 形心面积矩
	for i in range(len(b)):# 计算总面积、总惯性矩、总形心
		idx1, idx2, idx3 = b[i]
		point1, point2, point3 = a[idx1], a[idx2], a[idx3]
		x1, y1 = point1
		x2, y2 = point2
		x3, y3 = point3
		area = 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))# 计算面积
		inertia_x = (area * (y1**2 + y2**2 + y3**2 + y1*y2 + y2*y3 + y1*y3)) / 6# 计算惯性矩
		inertia_y = (area * (x1**2 + x2**2 + x3**2 + x1*x2 + x2*x3 + x1*x3)) / 6# 计算惯性矩
		x_mean =(x1 + x2 + x3) / 3 # 计算小形心
		y_mean =(y1 + y2 + y3) / 3 # 计算小形心
		Sy=y_mean*area# 计算面积矩
		Sx=x_mean*area# 计算面积矩
		Sy_sum+= Sy# 面积矩求和
		Sx_sum+= Sx# 面积矩求和
		area_sum += area# 面积求和
		inertia_x_sum += inertia_x# 惯性矩求和
		inertia_y_sum += inertia_y# 惯性矩求和
	centroid_y=Sy_sum/area_sum# 计算总形心
	centroid_x=Sx_sum/area_sum# 计算总形心
	inertia_x_sum-= centroid_y**2 * area_sum# 计算形心轴惯性矩
	inertia_y_sum-= centroid_x**2 * area_sum# 计算形心轴惯性矩
	for i in range(len(b)):# 计算形心面积矩
		idx1, idx2, idx3 = b[i]
		point1, point2, point3 = a[idx1], a[idx2], a[idx3]
		x1, y1 = point1
		x2, y2 = point2
		x3, y3 = point3
		area = 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
		y_mean =(y1 + y2 + y3) / 3
		x_mean =(x1 + x2 + x3) / 3
		if y_mean > centroid_y:# 计算形心轴单侧面积矩作为形心面积矩
			SQy+=(y_mean-centroid_y)* area
		if x_mean > centroid_x:# 计算形心轴单侧面积矩作为形心面积矩
			SQx+=(x_mean-centroid_x)* area
	return area_sum, inertia_x_sum, inertia_y_sum, centroid_y, centroid_x, SQy, SQx

def get_segment(vector):# 定义函数进行点线分段编号
	vector_num = len(vector)# 划分段
	vector_matrix = np.zeros((sum(vector), 2), dtype=int)# 初始全长二维矩阵
	for i in range(vector_num):# 逐段计算
		a=sum(vector[:i])# 段起始编号
		b=sum(vector[:i+1])# 段结束编号
		for j in range(a,b):# 段内编号
			vector_matrix[j] = [j, (j + 1)]
		vector_matrix[j]=[j,a]# 闭合段结束编号
	return vector_matrix
	
def get_polygon(bw, web_n, tw, h):# 定义函数生成截面
	# 既定：顶板倒角1*0.2、底板倒角0.6*0.2
	# 输入参数为截面宽度、腹板数量、腹板厚度、梁高
	# 输出参数为截面拐点坐标矩阵、箱内空心点坐标矩阵、闭合框线数量列表
	h_store=[2, 2.3, 2.5]# 参照梁高
	cantilever_store=[5, 5.415, 5.695]# 参照悬臂长度
	box_edge1_store=[5.2, 5.415, 5.695]# 参照边箱内侧线位置
	box_bottom_store=[-1.6, -1.7, -1.9]# 参照边箱底缘位置
	box_edge2_store=[4.872, 5.01, 5.289]# 参照边箱底侧线位置
	pos=h_store.index(h)
	can=cantilever_store[pos]
	ed1=box_edge1_store[pos]
	bot=box_bottom_store[pos]
	ed2=box_edge2_store[pos]
	tt=0.28
	tb=0.22
	line_out = [[0, 0], [0, -0.185], [1.36, -0.356], [2.926, -0.755], [4.345, -1.529], [can, -h], [bw-can, -h], [bw-4.345, -1.529], [bw-2.926, -0.755], [bw-1.36, -0.356], [bw, -0.185], [bw, 0]]# 外边框坐标（12节点）
	line_in_box = [[3.5, -tt], [3.4, -tt-0.1], [3.4, -0.541], [ed2, bot], [ed1, bot], [ed1, -tt-0.2], [ed1-1, -tt]]# 内边框坐标，初始为第一个小箱坐标（7节点）
	line_in_box.reverse()# 顺时针排序
	peri_i=get_peri(line_in_box)
	line_in_last = [[bw-3.5, -tt], [bw-3.4, -tt-0.1], [bw-3.4, -0.541], [bw-ed2, bot], [bw-ed1, bot], [bw-ed1, -tt-0.2], [bw-ed1+1, -tt]]# 最后一个小箱坐标（7节点）
	peri_i+=get_peri(line_in_last)
	box_in = [[3.5, -tt-0.1]]# 内边框空心点坐标，初始为第一个小箱空心点
	box_in_last=[[bw-3.5, -tt-0.1]]# 最后一个小箱空心点
	line_num=[8 for i in range(web_n+2)]# 各边框线数量列表
	line_num[0]=12
	line_num[1]=7
	line_num[-1]=7
	for i in range(web_n-1):
		web_d= (bw-ed1*2-0.25*2)/(web_n-1) #计算腹板线间距
		web_x1=ed1+0.25+web_d*i+tw/2# 计算内边框左边线
		web_x2=ed1+0.25+web_d*(i+1)-tw/2# 计算内边框右边线
		box=[[web_x1+1, -tt], [web_x1, -tt-0.2], [web_x1, -h+tb+0.2] ,[web_x1+0.6, -h+tb] , [web_x2-0.6, -h+tb], [web_x2, -h+tb+0.2], [web_x2, -tt-0.2], [web_x2-1, -tt]]# 计算并汇总内边框坐标（每大箱8节点）
		box.reverse()# 顺时针排序
		peri_i+=get_peri(box)
		line_in_box+=box
		box_in+=[[web_x1+1, -tt-0.2]]# 计算并汇总内边框空心点坐标
	line_sum=line_out+line_in_box+line_in_last# 边框点坐标汇总
	box_in_sum=box_in+box_in_last# 内箱空心点汇总
	peri_o=get_peri(line_out)
	return line_sum, box_in_sum, line_num, h, can, ed1, tt, tb, peri_o, peri_i

def get_sec_pro(bridge_width, web_quantity, web_thickness, A, Ixx, Iyy, cent_y, cent_x, Qy, Qx, h, can, ed1, tt, tb, peri_out, peri_in):# 定义函数规范化截面特性输出格式
	Qyb=Qy/(web_quantity*web_thickness)# 计算沿yc剪切系数
	Qxb=Qx/(tt+tb)# 计算沿xc剪切系数
	Izz=(bridge_width-(ed1+0.25)*2)*(h-tt/2-tb/2)# 计算扭转惯性矩
	Asx=(bridge_width-can*2)*tb+bridge_width*tt# 计算沿xc有效剪切面积
	Asy=web_quantity*web_thickness*2# 计算沿yc有效剪切面积
	stress_point_location=[[-cent_x, -cent_y], [cent_x, -cent_y], [cent_x-can, -cent_y-h], [-cent_x+can, -cent_y-h]]# 计算形心外框4个应力点坐标
	yc_distance=cent_y+h # 计算截面最下端到形心的距离
	xc_distance=cent_x#  计算截面最左侧到形心的距离
	cxp=xc_distance
	cxm=xc_distance
	cyp=h-yc_distance
	cym=yc_distance
	T1=tt# 设计用顶板厚
	T2=tb# 设计用底板厚
	HT=h-T1/2-T2/2
	BT=bridge_width-(ed1+0.25)*2
	Z1=T2+0.2# 剪切验算位置Z1
	Z3=h-T1-0.2# 剪切验算位置Z3
	tw=tt/2+tb/2# 验算扭转用厚度
	# 调整截面特性输出格式，对应.mct文件的参数顺序
	# 本程序定义截面的坐标轴（x0,y0,z0）与mct文件坐标轴(X,Y,Z)，对应转换关系为x0轴>Y轴，y0轴>Z轴，z0轴>X轴
	sec_pro_st=[[],[],[],[],[]]
	sec_pro_st[0]=[A, Asx, Asy, Izz, Ixx, Iyy]
	sec_pro_st[1]=[cxp, cxm, cyp, cym, Qyb, Qxb, peri_out, peri_in, xc_distance, yc_distance]
	sec_pro_st[2]=[stress_point_location[0][0], stress_point_location[1][0], stress_point_location[2][0], stress_point_location[3][0], stress_point_location[0][1], stress_point_location[1][1], stress_point_location[2][1], stress_point_location[3][1]]
	sec_pro_st[3]=[HT, BT, T1, T2]
	sec_pro_st[4]=[Z1, Z3, tw]
	return sec_pro_st

def get_sec_poly(polygon, web_quantity, cent_x, cent_y):# 定义函数标准化截面坐标输出格式
	for i in range(len(polygon)):# 以形心为原点，对截面坐标进行转换
		polygon[i]=[polygon[i][0]-cent_x,polygon[i][1]-cent_y]
	polygon_array=sum(polygon,[])# 二维转一维
	polygon_ser=[0]*(web_quantity-1+3+1)# 初始框线控制序号
	polygon_ser[1]=12# 修改赋值：第一行外轮廓12节点
	polygon_ser[2]=polygon_ser[1]+7# 第二行左侧小箱7节点
	for i in range(web_quantity-1):
		polygon_ser[i+3]=polygon_ser[i+2]+8# 中间箱8节点
	polygon_ser[-1]=polygon_ser[-2]+7# 最后一行右侧小箱7节点
	sec_poly_st=[[]]*(web_quantity-1+3)# 初始线框坐标列表，每行一个线框
	for i in range(web_quantity-1+3):
		sec_poly_st[i]=polygon_array[polygon_ser[i]*2:polygon_ser[i+1]*2]# 逐行赋值线框坐标
	return sec_poly_st

def section_build(bridge_width, web_quantity, web_thickness, beam_height):# 定义函数，调用上述基本函数建立截面并整理输出sec_pro,sec_poly
	polygon, hole_point, poly_num, h, can, ed1, tt, tb, p_o, p_i=get_polygon(bridge_width, web_quantity, web_thickness, beam_height)# 生成截面数据
	seg=get_segment(poly_num)# 生成截面边框点线顺序
	tr_input= dict(vertices=polygon,segments=seg,holes=hole_point)# 整理triangle入参
	tr_output= tr.triangulate(tr_input,'a0.04q30lpen',)# 执行triangle划分
	A, Ixx, Iyy, cent_y, cent_x, Qy, Qx= get_property(tr_output['vertices'], tr_output['triangles'])# 根据triangle出参计算截面特性
	sec_pro=get_sec_pro(bridge_width, web_quantity, web_thickness, A, Ixx, Iyy, cent_y, cent_x, Qy, Qx, h, can, ed1, tt, tb, p_o, p_i)# 整理输出截面特性
	sec_poly=get_sec_poly(polygon, web_quantity, cent_x, cent_y)# 整理输出截面点坐标
	return sec_pro, sec_poly

# ~ # 输出截面特性
# ~ filename='sec_pro.json'
# ~ with open(filename, 'w') as f_obj:
	# ~ json.dump(sec_pro, f_obj)
# ~ # 输出截面坐标
# ~ filename='sec_poly.json'
# ~ with open(filename, 'w') as f_obj:
	# ~ json.dump(sec_poly, f_obj)

# ~ # 截面三角划分绘图
# ~ tr.compare(plt, tr_input, tr_output)
# ~ plt.show()
