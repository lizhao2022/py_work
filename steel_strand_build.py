span=[30, 30, 30]# ¿ç¾¶×éºÏ£¬3¿çÎªÀı
web_quantity=10# ¸¹°åÊıÁ¿
end_seams=[0.05, 0.05]# Áº¶Ë·ì¿í
def steel_strand_build(span, end_seams, web:
	span1=span[0]-end_seams[0]
	span2=span1+span[1]
	span_end=span2+span[2]-end_seams[1]
	
	d1_x=[4, 7, span1-4, span1-2, span1+2, span1+4, span2-4, span2-2, span2+2, span2+4, span_end-7, span_end-4]
	d2_x=[0.15, 3.15, span1-12.5, span1-9.5]
	d2a_x=[0.15, 3.15, span1-10.5, span1-7.5]
	d3_x=[span2+9.5, span2+12.5, span_end-3.15, span_end-0.15]
	d3a_x=[span2+7.5, span2+10.5, span_end-3.15, span_end-0.15]
	f1_x=[7.8, 11.344, span1-9.076, span1-4, span1+4, span1+9.076, span2-9.076, span2-4, span2+4, span2+9.076, span_end-11.344, span_end-7.8]
	f2_x=[5.3, 9.284, span1-7.628, span1-3, span1+3, span1+7.628, span2-7.628, span2-3, span2+3, span2+7.628, span_end-9.284, span_end-5.3]
	f3_x=[3.3, 7.723, span1-6.292, span1-2, span1+2, span1+6.292, span2-6.292, span2-2, span2+2, span2+6.292, span_end-7.723, span_end-3.3]
	t1_x=[span1-10.5, span1-7.5, span2+7.5, span2+10.5]
	t2_x=[0.15, 2, 2.7, span1+7.5, span1+10.5]
	t3_x=[span2-10.5, span2-7.5, span_end-2.7, span_end-2, span_end-0.15]
	t4_x=[9.85, span_end-9.85]
	t4a_x=[6.55, span_end-6.55]
	steel_x=[d1_x, d2_x, d2a_x, d3_x, d3a_x, f1_x, f2_x, f3_x, t1_x, t2_x, t3_x, t4_x, t4a_x]
	
	d1_y=[-1.4, -1.86, -1.86, -1.825, -1.825, -1.86, -1.86, -1.825, -1.825, -1.86, -1.86, -1.4]
	d2_y=[-1.7, -1.86, -1.86, -1.22]
	d2a_y=[-1.7, -1.86, -1.86, -1.4]
	d3_y=[-1.22, -1.86, -1.86, -1.7]
	d3a_y=[-1.4, -1.86, -1.86, -1.7]
	f1_y=[-0.25, -1.54, -1.54, -0.18, -0.18, -1.54, -1.54, -0.18, -0.18, -1.54, -1.54, -0.25]
	f2_y=[-0.25, -1.7, -1.7, -0.46, -0.46, -1.7, -1.7, -0.46, -0.46, -1.7, -1.7, -0.25]
	f3_y=[-0.25, -1.86, -1.86, -0.71, -0.71, -1.86, -1.86, -0.71, -0.71, -1.86, -1.86, -0.25]
	t1_y=[-0.7, -0.18, -0.18, -0.7]
	t2_y=[-0.22, -0.22, -0.18, -0.18, -0.7]
	t3_y=[-0.7, -0.18, -0.18, -0.22, -0.22]
	t4_y=[-0.18, -0.18]
	t4a_y=[-0.18, -0.18]
	steel_y=[d1_y, d2_y, d2a_y, d3_y, d3a_y, f1_y, f2_y, f3_y, t1_y, t2_y, t3_y, t4_y, t4a_y]
	
	d1_r=[6]*12
	d1_r[0]=0
	d1_r[-1]=0
	d2_r=[0, 6, 6, 0]
	d2a_r=[0, 6, 6, 0]
	d3_r=[0, 6, 6, 0]
	d3a_r=[0, 6, 6, 0]
	f1_r=[10]*12
	f1_r[0]=0
	f1_r[1]=8
	f1_r[-2]=8
	f1_r[-1]=0
	f2_r=[10]*12
	f2_r[0]=0
	f2_r[-1]=0
	f3_r=[0, 10, 10, 8, 8, 10, 10, 8, 8, 10, 10, 0]
	t1_r=[0, 6, 6, 0]
	t2_r=[0, 6, 6, 6, 0]
	t3_r=[0, 6, 6, 6, 0]
	t4_r=[0, 0]
	t4a_r=[0, 0]
	steel_r=[d1_r, d2_r, d2a_r, d3_r, d3a_r, f1_r, f2_r, f3_r, t1_r, t2_r, t3_r, t4_r, t4a_r]
	
	steel_count=[2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web-2, 2*web, 2*web, 2*web, 4*web-6, 2*web, 2*web, 4, 2]
	return steel_x, steel_y, steel_r, steel_count

def steel_strand_str(count, x, y, r):
	steel_str=[[]]*(3+len(x))
	steel_str[0]='        , AUTO1, , , YES, '+str(count)+', 0, 0\n'
	steel_str[1]='        STRAIGHT, 0, 0, 0, X, 0, 0\n'
	steel_str[2]='        0, YES, Y, 0\n'
	for i in range(len(x))
		steel_str[i+3]='        '+str(x[i])+', 0, '+str(y[i])+', NO, 0, 0, '+str(r[i])+'\n'
	return steel_str
