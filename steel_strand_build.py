import math

def steel_f(xe, xp, sp1, sp2, sp3, ye, yp, ys1, ys2, ys3, ae, ap, bh):# 计算腹板束坐标
	yk=[ye, -bh+ys1, yp, -bh+ys2, yp, -bh+ys3, ye]
	a=[ap]*6
	a[0]=ae
	a[-1]=ae
	dx=[0]*(len(yk)-1)
	for j in range(len(yk)-1):
		dy=abs(yk[j+1]-yk[j])
		dx[j]=dy/math.tan(math.radians(a[j]))
	x=[xe, xe+dx[0], sp1-xp-dx[1], sp1-xp, sp1+xp, sp1+xp+dx[2], sp2-xp-dx[3], sp2-xp, sp2+xp, sp2+xp+dx[4], sp3-xe-dx[5], sp3-xe]
	y=[ye, -bh+ys1, -bh+ys1, yp, yp, -bh+ys2, -bh+ys2, yp, yp, -bh+ys3, -bh+ys3, ye]
	return x, y

def steel_det(b_h):# 钢束形状名称
	if b_h >=2.5:
		steel_det=[[]]*16
		steel_det[0]=['D1', 'N-12', '4to78', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[1]=['D1A', 'N-12', '1to20', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[2]=['F1', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[3]=['F2', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[4]=['F3', 'N-12', '11to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[5]=['F4', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[6]=['F5', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[7]=['T1', 'N-12', '4to78', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[8]=['T2', 'N-9', '19to63', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[9]=['T3', 'N-9', '1to37', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[10]=['T4', 'N-9', '45to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[11]=['T5', 'N-9', '10to72', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[12]=['T6', 'N-9', '7to75', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[13]=['T7', 'N-9', '7to75', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[14]=['T8', 'N-9', '7to75', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[15]=['T9', 'N-9', '7to75', 'BOTH', '1.35e+06', '1.35e+06']
	else:
		steel_det=[[]]*13
		steel_det[0]=['D1', 'N-9', '4to78', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[1]=['D2', 'N-9', '1to20', 'END', '0', '1.35e+06']
		steel_det[2]=['D2A', 'N-9', '1to21', 'END', '0', '1.35e+06']
		steel_det[3]=['D3', 'N-9', '62to81', 'BEGIN', '1.35e+06', '0']
		steel_det[4]=['D3A', 'N-9', '61to81', 'BEGIN', '1.35e+06', '0']
		steel_det[5]=['F1', 'N-12', '8to74', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[6]=['F2', 'N-12', '6to76', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[7]=['F3', 'N-12', '4to78', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[8]=['T1', 'N-9', '19to63', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[9]=['T2', 'N-9', '1to37', 'END', '0', '1.35e+06']
		steel_det[10]=['T3', 'N-9', '45to81', 'BEGIN', '1.35e+06', '0']
		steel_det[11]=['T4', 'N-9', '10to72', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[12]=['T4A', 'N-9', '7to75', 'BOTH', '1.35e+06', '1.35e+06']
	return steel_det
	
def steel_strand_build(span, end_seams, web, beam_height, node_x):
	span_1=span[0]-end_seams[0]
	span_2=span_1+span[1]
	span_3=span_2+span[2]-end_seams[1]
	steel_detail=steel_det(beam_height)
	if beam_height >=2.5:
		# 腹板束形状设计参数
		xf_ends=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15]# 腹板束端部起终点水平位置
		xf_pivot=[3.8, 3.3, 2.8, 2.3, 1.8]# 腹板束中支点起终点水平位置
		yf_ends=[-0.45, -0.85, -1.2, -1.55, -1.9]#　腹板束端部竖向位置
		yf_pivot=[-0.18, -0.46, -0.71, -0.92, -1.13]# 腹板束中支点竖向位置
		angle_f_ends=[5.5, 5, 4.5, 4, 3.5]# 腹板束端部弯起角度
		angle_f_pivot=[8.91, 8.77, 8.69, 8.87, 9.08]# 腹板束中支点弯起角度
		yf_span_1=[0.94, 0.74, 0.54, 0.34, 0.14]# 腹板束边跨跨中竖向距离
		yf_span_2=[0.8, 0.62, 0.46, 0.3, 0.14]# 腹板束中跨跨中竖向距离
		yf_span_3=[0.94, 0.74, 0.54, 0.34, 0.14]# 腹板束边跨跨中竖向距离
		# 建立腹板束坐标
		f_x=[[]]*len(xf_ends)
		f_y=[[]]*len(xf_ends)
		for i in range(len(xf_ends)):
			f_x[i], f_y[i]=steel_f(xf_ends[i], xf_pivot[i], span_1, span_2, span_3, yf_ends[i], yf_pivot[i], yf_span_1[i], yf_span_2[i], yf_span_3[i], angle_f_ends[i], angle_f_pivot[i], beam_height)
		# 底板束形状设计参数
		xd_1=[14, 17, -17, -14]# D1水平控制点距离
		xd_1a=[10.5, 13.5, -13.5, -10.5]# D1a水平控制点距离
		yd_1=[0.62, 0.14, 0.14, 0.62]# D1竖向位置
		yd_1a=[0.62, 0.14, 0.14, 0.62]# D1a竖向位置
		# 建立底板束坐标
		d1_x=[span_1+xd_1[0], span_1+xd_1[1], span_2+xd_1[2], span_2+xd_1[3]]
		d1a_x=[span_1+xd_1a[0], span_1+xd_1a[1], span_2+xd_1a[2], span_2+xd_1a[3]]
		d1_y=[-beam_height+i for i in d1_y]
		d1_ya=[-beam_height+i for i in d1_ya]
		# 顶板束形状设计参数
		xt_1=[0.15, 2, 2.7]
		xt_2=[15.5, 12, 8.5, 5]
		xt_c=3
		yt_1=[-0.22, -0.22, -0.18]
		yt_2=[-0.7, -0.7, -0.65, -0.7]
		yt_c=-0.18
		# 建立顶板束坐标
		t1_x=[xt_1[0], xt_1[1], xt_1[2], span_3-xt_1[2], span_3-xt_1[1], span_3-xt_1[0]]
		t1_y=[yt_1[0], yt_1[1], yt_1[2], yt_1[2], yt_1[1], yt_1[0]]
		t2_x=[[]]*len(xt_2)*2
		t2_y=[[]]*len(xt_2)*2
		for i in range(len(xt_2))
			t2_x[i]=[span_1-xt_2[i]-xt_c, span_1-xt_2[i], span_1+xt_2[i]+span_1+xt_2[i]+xt_c]
			t2_x[i+4]=[span_2-xt_2[i]-xt_c, span_2-xt_2[i], span_2+xt_2[i]+span_2+xt_2[i]+xt_c]
			t2_y[i]=[yt_2[i], yt_c, yt_c, yt_2[i]]
			t2_y[i+4]=[yt_2[i], yt_c, yt_c, yt_2[i]]
		#　钢束弯曲半径参数
		dr=6
		fr=30
		fra=[20, 20, 15, 10, 6]
		tr=6
		d1_r=[0, dr, dr, 0]
		f_r=[[]]*len(xf_ends)
		for i in range(len(f_r)):
			f_r[i]=[0, fr, fr, fra[i], fra[i], fr, fr, fra[i], fra[i], fr, fr, 0]
		t1_r=[0, tr, tr, tr, tr, 0]
		t2_r=[[0, tr, tr, 0]]*len(xt_2)*2
		# 整理所有钢束坐标及半径
		steel_x=[d1_x, d2_x, d2a_x, d3_x, d3a_x, f_x[0], f_x[1], f_x[2], t1_x, t2_x, t3_x, t4_x, t4a_x]
		steel_y=[d1_y, d2_y, d2a_y, d3_y, d3a_y, f_y[0], f_y[1], f_y[2], t1_y, t2_y, t3_y, t4_y, t4a_y]
		steel_r=[d1_r, d2_r, d2a_r, d3_r, d3a_r, f_r[0], f_r[1], f_r[2], t1_r, t2_r, t3_r, t4_r, t4a_r]
		steel_count=[2*web-2, 2*web-2, 2*web, 2*web, 2*web, 2*web, 2*web, 2*web+2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2]
	else:
		# 腹板束形状设计参数
		xf_ends=[7.8, 5.3, 3.3]# 腹板束端部起终点水平位置
		xf_pivot=[4, 3, 2]# 腹板束中支点起终点水平位置
		yf_ends=[-0.2, -0.2, -0.2]#　腹板束端部竖向位置
		yf_pivot=[-0.18, -0.46, -0.71]# 腹板束中支点竖向位置
		angle_f_ends=[20, 20, 20]# 腹板束端部弯起角度
		angle_f_pivot=[15, 15, 15]# 腹板束中支点弯起角度
		yf_span_1=[0.46, 0.3, 0.14]# 腹板束边跨跨中竖向距离
		yf_span_2=[0.46, 0.3, 0.14]# 腹板束中跨跨中竖向距离
		yf_span_3=[0.46, 0.3, 0.14]# 腹板束边跨跨中竖向距离		
		# 建立腹板束坐标
		f_x=[[]]*len(xf_ends)
		f_y=[[]]*len(xf_ends)
		for i in range(len(xf_ends)):
			f_x[i], f_y[i]=steel_f(xf_ends[i], xf_pivot[i], span_1, span_2, span_3, yf_ends[i], yf_pivot[i], yf_span_1[i], yf_span_2[i], yf_span_3[i], angle_f_ends[i], angle_f_pivot[i], beam_height)
		# 底板束形状设计参数
		xd_l=[4, 7, 4, 2]# 通长束D1水平控制点距离[端部，端部，支点，支点]
		xd_s=[0.15, 3.15, 12.5, 9.5]# 短束D2D3水平控制点距离
		xd_a=[0, 0, 2, 2]# 短束D2AD3A水平控制点相对D2D3距离
		yd_l=[0.6, 0.14, 0.175]# 通长束D1竖向位置[端部，跨中，支点]
		yd_s=[0.3, 0.14, 0.14, 0.78]# 短束D2D3竖向位置
		yd_a=[0.3, 0.14, 0.14, 0.6]# 短束D2AD3A竖向位置
		# 建立底板束x坐标
		d1_x=[xd_l[0], xd_l[1], span_1-xd_l[2], span_1-xd_l[3], span_1+xd_l[3], span_1+xd_l[2], span_2-xd_l[2], span_2-xd_l[3], span_2+xd_l[3], span_2+xd_l[2], span_3-xd_l[1], span_3-xd_l[0]]
		d2_x=[xd_s[0], xd_s[1], span_1-xd_s[2], span_1-xd_s[3]]
		d2a_x=[i+j for i, j in zip(xd_a, d2_x)]
		d3_x=[span_2+xd_s[3], span_2+xd_s[2], span_3-xd_s[1], span_3-xd_s[0]]
		d3a_x=[-i+j for i, j in zip(list(reversed(xd_a)), d3_x)]
		# 建立底板束y坐标
		d1_y=[yd_l[0], yd_l[1], yd_l[1], yd_l[2], yd_l[2], yd_l[1], yd_l[1], yd_l[2], yd_l[2], yd_l[1], yd_l[1], yd_l[0]]
		d1_y=[-beam_height+i for i in d1_y]
		d2_y=[-beam_height+i for i in yd_s]
		d2a_y=[-beam_height+i for i in yd_a]
		d3_y=[-beam_height+i for i in list(reversed(yd_s))]
		d3a_y=[-beam_height+i for i in list(reversed(yd_a))]
		# 顶板束形状设计参数
		xt_1=[10.5, 7.5]
		xt_2=[0.15, 2, 2.7, 7.5, 10.5]
		xt_3=list(reversed(xt_2))
		xt_c=[9.85, 6.55]
		yt_1=[-0.7, -0.18]
		yt_2=[-0.22, -0.18, -0.7]
		yt_c=-0.18
		# 建立顶板束x坐标
		t1_x=[span_1-xt_1[0], span_1-xt_1[1], span_2+xt_1[1], span_2+xt_1[0]]
		t2_x=[xt_2[0], xt_2[1], xt_2[2], span_1+xt_2[3], span_1+xt_2[4]]
		t3_x=[span_2-xt_3[0], span_2-xt_3[1], span_3-xt_3[2], span_3-xt_3[3], span_3-xt_3[4]]
		t4_x=[xt_c[0], span_3-xt_c[0]]
		t4a_x=[xt_c[1], span_3-xt_c[1]]
		# 建立顶板束y坐标
		t1_y=[yt_1[0], yt_1[1], yt_1[1], yt_1[0]]
		t2_y=[yt_2[0], yt_2[0], yt_2[1], yt_2[1], yt_2[2]]
		t3_y=list(reversed(t2_y))
		t4_y=[yt_c, yt_c]
		t4a_y=[yt_c, yt_c]
		#　钢束弯曲半径参数
		dr=6
		tr=6
		fr=10
		d1_r=[dr]*12
		d1_r[0]=0
		d1_r[-1]=0
		#　建立钢束弯曲半径
		d2_r=[0, dr, dr, 0]
		d2a_r=[0, dr, dr, 0]
		d3_r=[0, dr, dr, 0]
		d3a_r=[0, dr, dr, 0]
		f_r=[[]]*len(xf_ends)
		for i in range(len(xf_ends)):
			f_r[i]=[fr]*12
			f_r[i][0]=0
			f_r[i][-1]=0
		t1_r=[0, tr, tr, 0]
		t2_r=[0, tr, tr, tr, 0]
		t3_r=[0, tr, tr, tr, 0]
		t4_r=[0, 0]
		t4a_r=[0, 0]
		
		# 整理所有钢束坐标及半径
		steel_x=[d1_x, d2_x, d2a_x, d3_x, d3a_x, f_x[0], f_x[1], f_x[2], t1_x, t2_x, t3_x, t4_x, t4a_x]
		steel_y=[d1_y, d2_y, d2a_y, d3_y, d3a_y, f_y[0], f_y[1], f_y[2], t1_y, t2_y, t3_y, t4_y, t4a_y]
		steel_r=[d1_r, d2_r, d2a_r, d3_r, d3a_r, f_r[0], f_r[1], f_r[2], t1_r, t2_r, t3_r, t4_r, t4a_r]
		steel_count=[2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web, 2*web, 2*web, 4*web-6, 2*web, 2*web, 4, 2]	
	return steel_x, steel_y, steel_r, steel_count, steel_detail
