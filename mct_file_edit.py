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
	pro_taper[6]='       '+', '.join([str(x) for x in pro_i[3]])+', '+', '.join([str(x) for x in pro_j[3]])+'\n'# 首尾顺序
	pro_taper[7]='       YES, '+str(pro_i[4][0])+', '+str(pro_i[4][1])+', YES, , YES, , YES, , '+str(pro_i[4][2])+', YES, , YES, , YES, , '+str(pro_j[4][0])+', '+str(pro_j[4][1])+', YES, , YES, , YES, , '+str(pro_j[4][2])+', YES, , YES, , YES,\n'# 首尾顺序
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

def steel_strand_str(x, y, r, count, na):
	'''# 建立钢束形状信息字符串'''
	steel_str=[[]]*(4+len(x))
	steel_str[0]='   NAME='+na[0]+', '+na[1]+', '+na[2]+', 0, 0, ROUND, 3D\n'
	steel_str[1]='        , AUTO1, , , YES, '+str(count)+', 0, 0\n'
	steel_str[2]='        STRAIGHT, 0, 0, 0, X, 0, 0\n'
	steel_str[3]='        0, YES, Y, 0\n'
	for i in range(len(x)):
		steel_str[i+4]='        '+str(x[i])+', 0, '+str(y[i])+', NO, 0, 0, '+str(r[i])+'\n'
	return steel_str

def stld_str(st_load):
	'''# 建立二期荷载信息字符串'''
	st_str=[[]]*(len(st_load)-1)
	for i in range(len(st_str)):
		st_str[i]='    '+str(i+1)+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(st_load[i])+', 1, '+str(st_load[i+1])+', 0, 0, 0, 0, 二期, NO, 0, 0, NO,\n' 
	return st_str

def stld_prestress(prest):
	'''# 建立预应力荷载信息字符串'''
	pre_str=[[]]*len(prest)
	for i in range(len(prest)):
		pre_str[i]=' '+prest[i][0]+', STRESS, '+prest[i][3]+', '+prest[i][4]+', '+prest[i][5]+', 1, 预应力\n'
	return pre_str

def stld_crossbeam_str(crossbeam_load, plate_load):
	'''# 建立横梁荷载信息字符串'''
	a=crossbeam_load
	b=plate_load
	ele=[1, 2, 3, 26, 27, 28, 29, 53, 54, 55, 56, 79, 80, 81]
	crossbeam_str=[[]]*(len(ele))
	crossbeam_str[0]='    '+str(ele[0])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[0])+', 1, '+str(a[0])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[1]='    '+str(ele[1])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[0])+', 1, '+str(a[0])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[2]='    '+str(ele[2])+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(b[0])+', 1, 0, 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[3]='    '+str(ele[3])+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, 0, 1, '+str(b[1])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[4]='    '+str(ele[4])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[1])+', 1, '+str(a[1])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[5]='    '+str(ele[5])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[1])+', 1, '+str(a[1])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[6]='    '+str(ele[6])+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(b[1])+', 1, 0, 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[7]='    '+str(ele[7])+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, 0, 1, '+str(b[2])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[8]='    '+str(ele[8])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[2])+', 1, '+str(a[2])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[9]='    '+str(ele[9])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[2])+', 1, '+str(a[2])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[10]='    '+str(ele[10])+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(b[2])+', 1, 0, 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[11]='    '+str(ele[11])+', LINE   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, 0, 1, '+str(b[3])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[12]='    '+str(ele[12])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[3])+', 1, '+str(a[3])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	crossbeam_str[13]='    '+str(ele[13])+', BEAM   , UNILOAD, GZ, NO , NO, aDir[1], , , , 0, '+str(a[3])+', 1, '+str(a[3])+', 0, 0, 0, 0, 恒载组, NO, 0, 0, NO,\n'
	return crossbeam_str

def stld_tem_str(tem_width_1, tem_width_2, tem_h, tem):
	'''# 建立温度梯度荷载信息字符串'''
	w1=tem_width_1
	w2=tem_width_2
	h=tem_h
	t=tem
	tem_str=[[]]*4*81
	for i in range(len(w1)-1):
		tem_str[i*4]='  '+str(i+1)+', LZ, Top, 3, , NO\n'
		tem_str[i*4+1]='    ELEMENT,  0, 0,  '+str(w1[i])+',  '+str(h[0])+', '+str(t[0])+',  '+str(h[1])+', '+str(t[1])+'\n'
		tem_str[i*4+2]='    ELEMENT,  0, 0,  '+str(w1[i])+',  '+str(h[1])+', '+str(t[1])+',  '+str(h[2])+', '+str(t[2])+'\n'
		tem_str[i*4+3]='    ELEMENT,  0, 0,  '+str(w2[i])+',  '+str(h[2])+', '+str(t[2])+',  '+str(h[3])+', '+str(t[3])+'\n'
	return tem_str

def lane_str_1(span, fac):
	'''# 建立车道线信息字符串'''
	a=str(max(span))
	b=fac
	lane_str=[[]]*27
	for i in range(27):
		lane_str[i]='           '+str(3*i+1)+', 0, '+a+', NO, '+str(b[3*i])+',    '+str(3*i+2)+', 0, '+a+', NO, '+str(b[3*i+1])+',    '+str(3*i+3)+', 0, '+a+', NO, '+str(b[3*i+2])+'\n'
	lane_str[0]='           1, 0, '+a+', YES, '+str(b[0])+',    2, 0, '+a+', NO, '+str(b[1])+',    3, 0, '+a+', NO, '+str(b[2])+'\n'
	return lane_str

def lane_str_2(span, fac):
	'''# 建立车道线信息字符串'''
	a=str(max(span))
	b=fac
	lane_str=[[]]*40
	for i in range(1,40):
		lane_str[i]='           '+str(2*i+2)+', 0, '+a+', NO, '+str(b[2*i+1])+',    '+str(2*i+3)+', 0, '+a+', NO, '+str(b[2*i+2])+'\n'
	lane_str[0]='           1, 0, '+a+', YES, '+str(b[0])+',    2, 0, '+a+', NO, '+str(b[1])+',    3, 0, '+a+', NO, '+str(b[2])+'\n'
	return lane_str

def mld_str(fac):
	'''# 建立移动荷载工况信息字符串'''
	mld_str=['        VL, CH-CD, '+str(fac)+', 0, 1, 车道1\n']
	return mld_str

def sm_group_str(span):
	'''# 建立沉降组信息字符串'''
	sm_str=[[]]*4
	sm_str[0]='   1, '+str(-span[0]/5000)+', 83\n'
	sm_str[1]='   2, '+str(-max(span[0:2])/5000)+', 84\n'
	sm_str[2]='   3, '+str(-max(span[1:3])/5000)+', 85\n'
	sm_str[3]='   4, '+str(-span[2]/5000)+', 86\n'
	return sm_str

def span_str(span, ped, seam):
	'''# 建立结构跨度信息字符串'''
	span_str=['        YES, '+str(ped[0])+', '+str(span[0]-ped[0]-seam[0])+', '+str(span[1])+', '+str(span[1]-ped[1]-seam[1])+', '+str(ped[1])+'\n']
	return span_str

def sec_manager_rebar_str(web_quantity, stirrups_dia):
	'''# 建立SECTION-MANAGER-REBAR字符串'''
	stirrups_area=web_quantity*stirrups_dia*stirrups_dia/4*3.1415926/1000/1000*2# 双肢面积
	manager_rebar_str=[[]]*13*4
	for i in range(13):
		manager_rebar_str[4*i]='   SECT='+str(i+19)+', YES, YES, NO, 1, NO, 0, 0\n'
		manager_rebar_str[4*i+1]=' 0, 0\n'
		manager_rebar_str[4*i+2]=' NO, 0, 0, 0, NO, 0, 90, 0, 0, 0.6, NO, 0, 0, 0, YES, 0.1, '+str(stirrups_area*2)+', NO, 0, NO, 0, 0, 0, 0, 0\n'
		manager_rebar_str[4*i+3]=' NO, 0, 0, 0, NO, 0, 90, 0, 0, 0.6, NO, 0, 0, 0, YES, 0.1, '+str(stirrups_area*2)+', NO, 0, NO, 0, 0, 0, 0, 0\n'
	for i in [2, 6, 10]:
		manager_rebar_str[4*i]='   SECT='+str(i+19)+', YES, YES, NO, 1, NO, 0, 0\n'
		manager_rebar_str[4*i+1]=' 0, 0\n'
		manager_rebar_str[4*i+2]=' NO, 0, 0, 0, NO, 0, 90, 0, 0, 0.6, NO, 0, 0, 0, YES, 0.1, '+str(stirrups_area)+', NO, 0, NO, 0, 0, 0, 0, 0\n'
		manager_rebar_str[4*i+3]=' NO, 0, 0, 0, NO, 0, 90, 0, 0, 0.6, NO, 0, 0, 0, YES, 0.1, '+str(stirrups_area)+', NO, 0, NO, 0, 0, 0, 0, 0\n'
	return manager_rebar_str

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

# ~ def data_template_edit_steel(steel_str, steel_pos, row_add, data):
	# ~ str_pos=steel_pos+row_add
	# ~ for i in range(len(steel_str)):
		# ~ data=ins_list(str_pos, steel_str[i], data)
		# ~ str_pos+=len(steel_str[i])
		# ~ row_add+=len(steel_str[i])
	# ~ return data, row_add

# ~ '''# 生成.mct模型文件'''
# ~ project_name='test.mct'# 生成模型文件，即midas软件的.mct文件
# ~ with open(project_name, 'w') as file_object:
	# ~ file_object.writelines(data_template)
