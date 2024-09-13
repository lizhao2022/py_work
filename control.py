from tkinter import filedialog 
import tkinter as tk
import os
import json
import rapid_modeling
class Controller:
	# 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
	ui: object
	def __init__(self):
		pass
	def init(self, ui):
		"""
		得到UI实例，对组件进行初始化配置
		"""
		self.ui = ui
		# TODO 组件初始化 赋值操作		
	def f_open(self,evt):
		file_path=filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json Files", "*.json"), ("All Files", "*.*")])
		if file_path:
			directory=os.path.dirname(file_path)
			filename=os.path.basename(file_path)
			with open(filename, 'r') as f_obj:
				ui_tem=json.load(f_obj)
			"""
			清空所有窗口
			"""
			self.ui.tk_input_B1.delete(0,tk.END)
			self.ui.tk_input_B2.delete(0,tk.END)
			self.ui.tk_input_B3.delete(0,tk.END)
			self.ui.tk_input_B4.delete(0,tk.END)
			self.ui.tk_input_B5.delete(0,tk.END)
			self.ui.tk_input_B6.delete(0,tk.END)
			self.ui.tk_input_B7.delete(0,tk.END)
			self.ui.tk_input_B8.delete(0,tk.END)
			self.ui.tk_input_B9.delete(0,tk.END)
			self.ui.tk_input_B10.delete(0,tk.END)
			self.ui.tk_input_B11.delete(0,tk.END)
			self.ui.tk_input_B12.delete(0,tk.END)
			self.ui.tk_input_B13.delete(0,tk.END)
			self.ui.tk_input_B14.delete(0,tk.END)
			self.ui.tk_input_BW1.delete(0,tk.END)
			self.ui.tk_input_BW2.delete(0,tk.END)
			self.ui.tk_input_BW3.delete(0,tk.END)
			self.ui.tk_input_L1.delete(0,tk.END)
			self.ui.tk_input_L2.delete(0,tk.END)
			self.ui.tk_input_L3.delete(0,tk.END)
			self.ui.tk_input_C1.delete(0,tk.END)
			self.ui.tk_input_C2.delete(0,tk.END)
			self.ui.tk_input_C3.delete(0,tk.END)
			self.ui.tk_input_C4.delete(0,tk.END)
			self.ui.tk_input_Z1.delete(0,tk.END)
			self.ui.tk_input_Z2.delete(0,tk.END)
			self.ui.tk_input_E1.delete(0,tk.END)
			self.ui.tk_input_E2.delete(0,tk.END)
			self.ui.tk_input_W1.delete(0,tk.END)
			self.ui.tk_input_W2.delete(0,tk.END)
			self.ui.tk_input_W3.delete(0,tk.END)
			self.ui.tk_input_W4.delete(0,tk.END)
			self.ui.tk_input_W5.delete(0,tk.END)
			self.ui.tk_input_W6.delete(0,tk.END)
			self.ui.tk_input_WT1.delete(0,tk.END)
			self.ui.tk_input_WT2.delete(0,tk.END)
			self.ui.tk_input_WT3.delete(0,tk.END)
			self.ui.tk_input_WT4.delete(0,tk.END)
			self.ui.tk_input_WT5.delete(0,tk.END)
			self.ui.tk_input_WT6.delete(0,tk.END)
			self.ui.tk_input_P1.delete(0,tk.END)
			self.ui.tk_input_N1.delete(0,tk.END)
			self.ui.tk_input_H1.delete(0,tk.END)
			"""
			将模板文件的数据显示在窗口中
			"""
			self.ui.tk_input_B1.insert(0,ui_tem["bridge_width"][0])
			self.ui.tk_input_B2.insert(0,ui_tem["bridge_width"][1])
			self.ui.tk_input_B3.insert(0,ui_tem["bridge_width"][2])
			self.ui.tk_input_B4.insert(0,ui_tem["bridge_width"][3])
			self.ui.tk_input_B5.insert(0,ui_tem["bridge_width"][4])
			self.ui.tk_input_B6.insert(0,ui_tem["bridge_width"][5])
			self.ui.tk_input_B7.insert(0,ui_tem["bridge_width"][6])
			self.ui.tk_input_B8.insert(0,ui_tem["bridge_width"][7])
			self.ui.tk_input_B9.insert(0,ui_tem["bridge_width"][8])
			self.ui.tk_input_B10.insert(0,ui_tem["bridge_width"][9])
			self.ui.tk_input_B11.insert(0,ui_tem["bridge_width"][10])
			self.ui.tk_input_B12.insert(0,ui_tem["bridge_width"][11])
			self.ui.tk_input_B13.insert(0,ui_tem["bridge_width"][12])
			self.ui.tk_input_B14.insert(0,ui_tem["bridge_width"][13])
			self.ui.tk_input_BW1.insert(0,ui_tem["bumperwall_width"][0])
			self.ui.tk_input_BW2.insert(0,ui_tem["bumperwall_width"][1])
			self.ui.tk_input_BW3.insert(0,ui_tem["bumperwall_width"][2])
			self.ui.tk_input_L1.insert(0,ui_tem["span"][0])
			self.ui.tk_input_L2.insert(0,ui_tem["span"][1])
			self.ui.tk_input_L3.insert(0,ui_tem["span"][2])
			self.ui.tk_input_C1.insert(0,ui_tem["crossbeam"][0])
			self.ui.tk_input_C2.insert(0,ui_tem["crossbeam"][1])
			self.ui.tk_input_C3.insert(0,ui_tem["crossbeam"][2])
			self.ui.tk_input_C4.insert(0,ui_tem["crossbeam"][3])
			self.ui.tk_input_Z1.insert(0,ui_tem["pedestal_position"][0])
			self.ui.tk_input_Z2.insert(0,ui_tem["pedestal_position"][1])
			self.ui.tk_input_E1.insert(0,ui_tem["end_seams"][0])
			self.ui.tk_input_E2.insert(0,ui_tem["end_seams"][1])
			self.ui.tk_input_W1.insert(0,ui_tem["web_thickened_length"][0])
			self.ui.tk_input_W2.insert(0,ui_tem["web_thickened_length"][1])
			self.ui.tk_input_W3.insert(0,ui_tem["web_thickened_length"][2])
			self.ui.tk_input_W4.insert(0,ui_tem["web_thickened_length"][3])
			self.ui.tk_input_W5.insert(0,ui_tem["web_thickened_length"][4])
			self.ui.tk_input_W6.insert(0,ui_tem["web_thickened_length"][5])
			self.ui.tk_input_WT1.insert(0,ui_tem["web_thickening_length"][0])
			self.ui.tk_input_WT2.insert(0,ui_tem["web_thickening_length"][1])
			self.ui.tk_input_WT3.insert(0,ui_tem["web_thickening_length"][2])
			self.ui.tk_input_WT4.insert(0,ui_tem["web_thickening_length"][3])
			self.ui.tk_input_WT5.insert(0,ui_tem["web_thickening_length"][4])
			self.ui.tk_input_WT6.insert(0,ui_tem["web_thickening_length"][5])
			self.ui.tk_input_P1.insert(0,ui_tem["plate_thickening_length"][0])
			self.ui.tk_input_N1.insert(0,ui_tem["web_quantity"])
			self.ui.tk_input_H1.insert(0,ui_tem["beam_height"])
	def f_save(self,evt):
		"""
		读取窗口中的数据，赋值给对应的变量
		"""
		L=[self.ui.tk_input_L1.get(), self.ui.tk_input_L2.get(), self.ui.tk_input_L3.get()]
		H=self.ui.tk_input_H1.get()
		C=[self.ui.tk_input_C1.get(), self.ui.tk_input_C2.get(), self.ui.tk_input_C3.get(), self.ui.tk_input_C4.get()]
		PP=[self.ui.tk_input_Z1.get(), self.ui.tk_input_Z2.get()]
		ES=[self.ui.tk_input_E1.get(), self.ui.tk_input_E2.get()]
		WTL=[self.ui.tk_input_W1.get(), self.ui.tk_input_W2.get(), self.ui.tk_input_W3.get(), self.ui.tk_input_W4.get(), self.ui.tk_input_W5.get(), self.ui.tk_input_W6.get()]
		WTTL=[self.ui.tk_input_WT1.get(), self.ui.tk_input_WT2.get(), self.ui.tk_input_WT3.get(), self.ui.tk_input_WT4.get(), self.ui.tk_input_WT5.get(), self.ui.tk_input_WT6.get()]
		PTL=[self.ui.tk_input_P1.get()]*6
		WN=self.ui.tk_input_N1.get()
		BPW=[self.ui.tk_input_BW1.get(), self.ui.tk_input_BW2.get(), self.ui.tk_input_BW3.get()]
		BW=[self.ui.tk_input_B1.get(), self.ui.tk_input_B2.get(), self.ui.tk_input_B3.get(), self.ui.tk_input_B4.get(), self.ui.tk_input_B5.get(), self.ui.tk_input_B6.get(), self.ui.tk_input_B7.get(), self.ui.tk_input_B8.get(), self.ui.tk_input_B9.get(), self.ui.tk_input_B10.get(), self.ui.tk_input_B11.get(), self.ui.tk_input_B12.get(), self.ui.tk_input_B13.get(), self.ui.tk_input_B14.get()]
		"""
		整理数据为json格式，将文本转换为数据
		"""
		tem_dic= {
			"span": [ float(x) for x in L ], 
			"beam_height": float(H), 
			"crossbeam": [ float(x) for x in C ], 
			"pedestal_position": [ float(x) for x in PP ], 
			"end_seams": [ float(x) for x in ES ], 
			"web_thickened_length": [ float(x) for x in WTL ], 
			"web_thickening_length": [ float(x) for x in WTTL ], 
			"plate_thickening_length": [ float(x) for x in PTL ], 
			"web_quantity": int(WN), 
			"bumperwall_width": [ float(x) for x in BPW ], 
			"bridge_width": [ float(x) for x in BW ]
		}
		file_path=filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json Files", "*.json"), ("All Files", "*.*")])
		if file_path:
			directory=os.path.dirname(file_path)
			filename=os.path.basename(file_path)
			with open(filename, 'w') as f_obj:
				json.dump(tem_dic, f_obj)
				
	def m_generate(self,evt):
		"""
		读取窗口中的数据，赋值给对应的变量
		"""
		L=[self.ui.tk_input_L1.get(), self.ui.tk_input_L2.get(), self.ui.tk_input_L3.get()]
		H=self.ui.tk_input_H1.get()
		C=[self.ui.tk_input_C1.get(), self.ui.tk_input_C2.get(), self.ui.tk_input_C3.get(), self.ui.tk_input_C4.get()]
		PP=[self.ui.tk_input_Z1.get(), self.ui.tk_input_Z2.get()]
		ES=[self.ui.tk_input_E1.get(), self.ui.tk_input_E2.get()]
		WTL=[self.ui.tk_input_W1.get(), self.ui.tk_input_W2.get(), self.ui.tk_input_W3.get(), self.ui.tk_input_W4.get(), self.ui.tk_input_W5.get(), self.ui.tk_input_W6.get()]
		WTTL=[self.ui.tk_input_WT1.get(), self.ui.tk_input_WT2.get(), self.ui.tk_input_WT3.get(), self.ui.tk_input_WT4.get(), self.ui.tk_input_WT5.get(), self.ui.tk_input_WT6.get()]
		PTL=[self.ui.tk_input_P1.get()]*6
		WN=self.ui.tk_input_N1.get()
		BPW=[self.ui.tk_input_BW1.get(), self.ui.tk_input_BW2.get(), self.ui.tk_input_BW3.get()]
		BW=[self.ui.tk_input_B1.get(), self.ui.tk_input_B2.get(), self.ui.tk_input_B3.get(), self.ui.tk_input_B4.get(), self.ui.tk_input_B5.get(), self.ui.tk_input_B6.get(), self.ui.tk_input_B7.get(), self.ui.tk_input_B8.get(), self.ui.tk_input_B9.get(), self.ui.tk_input_B10.get(), self.ui.tk_input_B11.get(), self.ui.tk_input_B12.get(), self.ui.tk_input_B13.get(), self.ui.tk_input_B14.get()]
		"""
		整理数据为json格式，将文本转换为数据
		"""
		tem_dic= {
			"span": [ float(x) for x in L ], 
			"beam_height": float(H), 
			"crossbeam": [ float(x) for x in C ], 
			"pedestal_position": [ float(x) for x in PP ], 
			"end_seams": [ float(x) for x in ES ], 
			"web_thickened_length": [ float(x) for x in WTL ], 
			"web_thickening_length": [ float(x) for x in WTTL ], 
			"plate_thickening_length": [ float(x) for x in PTL ], 
			"web_quantity": int(WN), 
			"bumperwall_width": [ float(x) for x in BPW ], 
			"bridge_width": [ float(x) for x in BW ]
		}
		rapid_modeling
		
		
		file_path=filedialog.asksaveasfilename(defaultextension=".mct", filetypes=[("Midas Files", "*.mct"), ("All Files", "*.*")])
		if file_path:
			directory=os.path.dirname(file_path)
			file_name=os.path.basename(file_path)
			with open(file_name, 'w') as file_object:
				file_object.writelines(data_template)
	
