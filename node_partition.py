# 程序用于自动划分节点x坐标，应用范围：直线3跨连续梁
# 输入参数为：跨径组合、横梁宽度、支座梁端距、梁端缝宽、腹板加厚段长度、腹板变厚段长度、顶底板加腋长度
# 输出参数为：列表node_x，表示连续梁单元节点及虚拟支座节点x坐标
span=[30, 30, 30]# 跨径组合，3跨为例
crossbeam=[2, 3, 3, 2]# 横梁宽度，3跨4支点为例
pedestal_position=[0.6, 0.6]# 边支座距梁端，2边支点
end_seams=[0.05, 0.05]# 梁端缝宽
web_thickened_length=[7.4, 4.4, 4.4, 4.4, 4.4, 7.4]# 腹板加厚段长度，每跨2处，3跨6处
web_thickening_length=[3.6, 3.6, 3.6, 3.6, 3.6, 3.6]# 腹板变厚段长度，每跨2处，3跨6处
plate_thickening_length=[1.2, 1, 1, 1, 1, 1.2]# 顶底板加腋长度，每跨2处，3跨6处

node_x=list(range(86))# 初始划分主梁节点，3跨标准82节点，81个梁单元，4个虚拟支座节点

node_x[0]=0# 首节点位置
node_x[1]=pedestal_position[0]# D0位置
node_x[27]=span[0]-end_seams[0]# D1位置
node_x[54]=span[1]+span[0]-end_seams[0]# D2位置
node_x[80]=span[2]+span[1]+span[0]-end_seams[0]-end_seams[1]-pedestal_position[1]# D3位置
node_x[81]=span[2]+span[1]+span[0]-end_seams[0]-end_seams[1]# 尾节点位置

node_x[82]=node_x[1]# 虚拟支座节点与D0位置对应
node_x[83]=node_x[27]# 虚拟支座节点与D1位置对应
node_x[84]=node_x[54]# 虚拟支座节点与D2位置对应
node_x[85]=node_x[80]# 虚拟支座节点与D3位置对应

node_x[2]=node_x[1]+crossbeam[0]-pedestal_position[0]# D0横梁
node_x[3]=node_x[1]+crossbeam[0]-pedestal_position[0]+plate_thickening_length[0]# D0+顶底板变厚

node_x[25]=node_x[27]-crossbeam[1]/2-plate_thickening_length[1]# D1-顶底板变厚
node_x[26]=node_x[27]-crossbeam[1]/2# D1-横梁
node_x[28]=node_x[27]+crossbeam[1]/2# D1+横梁
node_x[29]=node_x[27]+crossbeam[1]/2+plate_thickening_length[2]# D1+顶底板变厚

node_x[52]=node_x[54]-crossbeam[2]/2-plate_thickening_length[3]# D2-顶底板变厚
node_x[53]=node_x[54]-crossbeam[2]/2# D2-横梁
node_x[55]=node_x[54]+crossbeam[2]/2# D2+横梁
node_x[56]=node_x[54]+crossbeam[2]/2+plate_thickening_length[4]# D2+顶底板变厚

node_x[78]=node_x[80]-crossbeam[3]+pedestal_position[1]-plate_thickening_length[5]# D3-顶底板变厚
node_x[79]=node_x[80]-crossbeam[3]+pedestal_position[1]# D3横梁

node_x[9]=node_x[2]+web_thickened_length[0]# D0+腹板变厚起点
node_x[10]=node_x[9]+web_thickening_length[0]/3# D0+腹板变厚
node_x[11]=node_x[10]+web_thickening_length[0]/3# D0+腹板变厚
node_x[12]=node_x[11]+web_thickening_length[0]/3# D0+腹板变厚终点

node_x[19]=node_x[26]-web_thickened_length[1]-web_thickening_length[1]# D1-腹板变厚起点
node_x[20]=node_x[19]+web_thickening_length[1]/3# D1-腹板变厚
node_x[21]=node_x[20]+web_thickening_length[1]/3# D1-腹板变厚
node_x[22]=node_x[21]+web_thickening_length[1]/3# D1-腹板变厚终点

node_x[32]=node_x[28]+web_thickened_length[2]# D1+腹板变厚起点
node_x[33]=node_x[32]+web_thickening_length[2]/3# D1+腹板变厚
node_x[34]=node_x[33]+web_thickening_length[2]/3# D1+腹板变厚
node_x[35]=node_x[34]+web_thickening_length[2]/3# D1+腹板变厚终点

node_x[46]=node_x[53]-web_thickened_length[3]-web_thickening_length[3]# D2-腹板变厚起点
node_x[47]=node_x[46]+web_thickening_length[3]/3# D2-腹板变厚
node_x[48]=node_x[47]+web_thickening_length[3]/3# D2-腹板变厚
node_x[49]=node_x[48]+web_thickening_length[3]/3# D2-腹板变厚终点

node_x[59]=node_x[55]+web_thickened_length[4]# D2+腹板变厚起点
node_x[60]=node_x[59]+web_thickening_length[4]/3# D2+腹板变厚
node_x[61]=node_x[60]+web_thickening_length[4]/3# D2+腹板变厚
node_x[62]=node_x[61]+web_thickening_length[4]/3# D2+腹板变厚终点

node_x[69]=node_x[79]-web_thickened_length[5]-web_thickening_length[5]# D3-腹板变厚起点
node_x[70]=node_x[69]+web_thickening_length[5]/3# D3-腹板变厚
node_x[71]=node_x[70]+web_thickening_length[5]/3# D3-腹板变厚
node_x[72]=node_x[71]+web_thickening_length[5]/3# D3-腹板变厚终点

node_x[4]=node_x[3]+(node_x[9]-node_x[3])/6*1# D0+腹板加厚段（去除顶底板变厚）6等分
node_x[5]=node_x[3]+(node_x[9]-node_x[3])/6*2
node_x[6]=node_x[3]+(node_x[9]-node_x[3])/6*3
node_x[7]=node_x[3]+(node_x[9]-node_x[3])/6*4
node_x[8]=node_x[3]+(node_x[9]-node_x[3])/6*5

node_x[13]=node_x[12]+(node_x[19]-node_x[12])/7*1# D0~D1腹板跨中段7等分
node_x[14]=node_x[12]+(node_x[19]-node_x[12])/7*2
node_x[15]=node_x[12]+(node_x[19]-node_x[12])/7*3
node_x[16]=node_x[12]+(node_x[19]-node_x[12])/7*4
node_x[17]=node_x[12]+(node_x[19]-node_x[12])/7*5
node_x[18]=node_x[12]+(node_x[19]-node_x[12])/7*6

node_x[23]=node_x[22]+(node_x[25]-node_x[22])/3*1# D1-腹板加厚段（去除顶底板变厚）3等分
node_x[24]=node_x[22]+(node_x[25]-node_x[22])/3*2
node_x[30]=node_x[29]+(node_x[32]-node_x[29])/3*1# D1+腹板加厚段（去除顶底板变厚）3等分
node_x[31]=node_x[29]+(node_x[32]-node_x[29])/3*2

node_x[36]=node_x[35]+(node_x[46]-node_x[35])/11*1# D1~D2腹板跨中段11等分
node_x[37]=node_x[35]+(node_x[46]-node_x[35])/11*2
node_x[38]=node_x[35]+(node_x[46]-node_x[35])/11*3
node_x[39]=node_x[35]+(node_x[46]-node_x[35])/11*4
node_x[40]=node_x[35]+(node_x[46]-node_x[35])/11*5
node_x[41]=node_x[35]+(node_x[46]-node_x[35])/11*6
node_x[42]=node_x[35]+(node_x[46]-node_x[35])/11*7
node_x[43]=node_x[35]+(node_x[46]-node_x[35])/11*8
node_x[44]=node_x[35]+(node_x[46]-node_x[35])/11*9
node_x[45]=node_x[35]+(node_x[46]-node_x[35])/11*10

node_x[50]=node_x[49]+(node_x[52]-node_x[49])/3*1# D2-腹板加厚段（去除顶底板变厚）3等分
node_x[51]=node_x[49]+(node_x[52]-node_x[49])/3*2
node_x[57]=node_x[56]+(node_x[59]-node_x[56])/3*1# D2+腹板加厚段（去除顶底板变厚）3等分
node_x[58]=node_x[56]+(node_x[59]-node_x[56])/3*2

node_x[63]=node_x[62]+(node_x[69]-node_x[62])/7*1# D2~D3腹板跨中段7等分
node_x[64]=node_x[62]+(node_x[69]-node_x[62])/7*2
node_x[65]=node_x[62]+(node_x[69]-node_x[62])/7*3
node_x[66]=node_x[62]+(node_x[69]-node_x[62])/7*4
node_x[67]=node_x[62]+(node_x[69]-node_x[62])/7*5
node_x[68]=node_x[62]+(node_x[69]-node_x[62])/7*6

node_x[73]=node_x[72]+(node_x[78]-node_x[72])/6*1# D3-腹板加厚段（去除顶底板变厚）6等分
node_x[74]=node_x[72]+(node_x[78]-node_x[72])/6*2
node_x[75]=node_x[72]+(node_x[78]-node_x[72])/6*3
node_x[76]=node_x[72]+(node_x[78]-node_x[72])/6*4
node_x[77]=node_x[72]+(node_x[78]-node_x[72])/6*5
