# ~ sec_pro=[[],[],[],[],[]]# 初始的sec_pro列表格式
# ~ sec_pro[0]=[A, Asx, Asy, Ixx, Iyy, Izz]
# ~ sec_pro[1]=[cxp, cxm, cyp, cym, Qxb, Qyb, peri_out, peri_in, xc_distance, yc_distance]
# ~ sec_pro[2]=[stress_point_location[0][0], stress_point_location[1][0], stress_point_location[2][0], stress_point_location[3][0], stress_point_location[0][1], stress_point_location[1][1], stress_point_location[2][1], stress_point_location[3][1]]
# ~ sec_pro[3]=[HT, BT, T1, T2]
# ~ sec_pro[4]=[ZZ1, ZZ3, tw]

def ins_list(pos, lis_source,lis_base):
	''' # 定义列表插入函数'''
	# 定义函数在列表lis_base的指定位置pos开始逐项插入列表lis_source的项
	for i in range(len(lis_source)):
		j=i+pos
		lis_base.insert(j,lis_source[i])# 逐项插入
	return lis_base# 返回修改后的列表

def node_str_build(node_x, node_z):
	'''# 建立节点坐标字符串'''
	node_adjust=list(range(len(node_x)))# 初始节点坐标字符串列表
	for i in range(len(node_x)):# 逐项修改节点坐标字符串
		node_adjust[i]='    '+str(i+1)+', {x}, 0, {z}\n'.format(x=node_x[i], z=node_z[i])
	return node_adjust

def sec_str_build(pro, polygon):
	'''# 建立控制截面特性及轮廓'''
	# 建立截面特性字符串列表
	pro_str=[[]]*5# 初始截面特性列表
	for i in range(4):
		pro_str[i]='       '+', '.join([str(x) for x in pro[i]])+'\n'
	pro_str[4]='       YES, '+str(pro[4][0])+', '+str(pro[4][1])+', YES, , YES, , YES, , '+str(pro[4][2])+', YES, , YES, , YES,\n'
	# 建立截面外轮廓字符串列表
	outpoly_str=[[]]*4
	outpoly_str[0]='       OPOLY='+', '.join([str(x) for x in polygon[0][0:8]])+'\n'
	outpoly_str[1]='             '+', '.join([str(x) for x in polygon[0][8:14]])+'\n'
	outpoly_str[2]='             '+', '.join([str(x) for x in polygon[0][14:20]])+'\n'
	outpoly_str[3]='             '+', '.join([str(x) for x in polygon[0][20:24]])+'\n'
	# 建立截面内轮廓第一个小箱字符串列表
	inpoly_str_first=[[]]*2
	inpoly_str_first[0]='       IPOLY='+', '.join([str(x) for x in polygon[1][0:8]])+'\n'
	inpoly_str_first[1]='             '+', '.join([str(x) for x in polygon[1][8:14]])+'\n'
	# 建立中间箱
	inpoly_str_mid=[[]]*(len(polygon)-3)*3# 初始中间箱，每箱3行
	for i in range(len(polygon)-3):# 逐箱建立
		inpoly_str_mid[i*3]='       IPOLY='+', '.join([str(x) for x in polygon[i+2][0:8]])+'\n'
		inpoly_str_mid[i*3+1]='             '+', '.join([str(x) for x in polygon[i+2][8:14]])+'\n'
		inpoly_str_mid[i*3+2]='             '+', '.join([str(x) for x in polygon[i+2][14:16]])+'\n'
	# 建立最后一个小箱
	inpoly_str_last=[[]]*2
	inpoly_str_last[0]='       IPOLY='+', '.join([str(x) for x in polygon[-1][0:8]])+'\n'
	inpoly_str_last[1]='             '+', '.join([str(x) for x in polygon[-1][8:14]])+'\n'
	# 合并截面轮廓所有项
	poly_str=outpoly_str+inpoly_str_first+inpoly_str_mid+inpoly_str_last
	# 合并截面特性与轮廓
	sec_insert=pro_str+poly_str
	return sec_insert

def sec_taper_str_build(pro_i, poly_i, pro_j, poly_j):
	'''# 建立变截面特性及轮廓'''
	# 建立截面特性字符串列表
	pro_taper=[[]]*8# 初始截面特性列表
	for i in range(3):
		pro_taper[i]='       '+', '.join([str(x) for x in pro_i[i]])+'\n'# 首端
		pro_taper[i+3]='       '+', '.join([str(x) for x in pro_j[i]])+'\n'# 尾端
	pro_taper[6]='       '+', '.join([str(x) for x in pro_i[3]])+', '.join([str(x) for x in pro_j[3]])+'\n'# 首尾顺序
	pro_taper[7]='       YES, '+str(pro_i[4][0])+', '+str(pro_i[4][1])+', YES, , YES, , YES, , '+str(pro_i[4][2])+', YES, , YES, , YES, YES, '+str(pro_j[4][0])+', '+str(pro_j[4][1])+', YES, , YES, , YES, , '+str(pro_j[4][2])+', YES, , YES, , YES,\n'# 首尾顺序
	# 建立首端截面外轮廓字符串列表
	outpoly_i=[[]]*4
	outpoly_i[0]='       OPOLY=YES, '+', '.join([str(x) for x in poly_i[0][0:8]])+'\n'
	outpoly_i[1]='                  '+', '.join([str(x) for x in poly_i[0][8:14]])+'\n'
	outpoly_i[2]='                  '+', '.join([str(x) for x in poly_i[0][14:20]])+'\n'
	outpoly_i[3]='                  '+', '.join([str(x) for x in poly_i[0][20:24]])+'\n'
	# 建立首端第一个小箱
	inpoly_i_first=[[]]*2
	inpoly_i_first[0]='       IPOLY=YES, '+', '.join([str(x) for x in poly_i[1][0:8]])+'\n'
	inpoly_i_first[1]='                  '+', '.join([str(x) for x in poly_i[1][8:14]])+'\n'
	# 建立首端中间箱
	inpoly_i_mid=[[]]*(len(poly_i)-3)*3# 初始中间箱，每箱3行
	for i in range(len(poly_i)-3):# 逐箱建立
		inpoly_i_mid[i*3]='       IPOLY=YES, '+', '.join([str(x) for x in poly_i[i+2][0:8]])+'\n'
		inpoly_i_mid[i*3+1]='                  '+', '.join([str(x) for x in poly_i[i+2][8:14]])+'\n'
		inpoly_i_mid[i*3+2]='                  '+', '.join([str(x) for x in poly_i[i+2][14:16]])+'\n'
	# 建立首端最后一个小箱
	inpoly_i_last=[[]]*2
	inpoly_i_last[0]='       IPOLY=YES, '+', '.join([str(x) for x in poly_i[-1][0:8]])+'\n'
	inpoly_i_last[1]='                  '+', '.join([str(x) for x in poly_i[-1][8:14]])+'\n'
	# 合并截面首端轮廓所有项
	poly_str_i=outpoly_i+inpoly_i_first+inpoly_i_mid+inpoly_i_last
	
	# 建立尾端截面外轮廓字符串列表
	outpoly_j=[[]]*4
	outpoly_j[0]='       OPOLY=NO, '+', '.join([str(x) for x in poly_j[0][0:8]])+'\n'
	outpoly_j[1]='                 '+', '.join([str(x) for x in poly_j[0][8:14]])+'\n'
	outpoly_j[2]='                 '+', '.join([str(x) for x in poly_j[0][14:20]])+'\n'
	outpoly_j[3]='                 '+', '.join([str(x) for x in poly_j[0][20:24]])+'\n'
	# 建立尾端第一个小箱
	inpoly_j_first=[[]]*2
	inpoly_j_first[0]='       IPOLY=NO, '+', '.join([str(x) for x in poly_j[1][0:8]])+'\n'
	inpoly_j_first[1]='                 '+', '.join([str(x) for x in poly_j[1][8:14]])+'\n'
	# 建立尾端中间箱
	inpoly_j_mid=[[]]*(len(poly_j)-3)*3# 初始中间箱，每箱3行
	for i in range(len(poly_j)-3):# 逐箱建立
		inpoly_j_mid[i*3]='       IPOLY=NO, '+', '.join([str(x) for x in poly_j[i+2][0:8]])+'\n'
		inpoly_j_mid[i*3+1]='                 '+', '.join([str(x) for x in poly_j[i+2][8:14]])+'\n'
		inpoly_j_mid[i*3+2]='                 '+', '.join([str(x) for x in poly_j[i+2][14:16]])+'\n'
	# 建立尾端最后一个小箱
	inpoly_j_last=[[]]*2
	inpoly_j_last[0]='       IPOLY=NO, '+', '.join([str(x) for x in poly_j[-1][0:8]])+'\n'
	inpoly_j_last[1]='                 '+', '.join([str(x) for x in poly_j[-1][8:14]])+'\n'
	# 合并截面首端轮廓所有项
	poly_str_j=outpoly_j+inpoly_j_first+inpoly_j_mid+inpoly_j_last
	
	# 合并变截面特性与轮廓
	sec_taper_insert=pro_taper+poly_str_i+poly_str_j
	return sec_taper_insert

def sec_rebar_str_build(web_quantity, stirrups_dia):
	'''# 建立截面配筋信息字符串'''
	stirrups_area=web_quantity*stirrups_dia*stirrups_dia/4*3.1415926/1000/1000*2# 双肢面积
	rebar_str=['        NO, , , , NO, , , , , , NO, , , , YES, 0.1, '+str(stirrups_area*2)+', NO, ,\n']*13
	rebar_str[2]='        NO, , , , NO, , , , , , NO, , , , YES, 0.15, '+str(stirrups_area)+', NO, ,\n'
	rebar_str[6]='        NO, , , , NO, , , , , , NO, , , , YES, 0.15, '+str(stirrups_area)+', NO, ,\n'
	rebar_str[10]='        NO, , , , NO, , , , , , NO, , , , YES, 0.15, '+str(stirrups_area)+', NO, ,\n'
	return rebar_str

def steel_strand_str(x, y, r, count):
	'''# 建立钢束形状信息字符串'''
	steel_str=[[]]*(3+len(x))
	steel_str[0]='        , AUTO1, , , YES, '+str(count)+', 0, 0\n'
	steel_str[1]='        STRAIGHT, 0, 0, 0, X, 0, 0\n'
	steel_str[2]='        0, YES, Y, 0\n'
	for i in range(len(x)):
		steel_str[i+3]='        '+str(x[i])+', 0, '+str(y[i])+', NO, 0, 0, '+str(r[i])+'\n'
	return steel_str

def data_template_edit_node(node_x, node_z, node_pos, data_template):
	node_edit=node_str_build(node_x,node_z)# 建立节点坐标字符串列表
	data_template[node_pos:node_pos+len(node_edit)]=node_edit# 修改节点坐标，行号不变
	return data_template

def data_template_edit_section(sec_pro_total, sec_poly_total, sec_pos, sec_pos_dgn, data_template):
	row_add=0
	for i in range(14):# 逐个建立控制截面
		sec_str=sec_str_build(sec_pro_total[i], sec_poly_total[i])# 建立截面信息字符串列表
		data_template=ins_list(sec_pos, sec_str, data_template)# 执行列表插入
		sec_pos+=len(sec_str)+1# 行号增加，并跳过模板template名称行
		sec_pos_dgn+=len(sec_str)# DGN行号增加
		row_add+=len(sec_str)
	for i in range(13):# 逐个建立变截面
		sec_taper_str=sec_taper_str_build(sec_pro_total[i], sec_poly_total[i], sec_pro_total[i+1], sec_poly_total[i+1])
		data_template=ins_list(sec_pos, sec_taper_str, data_template)
		sec_pos+=len(sec_taper_str)+1
		sec_pos_dgn+=len(sec_taper_str)
		row_add+=len(sec_taper_str)
	
	for i in range(14):# 逐个建立控制截面DGN
		sec_str=sec_str_build(sec_pro_total[i], sec_poly_total[i])# 建立截面信息字符串列表
		data_template=ins_list(sec_pos_dgn, sec_str, data_template)# 执行列表插入
		sec_pos_dgn+=len(sec_str)+1# DGN行号增加，并跳过模板template名称行
		row_add+=len(sec_str)
	for i in range(13):# 逐个建立变截面DGN
		sec_taper_str=sec_taper_str_build(sec_pro_total[i], sec_poly_total[i], sec_pro_total[i+1], sec_poly_total[i+1])
		data_template=ins_list(sec_pos_dgn, sec_taper_str, data_template)
		sec_pos_dgn+=len(sec_taper_str)+1
		row_add+=len(sec_taper_str)
		
	return data_template, row_add

def data_template_edit_rebar(rebar_str, pos_rebar, data):
	for i in range(13):
		data[pos_rebar]=rebar_str[i]
		pos_rebar+=2
	return data

def data_template_edit_steel(steel_str, steel_pos, row_add, data):
	str_pos=steel_pos+row_add
	for i in range(len(steel_str)):
		data=ins_list(str_pos, steel_str[i], data)
		str_pos+=len(steel_str[i])+1
		row_add+=len(steel_str[i])
	return data, row_add

# ~ '''# 生成.mct模型文件'''
# ~ project_name='test.mct'# 生成模型文件，即midas软件的.mct文件
# ~ with open(project_name, 'w') as file_object:
	# ~ file_object.writelines(data_template)
