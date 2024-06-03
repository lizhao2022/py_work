import section_build
import node_partition
import mct_file_edit

file_name='template.mct'# 读取模板文件
with open(file_name, 'r') as file_template:
	data_template=file_template.readlines()

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

node_pos=28# data_template模板文件原始节点坐标首行位置
sec_pos=425# data_template原始截面特性首行位置
sec_pos_dgn=578# data_template原始DGN截面特性首行位置

node_x, node_z=node_partition.node_partition(span, crossbeam, pedestal_position, end_seams, web_thickened_length, web_thickening_length, plate_thickening_length)
data_template=mct_file_edit.data_template_edit_node(node_x, node_z, node_pos, data_template)

sec_pro_total=[[]]*14
sec_poly_total=[[]]*14
for i in range(14):
	sec_pro_total[i], sec_poly_total[i]=section_build.section_build(bridge_width[i], web_quantity, web_thickness[i])
data_templatet, row_add=mct_file_edit.data_template_edit_section(sec_pro_total, sec_poly_total, sec_pos, sec_pos_dgn, data_template)



project_name=bridge_name+'.mct'# 生成模型文件，即midas软件的.mct文件
with open(project_name, 'w') as file_object:
	file_object.writelines(data_template)
