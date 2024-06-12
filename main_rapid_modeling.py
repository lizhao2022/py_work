import section_build as sec
import node_partition as node
import steel_strand_build as steel
import mct_file_edit as mct

file_name='template.mct'# 读取模板文件
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
stirrups_diameter=14# 抗剪箍筋直径
# 前置数据结束

# 样板信息开始
node_pos=28# data_template模板文件节点坐标首行位置
sec_pos=425# data_template模板文件截面特性首行位置
sec_pos_dgn=578# data_template模板文件GN截面特性首行位置
sec_pos_rebar=617# data_template模板文件截面钢筋首行位置
steel_strand_pos=682# data_template模板文件钢绞线束形布置首行位置
stld_phase2_pave=748# data_template模板文件静力荷载工况：二期（铺装）梁单元荷载首行位置
stld_phase2_bumperwall=840# data_template模板文件静力荷载工况：二期（防撞墙等）梁单元荷载首行位置
stld_crossbeam=952# data_template模板文件静力荷载工况：横梁荷载梁单元荷载首行位置
stld_temp0=993# data_template模板文件静力荷载工况：温度梯度（升温）首行位置993
stld_temp1=1008# data_template模板文件静力荷载工况：温度梯度（降温）首行位置1008
# 样板信息结束

# 修改节点
node_x, node_z=node.node_partition(span, crossbeam, pedestal_position, end_seams, web_thickened_length, web_thickening_length, plate_thickening_length)
data_template=mct.data_template_edit_node(node_x, node_z, node_pos, data_template)
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
# 修改二期铺装
# 修改二期防撞墙等
# 修改横梁荷载
# 修改温度梯度升温荷载
# 修改温度梯度降温荷载

project_name=bridge_name+'.mct'# 生成模型文件，即midas软件的.mct文件
with open(project_name, 'w') as file_object:
	file_object.writelines(data_template)
