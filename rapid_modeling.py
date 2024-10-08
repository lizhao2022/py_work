import section_build as sec
import node_partition as node
import steel_strand_build as steel
import static_load_cases as stld
import mct_file_edit as mct

def modeling(tem_dic):
	# 读取模板mct文件
	file_name='template.mct'
	with open(file_name, 'r') as file_template:
		data_template=file_template.readlines()
	"""
	前置数据开始
	"""
	# ~ bridge_name='test'
	span=tem_dic["span"]# 跨径组合，3跨为例
	beam_height=tem_dic["beam_height"]# 梁高
	crossbeam=tem_dic["crossbeam"]# 横梁宽度，3跨4支点为例
	pedestal_position=tem_dic["pedestal_position"]# 边支座距梁端，2边支点
	end_seams=tem_dic["end_seams"]# 梁端缝宽,2端
	web_thickened_length=tem_dic["web_thickened_length"]# 腹板加厚段长度，每跨2处，3跨6处
	web_thickening_length=tem_dic["web_thickening_length"]# 腹板变厚段长度，每跨2处，3跨6处
	plate_thickening_length=tem_dic["plate_thickening_length"]# 顶底板加腋长度，每跨2处，3跨6处
	bridge_width=tem_dic["bridge_width"]# 14个控制截面宽度
	web_quantity=tem_dic["web_quantity"]# 腹板数量
	bumperwall_width=tem_dic["bumperwall_width"]# 防撞墙宽度
	"""
	前置数据输入结束
	"""
	
	web_thickness=[0.8, 0.8, 0.5, 0.5, 0.8, 0.8, 0.5, 0.5, 0.8, 0.8, 0.5, 0.5, 0.8, 0.8]# 14个控制截面腹板厚度
	stirrups_diameter=14# 抗剪箍筋直径
	# 前置数据结束
	
	# 样板信息开始
	node_pos=28# data_template模板文件节点坐标首行位置
	sec_pos=425# data_template模板文件截面特性首行位置
	sec_pos_dgn=578# data_template模板文件DGN截面特性首行位置
	sec_pos_rebar=617# data_template模板文件截面钢筋首行位置
	steel_strand_pos=681# data_template模板文件钢绞线束形布置首行位置
	stld_pave_pos=734# data_template模板文件静力荷载工况：二期（铺装）梁单元荷载首行位置
	stld_bumperwall_pos=826# data_template模板文件静力荷载工况：二期（防撞墙等）梁单元荷载首行位置
	stld_prestress_pos=914# data_template模板文件静力荷载工况：预应力荷载首行位置
	stld_crossbeam_pos=925# data_template模板文件静力荷载工况：横梁荷载梁单元荷载首行位置
	stld_temup_pos=966# data_template模板文件静力荷载工况：温度梯度（升温）首行位置
	stld_temdown_pos=1301# data_template模板文件静力荷载工况：温度梯度（降温）首行位置
	lane_pos_1=1653# data_template模板文件车道线：单车道首行位置
	lane_pos_2=1681# data_template模板文件车道线：车道1（带系数）首行位置
	mld_pos=1862# data_template模板文件移动荷载工况首行位置
	sm_group_pos=1866# data_template模板文件沉降组首行位置
	span_pos=2055# data_template模板文件结构跨度首行位置
	# 样板信息结束
	
	# 修改节点
	node_x, node_z=node.node_partition(span, crossbeam, pedestal_position, end_seams, web_thickened_length, web_thickening_length, plate_thickening_length, beam_height)
	node_str=mct.node_str_build(node_x, node_z)
	data_template[node_pos:node_pos+len(node_str)]=node_str# 修改节点坐标，行号不变
	# 修改箍筋
	rebar_str=mct.sec_rebar_str_build(web_quantity, stirrups_diameter)
	data_template=mct.data_template_edit_rebar(rebar_str, sec_pos_rebar, data_template)# 修改箍筋，行号不变
	# 修改截面
	sec_pro_total=[[]]*14
	sec_poly_total=[[]]*14
	for i in range(14):
		sec_pro_total[i], sec_poly_total[i]=sec.section_build(bridge_width[i], web_quantity, web_thickness[i], beam_height)
	data_template, row_add=mct.data_template_edit_section(sec_pro_total, sec_poly_total, sec_pos, sec_pos_dgn, data_template)# 修改截面，行号增加
	# 修改钢束
	steel_x, steel_y, steel_r, steel_count, steel_det=steel.steel_strand_build(span, end_seams, web_quantity, beam_height, node_x)
	steel_str=[[]]*len(steel_x)
	steel_strand_pos+=row_add
	for i in range(len(steel_x)):
		steel_str[i]=mct.steel_strand_str(steel_x[i], steel_y[i], steel_r[i], steel_count[i], steel_det[i])
		data_template=mct.ins_list(steel_strand_pos, steel_str[i], data_template)# 修改钢束，行号增加
		steel_strand_pos+=len(steel_str[i])
		row_add+=len(steel_str[i])
	# 修改二期铺装及防撞墙
	pave_load, bumperwall_load=stld.pave_bumperwall_load(bumperwall_width, bridge_width, node_x)
	pave_str=mct.stld_str(pave_load)
	bumperwall_str=mct.stld_str(bumperwall_load)
	data_template[(stld_pave_pos+row_add):(stld_pave_pos+row_add+len(pave_str))]=pave_str# 修改二期铺装荷载，行号不变
	data_template[(stld_bumperwall_pos+row_add):(stld_bumperwall_pos+row_add+len(bumperwall_str))]=bumperwall_str# 修改二期防撞墙荷载，行号不变
	
	# 修改预应力荷载
	prestress_str=mct.stld_prestress(steel_det)
	data_template=mct.ins_list(stld_prestress_pos+row_add, prestress_str, data_template)# 修改预应力荷载，行号增加
	row_add+=len(prestress_str)
	
	# 修改横梁荷载
	crossbeam_load, plate_load=stld.crossbeam_plate_load(web_quantity, bridge_width, beam_height)
	crossbeam_str=mct.stld_crossbeam_str(crossbeam_load, plate_load)
	data_template[(stld_crossbeam_pos+row_add):(stld_crossbeam_pos+row_add+len(crossbeam_str))]=crossbeam_str# 修改二期铺装荷载，行号不变
	# 修改温度梯度荷载
	tem_width_1, tem_width_2, tem_h, tem_up, tem_down=stld.tem_load(web_quantity, bridge_width, node_x)
	stld_temup_str=mct.stld_tem_str(tem_width_1, tem_width_2, tem_h, tem_up)
	stld_temdown_str=mct.stld_tem_str(tem_width_1, tem_width_2, tem_h, tem_down)
	data_template[(stld_temup_pos+row_add):(stld_temup_pos+row_add+len(stld_temup_str))]=stld_temup_str# 修改温度梯度升温荷载，行号不变
	data_template[(stld_temdown_pos+row_add):(stld_temdown_pos+row_add+len(stld_temdown_str))]=stld_temdown_str# 修改温度梯度降温荷载，行号不变
	# 修改单车道车道线跨径
	fac_1=[1]*82
	lane_str_1=mct.lane_str_1(span, fac_1)
	data_template[(lane_pos_1+row_add):(lane_pos_1+row_add+len(lane_str_1))]=lane_str_1# 修改单车道车道线信息，行号不变
	# 修改车道1车道线跨径及系数
	fac_2, fac_3=stld.lane_fac(bridge_width, bumperwall_width, node_x)
	lane_str_2=mct.lane_str_2(span, fac_2)
	data_template[(lane_pos_2+row_add):(lane_pos_2+row_add+len(lane_str_2))]=lane_str_2# 修改车道1车道线信息，行号不变
	# 修改移动荷载工况
	mld_str=mct.mld_str(fac_3)
	data_template[(mld_pos+row_add):(mld_pos+row_add+len(mld_str))]=mld_str# 修改移动荷载工况信息，行号不变
	# 修改沉降组
	sm_group_str=mct.sm_group_str(span)
	data_template[(sm_group_pos+row_add):(sm_group_pos+row_add+len(sm_group_str))]=sm_group_str# 修改沉降组信息，行号不变
	# 修改结构跨度
	span_str=mct.span_str(span, pedestal_position, end_seams)
	data_template[(span_pos+row_add):(span_pos+row_add+len(span_str))]=span_str# 修改结构跨度信息，行号不变
	
	return data_template
