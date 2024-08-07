import math
import numpy as np

def steel_det(b_h):# ������״����
	if b_h >=2.5:
		steel_det=[[]]*16
		steel_det[0]=['D1', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[1]=['D1A', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[2]=['F1', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[3]=['F2', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[4]=['F3', 'N-12', '11to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[5]=['F4', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[6]=['F5', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[7]=['T1', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[8]=['T2', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[9]=['T3', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[10]=['T4', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[11]=['T5', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[12]=['T6', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[13]=['T7', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[14]=['T8', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[15]=['T9', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
	else:
		steel_det=[[]]*13
		steel_det[0]=['D1', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[1]=['D2', 'N-9', '1to81', 'END', '0', '1.35e+06']
		steel_det[2]=['D2A', 'N-9', '1to81', 'END', '0', '1.35e+06']
		steel_det[3]=['D3', 'N-9', '1to81', 'BEGIN', '1.35e+06', '0']
		steel_det[4]=['D3A', 'N-9', '1to81', 'BEGIN', '1.35e+06', '0']
		steel_det[5]=['F1', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[6]=['F2', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[7]=['F3', 'N-12', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[8]=['T1', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[9]=['T2', 'N-9', '1to81', 'END', '0', '1.35e+06']
		steel_det[10]=['T3', 'N-9', '1to81', 'BEGIN', '1.35e+06', '0']
		steel_det[11]=['T4', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
		steel_det[12]=['T4A', 'N-9', '1to81', 'BOTH', '1.35e+06', '1.35e+06']
	return steel_det

def steel_r(x):# ���װ����뾶
	r=[[]]*len(x)
	for i in range(len(r)):
		r[i]=[0]+[6]*(len(x[i])-2)+[0]
	return r

def steel_f(xe, xp, sp1, sp2, sp3, ye, yp, ys1, ys2, ys3, ae, ap, bh):# ���㸹��������
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

def steel_d_2(sp1, sp2, sp3, bh):# ����2-2.3�װ�������
	# �װ�����״��Ʋ���
	xd_l=[4, 7, 4, 2]# ͨ����D1ˮƽ���Ƶ����[�˲����˲���֧�㣬֧��]
	xd_s=[0.15, 3.15, 12.5, 9.5]# ����D2D3ˮƽ���Ƶ����
	xd_a=[0, 0, 2, 2]# ����D2AD3Aˮƽ���Ƶ����D2D3����
	yd_l=[0.6, 0.14, 0.175]# ͨ����D1����λ��[�˲������У�֧��]
	yd_s=[0.3, 0.14, 0.14, 0.78]# ����D2D3����λ��
	yd_a=[0.3, 0.14, 0.14, 0.6]# ����D2AD3A����λ��
	# �����װ���x����
	d1_x=[xd_l[0], xd_l[1], sp1-xd_l[2], sp1-xd_l[3], sp1+xd_l[3], sp1+xd_l[2], sp2-xd_l[2], sp2-xd_l[3], sp2+xd_l[3], sp2+xd_l[2], sp3-xd_l[1], sp3-xd_l[0]]
	d2_x=[xd_s[0], xd_s[1], sp1-xd_s[2], sp1-xd_s[3]]
	d2a_x=[i+j for i, j in zip(xd_a, d2_x)]
	d3_x=[sp2+xd_s[3], sp2+xd_s[2], sp3-xd_s[1], sp3-xd_s[0]]
	d3a_x=[-i+j for i, j in zip(list(reversed(xd_a)), d3_x)]
	# �����װ���y����
	d1_y=[yd_l[0], yd_l[1], yd_l[1], yd_l[2], yd_l[2], yd_l[1], yd_l[1], yd_l[2], yd_l[2], yd_l[1], yd_l[1], yd_l[0]]
	d1_y=[-bh+i for i in d1_y]
	d2_y=[-bh+i for i in yd_s]
	d2a_y=[-bh+i for i in yd_a]
	d3_y=[-bh+i for i in list(reversed(yd_s))]
	d3a_y=[-bh+i for i in list(reversed(yd_a))]
	x=[d1_x, d2_x, d2a_x, d3_x, d3a_x]
	y=[d1_y, d2_y, d2a_y, d3_y, d3a_y]
	r=steel_r(x)
	return x, y, r

def steel_d_3(sp1, sp2, sp3, bh):#����2.5�װ�������
	# �װ�����״��Ʋ���
	xd_1=[14, 17, -17, -14]# D1ˮƽ���Ƶ����
	xd_1a=[10.5, 13.5, -13.5, -10.5]# D1aˮƽ���Ƶ����
	yd_1=[0.62, 0.14, 0.14, 0.62]# D1����λ��
	yd_1a=[0.62, 0.14, 0.14, 0.62]# D1a����λ��
	# �����װ�������
	d1_x=[sp1+xd_1[0], sp1+xd_1[1], sp2+xd_1[2], sp2+xd_1[3]]
	d1a_x=[sp1+xd_1a[0], sp1+xd_1a[1], sp2+xd_1a[2], sp2+xd_1a[3]]
	d1_y=[-bh+i for i in yd_1]
	d1a_y=[-bh+i for i in yd_1a]
	x=[d1_x, d1a_x]
	y=[d1_y, d1a_y]
	r=steel_r(x)
	return x, y, r

def steel_t_2(sp1, sp2, sp3):# ����2-2.3����������
	# ��������״��Ʋ���
	xt_1=[10.5, 7.5]
	xt_2=[0.15, 2, 2.7, 7.5, 10.5]
	xt_3=list(reversed(xt_2))
	xt_c=[9.85, 6.55]
	yt_1=[-0.7, -0.18]
	yt_2=[-0.22, -0.18, -0.7]
	yt_c=-0.18
	# ����������x����
	t1_x=[sp1-xt_1[0], sp1-xt_1[1], sp2+xt_1[1], sp2+xt_1[0]]
	t2_x=[xt_2[0], xt_2[1], xt_2[2], sp1+xt_2[3], sp1+xt_2[4]]
	t3_x=[sp2-xt_3[0], sp2-xt_3[1], sp3-xt_3[2], sp3-xt_3[3], sp3-xt_3[4]]
	t4_x=[xt_c[0], sp3-xt_c[0]]
	t4a_x=[xt_c[1], sp3-xt_c[1]]
	# ����������y����
	t1_y=[yt_1[0], yt_1[1], yt_1[1], yt_1[0]]
	t2_y=[yt_2[0], yt_2[0], yt_2[1], yt_2[1], yt_2[2]]
	t3_y=list(reversed(t2_y))
	t4_y=[yt_c, yt_c]
	t4a_y=[yt_c, yt_c]
	x=[t1_x, t2_x, t3_x, t4_x, t4a_x]
	y=[t1_y, t2_y, t3_y, t4_y, t4a_y]
	r=steel_r(x)
	return x, y, r

def steel_t_3(sp1, sp2, sp3):# ����2.5����������
	# ��������״��Ʋ���
	xt_1=[0.15, 2, 2.7]
	xt_2=[15.5, 12, 8.5, 5]
	xt_c=3
	yt_1=[-0.22, -0.22, -0.18]
	yt_2=[-0.7, -0.7, -0.65, -0.7]
	yt_c=-0.18
	# ��������������
	t1_x=[xt_1[0], xt_1[1], xt_1[2], sp3-xt_1[2], sp3-xt_1[1], sp3-xt_1[0]]
	t1_y=[yt_1[0], yt_1[1], yt_1[2], yt_1[2], yt_1[1], yt_1[0]]
	t2_x=[[]]*len(xt_2)*2
	t2_y=[[]]*len(xt_2)*2
	for i in range(len(xt_2)):
		t2_x[i]=[sp1-xt_2[i]-xt_c, sp1-xt_2[i], sp1+xt_2[i], sp1+xt_2[i]+xt_c]
		t2_x[i+4]=[sp2-xt_2[i]-xt_c, sp2-xt_2[i], sp2+xt_2[i], sp2+xt_2[i]+xt_c]
		t2_y[i]=[yt_2[i], yt_c, yt_c, yt_2[i]]
		t2_y[i+4]=[yt_2[i], yt_c, yt_c, yt_2[i]]
	x=[t1_x]+t2_x
	y=[t1_y]+t2_y
	r=steel_r(x)
	return x, y, r

def steel_det_elenum(std, sx, nx):# ����������յ��Ӧ��Ԫ��
	for i in range(len(std)):
		pos=np.searchsorted(nx[:-4], [sx[i][0],sx[i][-1]])
		std[i][2]=str(pos[0])+'to'+str(pos[1])
	return std

def steel_strand_build(span, end_seams, web, beam_height, node_x):
	span_1=span[0]-end_seams[0]
	span_2=span_1+span[1]
	span_3=span_2+span[2]-end_seams[1]
	steel_detail=steel_det(beam_height)
	# ��������״��Ʋ���
	if beam_height >=2.5:
		xf_ends=[0.15, 0.15, 0.15, 0.15, 0.15]# �������˲����յ�ˮƽλ��
		xf_pivot=[3.8, 3.3, 2.8, 2.3, 1.8]# ��������֧�����յ�ˮƽλ��
		yf_ends=[-0.45, -0.85, -1.2, -1.55, -1.9]#���������˲�����λ��
		yf_pivot=[-0.18, -0.46, -0.71, -0.92, -1.13]# ��������֧������λ��
		angle_f_ends=[5.5, 5, 4.5, 4, 3.5]# �������˲�����Ƕ�
		angle_f_pivot=[8.91, 8.77, 8.69, 8.87, 9.08]# ��������֧������Ƕ�
		yf_span_1=[0.94, 0.74, 0.54, 0.34, 0.14]# �������߿�����������
		yf_span_2=[0.8, 0.62, 0.46, 0.3, 0.14]# �������п�����������
		yf_span_3=[0.94, 0.74, 0.54, 0.34, 0.14]# �������߿�����������
		f_r=[[0]+[30]*10+[0]]*len(xf_ends)# �����������뾶
		fra=[20, 20, 15, 10, 6]
		for i in range(5):
			f_r[i][3:5]=[fra[i]]*2
			f_r[i][7:9]=[fra[i]]*2
	else:
		xf_ends=[7.8, 5.3, 3.3]# �������˲����յ�ˮƽλ��
		xf_pivot=[4, 3, 2]# ��������֧�����յ�ˮƽλ��
		yf_ends=[-0.2, -0.2, -0.2]#���������˲�����λ��
		yf_pivot=[-0.18, -0.46, -0.71]# ��������֧������λ��
		angle_f_ends=[20, 20, 20]# �������˲�����Ƕ�
		angle_f_pivot=[15, 15, 15]# ��������֧������Ƕ�
		yf_span_1=[0.46, 0.3, 0.14]# �������߿�����������
		yf_span_2=[0.46, 0.3, 0.14]# �������п�����������
		yf_span_3=[0.46, 0.3, 0.14]# �������߿�����������	
		if beam_height >=2.3:
			yf_span_1=[0.2, 0.5, 0.8]
			yf_span_3=[0.2, 0.5, 0.8]
		f_r=[[0]+[10]*10+[0]]*len(xf_ends)#�������������뾶
	# ��������������
	f_x=[[]]*len(xf_ends)
	f_y=[[]]*len(xf_ends)
	for i in range(len(xf_ends)):
		f_x[i], f_y[i]=steel_f(xf_ends[i], xf_pivot[i], span_1, span_2, span_3, yf_ends[i], yf_pivot[i], yf_span_1[i], yf_span_2[i], yf_span_3[i], angle_f_ends[i], angle_f_pivot[i], beam_height)
	if beam_height >=2.5:
		d_x, d_y, d_r=steel_d_3(span_1, span_2, span_3, beam_height)
		t_x, t_y, t_r=steel_t_3(span_1, span_2, span_3)
	else:
		d_x, d_y, d_r=steel_d_2(span_1, span_2, span_3, beam_height)
		t_x, t_y, t_r=steel_t_2(span_1, span_2, span_3)
	# �������и������꼰�뾶
	steel_x=d_x+f_x+t_x
	steel_y=d_y+f_y+t_y
	steel_r=d_r+f_r+t_r
	# �����������
	if beam_height >=2.5:
		d_c=[2*web-2]*2
		f_c=[2*web]*5
		t_c=[2*web-2]*9
		t_c[0]=2*web+2
	else:
		d_c=[2*web-2]*5
		f_c=[2*web]*3
		t_c=[4*web-6, 2*web, 2*web, 4, 2]
	steel_c=d_c+f_c+t_c
	# �޸ĸ���Ӧ�õ�Ԫ
	steel_detail=steel_det_elenum(steel_detail, steel_x, node_x)
	return steel_x, steel_y, steel_r, steel_c, steel_detail

