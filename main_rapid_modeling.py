import section_build as sec
import node_partition as node
import steel_strand_build as steel
import static_load_cases as stld
import mct_file_edit as mct

# 读取模板mct文件
file_name='template.mct'
with open(file_name, 'r') as file_template:
	data_template=file_template.readlines()

# 前置数据开始
bridge_name='test'
span=[30, 30, 30]# 跨径组合，3跨为例
crossbeam=[2, 3, 3, 2]# 横梁宽度，3跨4支点为例
pedestal_position=[0.6, 0.6]# 边支座距梁端，2边支点
end_seams=[0.05, 0.05]# 梁端缝宽
web_thickened_length=[7.4, 4.4, 4.4, 4.4, 4.4, 7.4]# 腹板加厚段长度，每跨2处，3跨6处
web_thickening_length=[3.6, 3.6, 3.6, 3.6, 3.6, 3.6]# 腹板变厚段长度，每跨2处，3跨6处
plate_thickening_length=[1.2, 1, 1, 1, 1, 1.2]# 顶底板加腋长度，每跨2处，3跨6处

bridge_width=[49.96, 49.488, 49.248, 48.712, 48.391, 47.2, 46.836, 45.726, 45.363, 44.172, 45.808, 43.056, 42.693, 41.744]# 14个控制截面宽度
web_thickness=[0.8, 0.8, 0.5, 0.5, 0.8, 0.8, 0.5, 0.5, 0.8, 0.8, 0.5, 0.5, 0.8, 0.8]# 14个控制截面腹板厚度
web_quantity=10# 腹板数量
bumperwall_width=[0.525, 0.65, 0.525]# 防撞墙宽度
stirrups_diameter=14# 抗剪箍筋直径
# 前置数据结束

# 样板信息开始
node_pos=28# data_template模板文件节点坐标首行位置
sec_pos=425# data_template模板文件截面特性首行位置
sec_pos_dgn=578# data_template模板文件GN截面特性首行位置
sec_pos_rebar=617# data_template模板文件截面钢筋首行位置
steel_strand_pos=682# data_template模板文件钢绞线束形布置首行位置
stld_pave_pos=747# data_template模板文件静力荷载工况：二期（铺装）梁单元荷载首行位置
stld_bumperwall_pos=839# data_template模板文件静力荷载工况：二期（防撞墙等）梁单元荷载首行位置
stld_crossbeam_pos=951# data_template模板文件静力荷载工况：横梁荷载梁单元荷载首行位置
stld_temup_pos=992# data_template模板文件静力荷载工况：温度梯度（升温）首行位置
stld_temdown_pos=1327# data_template模板文件静力荷载工况：温度梯度（降温）首行位置
lane_pos_1=1679# data_template模板文件静车道线：单车道首行位置
lane_pos_2=1707# data_template模板文件静车道线：车道1（带系数）首行位置
# 样板信息结束

# 修改节点
node_x, node_z=node.node_partition(span, crossbeam, pedestal_position, end_seams, web_thickened_length, web_thickening_length, plate_thickening_length)
node_str=mct.node_str_build(node_x, node_z)
data_template[node_pos:node_pos+len(node_str)]=node_str# 修改节点坐标，行号不变
# 修改箍筋
rebar_str=mct.sec_rebar_str_build(web_quantity, stirrups_diameter)
data_template=mct.data_template_edit_rebar(rebar_str, sec_pos_rebar, data_template)
# 修改截面
sec_pro_total=[[]]*14
sec_poly_total=[[]]*14
for i in range(14):
	sec_pro_total[i], sec_poly_total[i]=sec.section_build(bridge_width[i], web_quantity, web_thickness[i])
data_template, row_add=mct.data_template_edit_section(sec_pro_total, sec_poly_total, sec_pos, sec_pos_dgn, data_template)
# 修改钢束
steel_x, steel_y, steel_r, steel_count=steel.steel_strand_build(span, end_seams, web_quantity)
steel_str=[[]]*len(steel_x)
for i in range(len(steel_x)):
	steel_str[i]=mct.steel_strand_str(steel_x[i], steel_y[i], steel_r[i], steel_count[i])
data_template, row_add=mct.data_template_edit_steel(steel_str, steel_strand_pos, row_add, data_template)
# 修改二期铺装及防撞墙
pave_load, bumperwall_load=stld.pave_bumperwall_load(bumperwall_width, bridge_width, node_x)
pave_str=mct.stld_str(pave_load)
bumperwall_str=mct.stld_str(bumperwall_load)
data_template[(stld_pave_pos+row_add):(stld_pave_pos+row_add+len(pave_str))]=pave_str# 修改二期铺装荷载，行号不变
data_template[(stld_bumperwall_pos+row_add):(stld_bumperwall_pos+row_add+len(bumperwall_str))]=bumperwall_str# 修改二期防撞墙荷载，行号不变
# 修改横梁荷载
crossbeam_load, plate_load=stld.crossbeam_plate_load(web_quantity, bridge_width)
crossbeam_str=mct.stld_crossbeam_str(crossbeam_load, plate_load)
data_template[(stld_crossbeam_pos+row_add):(stld_crossbeam_pos+row_add+len(crossbeam_str))]=crossbeam_str# 修改二期铺装荷载，行号不变
# 修改温度梯度荷载
tem_width_1, tem_width_2, tem_h, tem_up, tem_down=stld.tem_load(web_quantity, bridge_width, node_x)
stld_temup_str=mct.stld_tem_str(tem_width_1, tem_width_2, tem_h, tem_up)
stld_temdown_str=mct.stld_tem_str(tem_width_1, tem_width_2, tem_h, tem_down)
data_template[(stld_temup_pos+row_add):(stld_temup_pos+row_add+len(stld_temup_str))]=stld_temup_str# 修改温度梯度升温荷载，行号不变
data_template[(stld_temdown_pos+row_add):(stld_temdown_pos+row_add+len(stld_temdown_str))]=stld_temdown_str# 修改温度梯度升温荷载，行号不变

# 生成模型文件，即midas软件的.mct文件
project_name=bridge_name+'.mct'
with open(project_name, 'w') as file_object:
	file_object.writelines(data_template)
