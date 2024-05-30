# 程序用于计算单箱多室截面特性
# 既定：梁高2、双侧鱼腹式悬臂5、悬臂小箱、顶板厚0.28、底板厚0.22、顶板倒角1*0.2、底板倒角0.6*0.2
# 输入值：桥面宽度、腹板数量、腹板厚度
# 输出值：面积、对xc轴惯性矩、对yc轴惯性矩、形心yc、形心xc
# 输出值：形心扭转惯性矩、沿x有效剪切面积、沿y有效剪切面积、沿xc剪切系数、沿yc剪切系数
# 输出值：形心外框4个应力点坐标、对形心轴外框4个点距离、截面外轮廓周长、截面内轮廓周长
import triangle as tr
import numpy as np
import matplotlib.pyplot as plt
import math
def get_section_property(a, b):# 定义函数计算截面特性
	# 输入参数为划分的三角形点坐标矩阵、三角形点线顺序矩阵
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
	
def get_polygon(bw,web_n,tw):# 定义函数生成截面
	'''# 截面类型为单箱多室'''
	# 既定：梁高2、双侧鱼腹式悬臂5、悬臂小箱、顶板厚0.28、底板厚0.22、顶板倒角1*0.2、底板倒角0.6*0.2
	# 输入参数为截面宽度、腹板数量、腹板厚度
	# 输出参数为截面拐点坐标矩阵、箱内空心点坐标矩阵、闭合框线数量列表
	line_out = [[0, 0], [0, -0.185], [1.36, -0.356], [2.926, -0.755], [4.345, -1.529], [5, -2], [bw-5, -2], [bw-4.345, -1.529], [bw-2.926, -0.755], [bw-1.36, -0.356], [bw, -0.185], [bw, 0]]# 外边框坐标（12节点）
	line_in_box = [[3.5, -0.28], [3.4, -0.38], [3.4, -0.541], [4.872, -1.6], [5.2, -1.6], [5.2, -0.48], [4.2, -0.28]]# 内边框坐标，初始为第一个小箱坐标（7节点）
	line_in_last = [[bw-3.5, -0.28], [bw-3.4, -0.38], [bw-3.4, -0.541], [bw-4.872, -1.6], [bw-5.2, -1.6], [bw-5.2, -0.48], [bw-4.2, -0.28]]# 最后一个小箱坐标（7节点）
	box_in = [[3.5, -0.38]]# 内边框空心点坐标，初始为第一个小箱空心点
	box_in_last=[[bw-3.5, -0.38]]# 最后一个小箱空心点
	line_num=[8 for i in range(web_n+2)]# 各边框线数量列表
	line_num[0]=12
	line_num[1]=7
	line_num[-1]=7
	for i in range(web_n-1):
		web_d= (bw-10-0.9)/(web_n-1) #计算腹板线间距
		web_x1=5.45+web_d*i+tw/2# 计算内边框左边线
		web_x2=5.45+web_d*(i+1)-tw/2# 计算内边框右边线
		line_in_box+= [[web_x1+1, -0.28], [web_x1, -0.48], [web_x1, -1.58] ,[web_x1+0.6, -1.78] , [web_x2-0.6, -1.78], [web_x2, -1.58], [web_x2, -0.48], [web_x2-1, -0.28]]# 计算并汇总内边框坐标（每大箱8节点）
		box_in+=[[web_x1+1, -0.48]]# 计算并汇总内边框空心点坐标
	line_sum=line_out+line_in_box+line_in_last# 边框点坐标汇总
	box_in_sum=box_in+box_in_last# 内箱空心点汇总
	return line_sum, box_in_sum, line_num

bridge_width= 49.96# 桥面宽度
web_quantity= 10# 腹板数量
web_thickness= 0.8# 腹板厚度

polygon, hole_point, poly_num=get_polygon(bridge_width, web_quantity, web_thickness)# 生成截面数据
seg=get_segment(poly_num)# 生成截面边框点线顺序

tr_input= dict(vertices=polygon,segments=seg,holes=hole_point)# 整理triangle入参
tr_output= tr.triangulate(tr_input,'a0.04q30lpen',)# 执行triangle划分
A, Ixx, Iyy, cent_y, cent_x, Qy, Qx= get_section_property(tr_output['vertices'], tr_output['triangles'])# 整理triangle出参

Qyb=Qy/(web_quantity*web_thickness)# 沿yc剪切系数
Qxb=Qx/(0.28+0.22)# 沿xc剪切系数
Izz=(bridge_width-5.45*2)*1.75# 扭转惯性矩
Asx=(bridge_width-5*2)*0.22+bridge_width*0.28# 沿xc有效剪切面积
Asy=web_quantity*web_thickness*2# 沿yc有效剪切面积
peri_out=10*2+bridge_width*2-5*2# 外轮廓周长
peri_in=1*2+(web_quantity-1)*7.5+(bridge_width-5.45*2-(web_quantity-1)*(web_thickness+2))*2# 内轮廓周长
stress_point_location=[[-cent_x, -cent_y], [cent_x, -cent_y], [cent_x-5, -cent_y-2], [-cent_x+5, -cent_y-2]]# 形心外框4个应力点坐标
yc_distance=cent_y+2 # 截面最下端到形心的距离
xc_distance=cent_x#  截面最左侧到形心的距离
cxp=xc_distance
cxm=xc_distance
cyp=2-yc_distance
cym=yc_distance
T1=0.22# 设计用顶板厚
T2=0.28# 设计用底板厚
HT=2-T1/2-T2/2
BT=bridge_width-5.45*2
Z1=T1+0.2# 剪切验算位置Z1
Z3=2-T2-0.2# 剪切验算位置Z3
tw=0.25# 验算扭转用厚度
# 此处统一按列表输出截面特性参数，列表顺序为mct文件对应的参数顺序
# 本程序定义截面的坐标轴（x0,y0,z0）与mct文件坐标轴(X,Y,Z)，对应转换关系为x0轴>Y轴，y0轴>Z轴，z0轴>X轴
sec_pro=[[],[],[],[],[]]
sec_pro[0]=[A, Asx, Asy, Ixx, Iyy, Izz]
sec_pro[1]=[cxp, cxm, cyp, cym, Qxb, Qyb, peri_out, peri_in, xc_distance, yc_distance]
sec_pro[2]=[stress_point_location[0][0], stress_point_location[1][0], stress_point_location[2][0], stress_point_location[3][0], stress_point_location[0][1], stress_point_location[1][1], stress_point_location[2][1], stress_point_location[3][1]]
sec_pro[3]=[HT, BT, T1, T2]
sec_pro[4]=[Z1, Z3, tw]

# ~ print('A=%.4f, Izz=%.4f, Ixx=%.4f, Iyy=%.4f' %(A,Izz,Ixx,Iyy))
# ~ print('Asx=%.4f, Asy=%.4f, Qxb=%.4f, Qyb=%.4f' %(Asx,Asy,Qxb,Qyb))
# ~ print('peri_out=%.4f, peri_in=%.4f, c_x=%.4f, c_y=%.4f' %(peri_out,peri_in,xc_distance,yc_distance))
# ~ print('cxp=%.4f, cxm=%.4f, cyp=%.4f, cym=%.4f' %(cxp,cxm,cyp,cym))
# ~ print('stp_xy=', stress_point_location)
# ~ tr.compare(plt, tr_input, tr_output)
# ~ plt.show()

