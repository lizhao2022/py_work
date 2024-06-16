import numpy as np
# ~ import node_partition as node

# ~ span=[30, 30, 30]# 跨径组合，3跨为例
# ~ crossbeam=[2, 3, 3, 2]# 横梁宽度，3跨4支点为例
# ~ pedestal_position=[0.6, 0.6]# 边支座距梁端，2边支点
# ~ end_seams=[0.05, 0.05]# 梁端缝宽
# ~ web_thickened_length=[7.4, 4.4, 4.4, 4.4, 4.4, 7.4]# 腹板加厚段长度，每跨2处，3跨6处
# ~ web_thickening_length=[3.6, 3.6, 3.6, 3.6, 3.6, 3.6]# 腹板变厚段长度，每跨2处，3跨6处
# ~ plate_thickening_length=[1.2, 1, 1, 1, 1, 1.2]# 顶底板加腋长度，每跨2处，3跨6处
# ~ bridge_width=[49.96, 49.488, 49.248, 48.712, 48.391, 47.2, 46.836, 45.726, 45.363, 44.172, 45.808, 43.056, 42.693, 41.744]# 14个控制截面宽度
# ~ web_quantity=10# 腹板数量
# ~ bumperwall_width=[0.525, 0.65, 0.525]# 防撞墙宽度

# ~ node_x, node_z=node.node_partition(span, crossbeam, pedestal_position, end_seams, web_thickened_length, web_thickening_length, plate_thickening_length)

def pave_bumperwall_load(bumperwall_width, bridge_width, node_x):
	'''# 计算铺装荷载'''
	xp=[0.525, 0.65, 0.7 ,0.9]# 防撞墙宽度插值区间
	fp=[-11, -13, -18.5, -19.2]# 防撞墙宽度对应线荷载
	wall_load=np.interp(bumperwall_width, xp, fp)# 按宽度线性插值
	bumperwall_load=[sum(wall_load)]*82
	pave_t1=0.08# 铺装层厚度
	pave_t2=0.1# 调平层厚度
	pave_load_sec=[(x-sum(bumperwall_width))*(pave_t1*(-24)+pave_t2*(-26)) for x in bridge_width]# 按控制截面计算
	x=[0, 9, 12, 19, 22, 32, 35, 46, 49, 59, 62, 69, 72, 81]
	pave_load_x=[[]]*82
	for i in range(len(x)-1):
		sta=x[i]
		end=x[i+1]
		xp=[node_x[sta], node_x[end]]
		fp=[pave_load_sec[i],pave_load_sec[i+1]]
		pave_load_x[sta:end+1]=np.interp(node_x[sta:end+1], xp, fp)# 按节点位置线性插值
	return pave_load_x, bumperwall_load

def crossbeam_plate_load(web_quantity, bridge_width):
	'''# 计算横梁荷载及顶底板加腋荷载'''
	plate_width=[0]*4
	plate_width[0]=bridge_width[0]
	plate_width[1]=bridge_width[4]/2+bridge_width[5]/2
	plate_width[2]=bridge_width[8]/2+bridge_width[9]/2
	plate_width[3]=bridge_width[13]
	box_width=[(x-5.2*2-web_quantity*0.8) for x in plate_width]# 计算中间箱室总宽度
	crossbeam_load=[(1.5*2+x*(2-0.28-0.22)-(web_quantity-1)*(1*0.2+0.6*0.2))*(-26) for x in box_width]# 两侧小箱面积1.5*2
	plate_load=[(x*(0.2+0.2)+1.8*2*0.2)*(-26) for x in box_width]# 顶底板加腋厚0.2+0.2，两侧小箱顶板加腋0.2
	return crossbeam_load, plate_load

def tem_load(web_quantity, bridge_width, node_x):
	'''# 计算温度荷载宽度参数'''
	x=[0, 9, 12, 19, 22, 32, 35, 46, 49, 59, 62, 69, 72, 81]
	fp=bridge_width
	tem_width_1=[[]]*82
	for i in range(len(x)-1):
		sta=x[i]
		end=x[i+1]
		xp=[node_x[sta], node_x[end]]
		fp=[bridge_width[i],bridge_width[i+1]]
		tem_width_1[sta:end+1]=np.interp(node_x[sta:end+1], xp, fp)# 按节点位置线性插值
	tem_width_2=[(web_quantity*2.4+2.5*2)]*82
	tem_h=[0, 0.1, 0.28, 0.4]
	tem_up=[14, 5.5, 2.2, 0]
	tem_down=[-7, -2.75, -1.1, 0]
	return tem_width_1, tem_width_2, tem_h, tem_up, tem_down

def lane_fac(bridge_width, bumperwall_width, node_x):
	'''# 根据桥宽计算车道数'''
	a=len(bumperwall_width)-1# 计算单幅/双幅
	lane_xp=[6, 7, 10.5, 14, 17.5, 21, 24.5, 28, 31.5]
	lane_fp=[1, 2, 3, 4, 5, 6, 7, 8, 9]
	tra_fac=[1.2, 1, 0.78, 0.67, 0.6, 0.55, 0.52, 0.5, 0.5]
	lane_width=[(x-sum(bumperwall_width))/a for x in bridge_width]# 计算单幅车道净宽
	lane_num=[int(np.interp(x, lane_xp, lane_fp)) for x in lane_width]# 计算控制截面车道数，按宽度插值，并向下取整
	lane_sec=[x*np.interp(x, lane_fp, tra_fac) for x in lane_num]# 考虑车道数横向折减
	x=[0, 9, 12, 19, 22, 32, 35, 46, 49, 59, 62, 69, 72, 81]
	fac=[0]*82
	for i in range(len(x)-1):
		sta=x[i]
		end=x[i+1]
		xp=[node_x[sta], node_x[end]]
		fp=[lane_sec[i],lane_sec[i+1]]
		fac[sta:end+1]=np.interp(node_x[sta:end+1], xp, fp)# 按节点位置线性插值
	lane_fac=[y/fac[0] for y in fac]# 计算相对值
	return lane_fac, fac[0]*1.15*a
