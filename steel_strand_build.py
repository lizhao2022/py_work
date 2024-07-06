import math

def steel_f(xe, xp, sp1, sp2, sp3, ye, yp, ys1, ys2, ys3, ae, ap, bh):# ���㸹��������
	yk=[ye, bh-ys1, yp, bh-ys2, yp, bh-ys3, ye]
	a=[ap]*6
	a[0]=ae
	a[-1]=ae
	dx=[0]*(len(yk)-1)
	for j in range(len(yk)-1):
		dy=yk[j+1]-yk[j]
		dx[j]=dy/math.tan(math.radians(a[j]))
	x=[xe, xe+dx[0], sp1-dx[1], sp1-xp, sp1+xp, sp1+dx[2], sp2-dx[3], sp2-xp, sp2+xp, sp2+dx[4], sp3-dx[5], sp3-xe]
	y=[ye, bh-ys1, bh-ys1, yp, yp, bh-ys2, bh-ys2, yp, yp, bh-ys3, bh-ys3, ye]
	return x, y

def steel_strand_build(span, end_seams, web, beam_height):
	span_1=span[0]-end_seams[0]
	span_2=span_1+span[1]
	span_3=span_2+span[2]-end_seams[1]
	
	# ��������״��Ʋ���
	xf_ends=[7.8, 5.3, 3.3]# �������˲����յ�ˮƽλ��
	xf_pivot=[4, 3, 2]# ��������֧�����յ�ˮƽλ��
	yf_ends=[-0.2, -0.2, -0.2]#���������˲�����λ��
	yf_pivot=[-0.18, -0.46, -0.71]# ��������֧������λ��
	angle_f_ends=[20, 20, 20]# �������˲�����Ƕ�
	angle_f_pivot=[15, 15, 15]# ��������֧������Ƕ�
	yf_span_1=[0.46, 0.3, 0.14]# �������߿�����������
	yf_span_2=[0.46, 0.3, 0.14]# �������п�����������
	yf_span_3=[0.46, 0.3, 0.14]# �������߿�����������
	# ��������������
	f_x=[[]]*len(xf_ends)
	f_y=[[]]*len(xf_ends)
	for i in range(len(xf_ends)):
		f_x[i], f_y[i]=steel_f(xf_ends[i], xf_pivot[i], span_1, span_2, span_3, yf_ends[i], yf_pivot[i], yf_span_1[i], yf_span_2[i], yf_span_3[i], angle_f_ends[i], angle_f_pivot[i], beam_height)
	
	# ��������״��Ʋ���
	xd_l=[4, 7, 4, 2]# ͨ����D1ˮƽ���Ƶ����[�˲����˲���֧�㣬֧��]
	xd_s=[0.15, 3.15, 12.5, 9.5]# ����D2D3ˮƽ���Ƶ����
	xd_a=[0, 0, 2, 2]# ����D2AD3Aˮƽ���Ƶ����D2D3����
	yd_l=[0.6, 0.14, 0.175]# ͨ����D1����λ��[�˲������У�֧��]
	yd_s=[0.3, 0.14, 0.14, 0.78]# ����D2D3����λ��
	yd_a=[0.3, 0.14, 0.14, 0.6]# ����D2AD3A����λ��
	# �����װ���x����
	d1_x=[xd_l[0], xd_l[1], span_1-xd_l[2], span_1-xd_l[3], span_1+xd_l[3], span_1+xd_l[2], span_2-xd_l[2], span_2-xd_l[3], span_2+xd_l[3], span_2+xd_l[2], span_3-xd_l[1], span_3-xd_l[0]]
	d2_x=[xd_s[0], xd_s[1], span_1-xd_s[2], span_1-xd_s[3]]
	d2a_x=[i+j for i, j in zip(xd_a, d2_x)]
	d3_x=[span_2+xd_s[3], span_2+xd_s[2], span_3-xd_s[1], span_3-xd_s[0]]
	d3a_x=[-i+j for i, j in zip(list(reversed(xd_a)), d3_x)]
	# �����װ���y����
	d1_y=[yd_l[0], yd_l[1], yd_l[1], yd_l[2], yd_l[2], yd_l[1], yd_l[1], yd_l[2], yd_l[2], yd_l[1], yd_l[1], yd_l[0]]
	d1_y=[-beam_height+i for i in d1_y]
	d2_y=[-beam_height+i for i in yd_s]
	d2a_y=[-beam_height+i for i in yd_a]
	d3_y=[-beam_height+i for i in list(reversed(yd_s))]
	d3a_y=[-beam_height+i for i in list(reversed(yd_a))]
	
	# ��������״��Ʋ���
	xt_1=[10.5, 7.5]
	xt_2=[0.15, 2, 2.7, 7.5, 10.5]
	xt_3=list(reversed(xt_2))
	xt_c=[9.85, 6.55]
	yt_1=[-0.7, -0.18]
	yt_2=[-0.22, -0.18, -0.7]
	yt_c=-0.18
	# ����������x����
	t1_x=[span_1-xt_1[0], span_1-xt_1[1], span_2+xt_1[1], span_2+xt_1[0]]
	t2_x=[xt_2[0], xt_2[1], xt_2[2], span_1+xt_2[3], span_1+xt_2[4]]
	t3_x=[span_2-xt_3[0], span_2-xt_3[1], span_3-xt_3[2], span_3-xt_3[3], span_3-xt_3[4]]
	t4_x=[xt_c[0], span_3-xt_c[0]]
	t4a_x=[xt_c[1], span_3-xt_c[1]]
	# ����������y����
	t1_y=[yt_1[0], yt_1[1], yt_1[1], yt_1[0]]
	t2_y=[yt_2[0], yt_2[0], yt_2[1], yt_2[1], yt_2[2]]
	t3_y=list(reversed(t2_y))
	t4_y=[yt_c, yt_c]
	t4a_y=[yt_c, yt_c]
	
	#�����������뾶����
	dr=6
	tr=6
	fr=10
	d1_r=[dr]*12
	d1_r[0]=0
	d1_r[-1]=0
	#���������������뾶
	d2_r=[0, dr, dr, 0]
	d2a_r=[0, dr, dr, 0]
	d3_r=[0, dr, dr, 0]
	d3a_r=[0, dr, dr, 0]
	f_r=[[]]*len(xf_ends)
	for i in range(len(xf_ends)):
		f1_r=[fr]*12
		f1_r[0]=0
		f1_r[-1]=0
	t1_r=[0, tr, tr, 0]
	t2_r=[0, tr, tr, tr, 0]
	t3_r=[0, tr, tr, tr, 0]
	t4_r=[0, 0]
	t4a_r=[0, 0]
	
	# �������и������꼰�뾶
	steel_x=[d1_x, d2_x, d2a_x, d3_x, d3a_x, f_x[0], f_x[1], f_x[2], t1_x, t2_x, t3_x, t4_x, t4a_x]
	steel_y=[d1_y, d2_y, d2a_y, d3_y, d3a_y, f_y[0], f_y[1], f_y[2], t1_y, t2_y, t3_y, t4_y, t4a_y]
	steel_r=[d1_r, d2_r, d2a_r, d3_r, d3a_r, f_r[0], f_r[1], f_r[2], t1_r, t2_r, t3_r, t4_r, t4a_r]
	
	steel_count=[2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web, 2*web, 2*web, 4*web-6, 2*web, 2*web, 4, 2]
	return steel_x, steel_y, steel_r, steel_count
