#!/usr/bin/python
#coding=utf-8
'''Monitoring host status module C
	3.编写一个C模块调用A和B模块,查看内存、磁盘、cpu的使用情况，增加和删除用户
'''
import monitoring_A
import monitoring_B
def select_options():
	print '1.A模块,系统监控'
        print '2.B模块系统管理'
	global option
	option=raw_input('请输入选择')
	if option.isdigit():
		option=int(option)
		if option==1:
			monitoring_A.cpu_info()
			monitoring_A.mem_info()	
		elif option==2:
			monitoring_B.menu_options()
		elif option==3:
			exit()
global option
while True:
	select_options()
