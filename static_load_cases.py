import numpy as np
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
pave_t1=0.08# 铺装层厚度
pave_t2=0.1# 调平层厚度
bumperwall_width=[0.625, 0.7, 0.625]# 防撞墙宽度
stirrups_diameter=14# 抗剪箍筋直径
node_x, node_z=node.node_partition(span, crossbeam, pedestal_position, end_seams, web_thickened_length, web_thickening_length, plate_thickening_length)


pave_load_sec=[(x-sum(bumperwall_width))*(pave_t1*24+pave_t2*26) for x in bridge_width]
print(pave_load_sec)
x=[0, 9, 12, 19, 22, 32, 35, 46, 49, 59, 62, 69, 72, 81]
pave_load_x=[[]]*82
for i in range(len(x)-1):
	sta=x[i]
	end=x[i+1]
	xp=[node_x[sta], node_x[end]]
	fp=[pave_load_sec[i],pave_load_sec[i+1]]
	pave_load_x[sta:end+1]=np.interp(node_x[sta:end+1], xp, fp)

