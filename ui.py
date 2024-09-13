import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
class WinGUI(Window):
	def __init__(self):
		super().__init__(themename="cosmo", hdpi=False)
		self.__win()
		self.tk_canvas_section_display = self.__tk_canvas_section_display(self)
		self.tk_canvas_elevation_display = self.__tk_canvas_elevation_display(self)
		self.tk_input_B1 = self.__tk_input_B1(self)
		self.tk_input_B2 = self.__tk_input_B2(self)
		self.tk_input_B3 = self.__tk_input_B3(self)
		self.tk_input_B4 = self.__tk_input_B4(self)
		self.tk_input_B5 = self.__tk_input_B5(self)
		self.tk_input_B6 = self.__tk_input_B6(self)
		self.tk_input_B7 = self.__tk_input_B7(self)
		self.tk_input_B8 = self.__tk_input_B8(self)
		self.tk_input_B9 = self.__tk_input_B9(self)
		self.tk_input_B10 = self.__tk_input_B10(self)
		self.tk_input_B11 = self.__tk_input_B11(self)
		self.tk_input_B12 = self.__tk_input_B12(self)
		self.tk_input_B13 = self.__tk_input_B13(self)
		self.tk_input_B14 = self.__tk_input_B14(self)
		self.tk_input_BW1 = self.__tk_input_BW1(self)
		self.tk_input_BW2 = self.__tk_input_BW2(self)
		self.tk_input_BW3 = self.__tk_input_BW3(self)
		self.tk_input_L1 = self.__tk_input_L1(self)
		self.tk_input_L2 = self.__tk_input_L2(self)
		self.tk_input_L3 = self.__tk_input_L3(self)
		self.tk_input_C1 = self.__tk_input_C1(self)
		self.tk_input_C2 = self.__tk_input_C2(self)
		self.tk_input_C3 = self.__tk_input_C3(self)
		self.tk_input_C4 = self.__tk_input_C4(self)
		self.tk_input_Z1 = self.__tk_input_Z1(self)
		self.tk_input_Z2 = self.__tk_input_Z2(self)
		self.tk_input_E1 = self.__tk_input_E1(self)
		self.tk_input_E2 = self.__tk_input_E2(self)
		self.tk_input_W1 = self.__tk_input_W1(self)
		self.tk_input_W2 = self.__tk_input_W2(self)
		self.tk_input_W3 = self.__tk_input_W3(self)
		self.tk_input_W4 = self.__tk_input_W4(self)
		self.tk_input_W5 = self.__tk_input_W5(self)
		self.tk_input_W6 = self.__tk_input_W6(self)
		self.tk_input_WT1 = self.__tk_input_WT1(self)
		self.tk_input_WT2 = self.__tk_input_WT2(self)
		self.tk_input_WT3 = self.__tk_input_WT3(self)
		self.tk_input_WT4 = self.__tk_input_WT4(self)
		self.tk_input_WT5 = self.__tk_input_WT5(self)
		self.tk_input_WT6 = self.__tk_input_WT6(self)
		self.tk_input_P1 = self.__tk_input_P1(self)
		self.tk_input_N1 = self.__tk_input_N1(self)
		self.tk_input_H1 = self.__tk_input_H1(self)
	
		self.tk_label_SB = self.__tk_label_SB(self)
		self.tk_label_SBW = self.__tk_label_SBW(self)
		self.tk_label_SL = self.__tk_label_SL(self)
		self.tk_label_SC = self.__tk_label_SC(self)
		self.tk_label_SZ = self.__tk_label_SZ(self)
		self.tk_label_SE = self.__tk_label_SE(self)
		self.tk_label_SW = self.__tk_label_SW(self)
		self.tk_label_SWL = self.__tk_label_SWL(self)
		self.tk_label_SP = self.__tk_label_SP(self)
		self.tk_label_SWN = self.__tk_label_SWN(self)
		self.tk_label_SH = self.__tk_label_SH(self)
		
		self.tk_label_S = self.__tk_label_S(self)
		self.tk_label_S1 = self.__tk_label_S1(self)
		self.tk_label_S2 = self.__tk_label_S2(self)
		self.tk_label_S3 = self.__tk_label_S3(self)
		self.tk_label_S4 = self.__tk_label_S4(self)
		self.tk_label_S5 = self.__tk_label_S5(self)
		self.tk_label_S6 = self.__tk_label_S6(self)
		self.tk_label_S7 = self.__tk_label_S7(self)
		self.tk_label_S8 = self.__tk_label_S8(self)
		self.tk_label_S9 = self.__tk_label_S9(self)
		self.tk_label_S10 = self.__tk_label_S10(self)
		self.tk_label_S11 = self.__tk_label_S11(self)
		self.tk_label_S12 = self.__tk_label_S12(self)
		self.tk_label_S13 = self.__tk_label_S13(self)
		self.tk_label_S14 = self.__tk_label_S14(self)
		
		self.tk_button_f_open = self.__tk_button_f_open(self)
		self.tk_button_m_generate = self.__tk_button_m_generate(self)
		self.tk_button_f_save = self.__tk_button_f_save(self)
		self.tk_label_elevation_name = self.__tk_label_elevation_name(self)
		self.tk_label_section_name = self.__tk_label_section_name(self)
		
		
	def __win(self):
		self.title("现浇箱梁建模助手")
		# 设置窗口大小、居中
		width = 960
		height = 540
		screenwidth = self.winfo_screenwidth()
		screenheight = self.winfo_screenheight()
		geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		self.geometry(geometry)
		
		self.resizable(width=False, height=False)
		
	def scrollbar_autohide(self,vbar, hbar, widget):
		"""自动隐藏滚动条"""
		def show():
			if vbar: vbar.lift(widget)
			if hbar: hbar.lift(widget)
		def hide():
			if vbar: vbar.lower(widget)
			if hbar: hbar.lower(widget)
		hide()
		widget.bind("<Enter>", lambda e: show())
		if vbar: vbar.bind("<Enter>", lambda e: show())
		if vbar: vbar.bind("<Leave>", lambda e: hide())
		if hbar: hbar.bind("<Enter>", lambda e: show())
		if hbar: hbar.bind("<Leave>", lambda e: hide())
		widget.bind("<Leave>", lambda e: hide())
	
	def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
		widget.configure(yscrollcommand=vbar.set)
		vbar.config(command=widget.yview)
		vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
	def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
		widget.configure(xscrollcommand=hbar.set)
		hbar.config(command=widget.xview)
		hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
	def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
		vbar, hbar = None, None
		if is_vbar:
			vbar = Scrollbar(master)
			self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
		if is_hbar:
			hbar = Scrollbar(master, orient="horizontal")
			self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
		self.scrollbar_autohide(vbar, hbar, widget)
	def new_style(self,widget):
		ctl = widget.cget('style')
		ctl = "".join(random.sample('0123456789',5)) + "." + ctl
		widget.configure(style=ctl)
		return ctl
	def __tk_canvas_section_display(self,parent):
		canvas = Canvas(parent,bg="#aaa")
		canvas.place(x=460, y=145, width=460, height=150)
		return canvas
	def __tk_canvas_elevation_display(self,parent):
		canvas = Canvas(parent,bg="#aaa")
		canvas.place(x=20, y=410, width=900, height=120)
		return canvas
	def __tk_input_L1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=135, width=55, height=25)
		return ipt
	def __tk_label_S1(self,parent):
		label = Label(parent,text="1",anchor="center", bootstyle="default")
		label.place(x=100, y=45, width=55, height=25)
		return label
	def __tk_label_S2(self,parent):
		label = Label(parent,text="2",anchor="center", bootstyle="default")
		label.place(x=160, y=45, width=55, height=25)
		return label
	def __tk_input_L2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=135, width=55, height=25)
		return ipt
	def __tk_label_S3(self,parent):
		label = Label(parent,text="3",anchor="center", bootstyle="default")
		label.place(x=220, y=45, width=55, height=25)
		return label
	def __tk_input_L3(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=220, y=135, width=55, height=25)
		return ipt
	def __tk_label_S4(self,parent):
		label = Label(parent,text="4",anchor="center", bootstyle="default")
		label.place(x=280, y=45, width=55, height=25)
		return label
	def __tk_label_S5(self,parent):
		label = Label(parent,text="5",anchor="center", bootstyle="default")
		label.place(x=340, y=45, width=55, height=25)
		return label
	def __tk_label_S6(self,parent):
		label = Label(parent,text="6",anchor="center", bootstyle="default")
		label.place(x=400, y=45, width=55, height=25)
		return label
	def __tk_label_S(self,parent):
		label = Label(parent,text="序号",anchor="center", bootstyle="default")
		label.place(x=20, y=45, width=40, height=25)
		return label
	def __tk_label_SL(self,parent):
		label = Label(parent,text="跨径",anchor="center", bootstyle="default")
		label.place(x=20, y=135, width=40, height=25)
		return label
	def __tk_label_SC(self,parent):
		label = Label(parent,text="横梁宽",anchor="center", bootstyle="default")
		label.place(x=20, y=165, width=50, height=25)
		return label
	def __tk_input_C1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=165, width=55, height=25)
		return ipt
	def __tk_input_C2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=165, width=55, height=25)
		return ipt
	def __tk_input_C3(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=220, y=165, width=55, height=25)
		return ipt
	def __tk_input_C4(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=280, y=165, width=55, height=25)
		return ipt
	def __tk_label_SE(self,parent):
		label = Label(parent,text="梁端缝",anchor="center", bootstyle="default")
		label.place(x=20, y=225, width=50, height=25)
		return label
	def __tk_input_E1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=225, width=55, height=25)
		return ipt
	def __tk_input_E2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=225, width=55, height=25)
		return ipt
	def __tk_label_SW(self,parent):
		label = Label(parent,text="腹板加厚段",anchor="center", bootstyle="default")
		label.place(x=20, y=255, width=75, height=25)
		return label
	def __tk_input_W1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=255, width=55, height=25)
		return ipt
	def __tk_input_W2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=255, width=55, height=25)
		return ipt
	def __tk_input_W3(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=220, y=255, width=55, height=25)
		return ipt
	def __tk_input_W4(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=280, y=255, width=55, height=25)
		return ipt
	def __tk_input_W5(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=340, y=255, width=55, height=25)
		return ipt
	def __tk_input_W6(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=400, y=255, width=55, height=25)
		return ipt
	def __tk_label_SWL(self,parent):
		label = Label(parent,text="腹板变厚段",anchor="center", bootstyle="default")
		label.place(x=20, y=285, width=75, height=25)
		return label
	def __tk_input_WT6(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=400, y=285, width=55, height=25)
		return ipt
	def __tk_input_WT5(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=340, y=285, width=55, height=25)
		return ipt
	def __tk_input_WT4(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=280, y=285, width=55, height=25)
		return ipt
	def __tk_input_WT3(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=220, y=285, width=55, height=25)
		return ipt
	def __tk_input_WT2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=285, width=55, height=25)
		return ipt
	def __tk_input_WT1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=285, width=55, height=25)
		return ipt
	def __tk_label_SP(self,parent):
		label = Label(parent,text="顶板变厚段",anchor="center", bootstyle="default")
		label.place(x=20, y=315, width=75, height=25)
		return label
	def __tk_input_P1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=315, width=55, height=25)
		return ipt
	def __tk_label_S12(self,parent):
		label = Label(parent,text="12",anchor="center", bootstyle="default")
		label.place(x=760, y=45, width=55, height=25)
		return label
	def __tk_label_S11(self,parent):
		label = Label(parent,text="11",anchor="center", bootstyle="default")
		label.place(x=700, y=45, width=55, height=25)
		return label
	def __tk_label_S10(self,parent):
		label = Label(parent,text="10",anchor="center", bootstyle="default")
		label.place(x=640, y=45, width=55, height=25)
		return label
	def __tk_label_S9(self,parent):
		label = Label(parent,text="9",anchor="center", bootstyle="default")
		label.place(x=580, y=45, width=55, height=25)
		return label
	def __tk_label_S8(self,parent):
		label = Label(parent,text="8",anchor="center", bootstyle="default")
		label.place(x=520, y=45, width=55, height=25)
		return label
	def __tk_label_S7(self,parent):
		label = Label(parent,text="7",anchor="center", bootstyle="default")
		label.place(x=460, y=45, width=55, height=25)
		return label
	def __tk_label_S14(self,parent):
		label = Label(parent,text="14",anchor="center", bootstyle="default")
		label.place(x=880, y=45, width=55, height=25)
		return label
	def __tk_label_S13(self,parent):
		label = Label(parent,text="13",anchor="center", bootstyle="default")
		label.place(x=820, y=45, width=55, height=25)
		return label
	def __tk_label_SB(self,parent):
		label = Label(parent,text="桥宽",anchor="center", bootstyle="default")
		label.place(x=20, y=75, width=40, height=25)
		return label
	def __tk_input_B1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=75, width=55, height=25)
		return ipt
	def __tk_input_B2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=75, width=55, height=25)
		return ipt
	def __tk_input_B3(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=220, y=75, width=55, height=25)
		return ipt
	def __tk_input_B4(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=280, y=75, width=55, height=25)
		return ipt
	def __tk_input_B5(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=340, y=75, width=55, height=25)
		return ipt
	def __tk_input_B6(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=400, y=75, width=55, height=25)
		return ipt
	def __tk_input_B7(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=460, y=75, width=55, height=25)
		return ipt
	def __tk_input_B8(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=520, y=75, width=55, height=25)
		return ipt
	def __tk_input_B9(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=580, y=75, width=55, height=25)
		return ipt
	def __tk_input_B10(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=640, y=75, width=55, height=25)
		return ipt
	def __tk_input_B11(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=700, y=75, width=55, height=25)
		return ipt
	def __tk_input_B12(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=760, y=75, width=55, height=25)
		return ipt
	def __tk_input_B13(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=820, y=75, width=55, height=25)
		return ipt
	def __tk_input_B14(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=880, y=75, width=55, height=25)
		return ipt
	def __tk_label_SWN(self,parent):
		label = Label(parent,text="腹板数",anchor="center", bootstyle="default")
		label.place(x=20, y=345, width=50, height=25)
		return label
	def __tk_input_N1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=345, width=55, height=25)
		return ipt
	def __tk_input_H1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=375, width=55, height=25)
		return ipt
	def __tk_label_SH(self,parent):
		label = Label(parent,text="梁高",anchor="center", bootstyle="default")
		label.place(x=20, y=375, width=40, height=25)
		return label
	def __tk_label_SBW(self,parent):
		label = Label(parent,text="防撞墙宽",anchor="center", bootstyle="default")
		label.place(x=20, y=105, width=65, height=25)
		return label
	def __tk_input_BW1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=105, width=55, height=25)
		return ipt
	def __tk_input_BW2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=105, width=55, height=25)
		return ipt
	def __tk_input_BW3(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=220, y=105, width=55, height=25)
		return ipt
	def __tk_button_f_open(self,parent):
		btn = Button(parent, text="打开模板", takefocus=False,bootstyle="default")
		btn.place(x=20, y=5, width=80, height=30)
		return btn
	def __tk_button_m_generate(self,parent):
		btn = Button(parent, text="生成模型", takefocus=False,bootstyle="success")
		btn.place(x=220, y=5, width=80, height=30)
		return btn
	def __tk_button_f_save(self,parent):
		btn = Button(parent, text="保存文件", takefocus=False,bootstyle="default")
		btn.place(x=120, y=5, width=80, height=30)
		return btn
	def __tk_label_elevation_name(self,parent):
		label = Label(parent,text="立面图",anchor="center", bootstyle="default")
		label.place(x=870, y=380, width=55, height=25)
		return label
	def __tk_label_section_name(self,parent):
		label = Label(parent,text="断面图",anchor="center", bootstyle="default")
		label.place(x=870, y=300, width=55, height=25)
		return label
	def __tk_label_SZ(self,parent):
		label = Label(parent,text="支座梁端距",anchor="center", bootstyle="default")
		label.place(x=20, y=195, width=75, height=25)
		return label
	def __tk_input_Z1(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=100, y=195, width=55, height=25)
		return ipt
	def __tk_input_Z2(self,parent):
		ipt = Entry(parent, bootstyle="default")
		ipt.place(x=160, y=195, width=55, height=25)
		return ipt
class Win(WinGUI):
	def __init__(self, controller):
		self.ctl = controller
		super().__init__()
		self.__event_bind()
		self.__style_config()
		self.ctl.init(self)
	def __event_bind(self):
		self.tk_button_f_open.bind('<Button-1>',self.ctl.f_open)
		self.tk_button_m_generate.bind('<Button-1>',self.ctl.m_generate)
		self.tk_button_f_save.bind('<Button-1>',self.ctl.f_save)
		pass
	def __style_config(self):
		sty = Style()
		sty.configure(self.new_style(self.tk_label_S1),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S2),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S3),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S4),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S5),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S6),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SL),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SC),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SE),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SW),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SWL),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SP),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S12),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S11),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S10),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S9),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S8),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S7),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S14),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_S13),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SB),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SWN),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SH),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SBW),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_button_f_open),font=("微软雅黑",-12))
		sty.configure(self.new_style(self.tk_button_m_generate),font=("微软雅黑",-12))
		sty.configure(self.new_style(self.tk_button_f_save),font=("微软雅黑",-12))
		sty.configure(self.new_style(self.tk_label_elevation_name),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_section_name),font=("微软雅黑",-12,"bold"))
		sty.configure(self.new_style(self.tk_label_SZ),font=("微软雅黑",-12,"bold"))
		pass
if __name__ == "__main__":
	win = WinGUI()
	win.mainloop()
