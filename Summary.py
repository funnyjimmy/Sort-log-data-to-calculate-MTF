# -*- coding: utf-8 -*-
'''
	Writer: Yi Qin
	Create date: 2017/8/7
	The purpose is to dig the SFR MTF data from MT result
'''
from Tkinter import *
from tkFileDialog import *
import os
import csv

filetype = ['.txt'] #指定遍历的文件后缀名

#### 定义遍历函数，并将特定后缀文件地址保存到列表中

def walk_Directory(dir_name):
	m = []
	for i in os.walk(dir_name):
		if len(i[-1]) != 0:
			if os.path.splitext(i[-1][-1])[-1] in filetype:
				m.append((i[0]+"/"+i[-1][-1]).replace("\\","/"))
	return m

####定义读取数据函数###
def data_read(*file_name):
	Temp_ID = ''
	Dioper_ID = ''
	dataset = []
	for doc in file_name:
		Temp_ID = doc.split("/")[-4]
		Dioper_ID = doc.split("/")[-3] #根据文件夹名称创建样品ID
		with open(doc,'r') as f:
			sample_info = []
			sample_info.append(Temp_ID)
			sample_info.append(Dioper_ID)
			for dataline in f.readlines():
				if (dataline.find("Data_P SFR_ROI") != -1) and (dataline.find("MTFValue1") != -1): #判断是否是MTF数据行
					dataline = dataline.strip('\n').split(" ")
					sample_info.append(float(dataline[-1]))
			center_MTF = sum(sample_info[30:34])/4
			right_MTF = sum(sample_info[38:42])/4
			top_MTF = sum(sample_info[10:14])/4
			left_MTF = sum(sample_info[22:26])/4
			down_MTF = sum(sample_info[50:54])/4
			sample_info.append(center_MTF)
			sample_info.append(right_MTF)
			sample_info.append(top_MTF)
			sample_info.append(left_MTF)
			sample_info.append(down_MTF)
		dataset.append(sample_info)
	return dataset
					
####定义写入数据函数###

def data_save(dataset,filename):
	with open(filename,'wb') as csvfile:
		spamwriter = csv.writer(csvfile, dialect = 'excel')
		first_row = ['Sample_ID']
		first_row.append('Sub_ID') #写入样品ID号码
		for i in range(15):
			for j in range(4):
				first_row.append(str(i) +'_'+ str(j)) #生成ROI序列首行
		for k in ["Center","Right","Top","Left","Down"]:
			first_row.append(k)
		spamwriter.writerow(first_row)
		for dataline in dataset:
			spamwriter.writerow(dataline)

######


if __name__ == '__main__':

	#打开对话框
	root = Tk()
	dirname = askdirectory() #选择目录信息

	filelist = walk_Directory(dirname)
	SFR = data_read(*filelist)

	savename = asksaveasfilename(initialdir = "D:/",title = "Save file as...",defaultextension = "csv") 
	data_save(SFR,savename)


	root.mainloop() 



