#!/usr/bin/python
#coding=utf-8
'''Monitoring host status module B

	2.编写一个B模块实现增加和删除用户的功能
'''
import os
def user_add(user_add_name,user_add_password):
	if len(user_add_password)==0|user_add_password.isspace():
		user_add_password=1
	user_add_sh='useradd %s && echo %s | passwd --stdin %s'%(user_add_name,user_add_password,user_add_name)
	if os.system(user_add_sh)!=0:
		print("添加失败！！")
	else:
		print("添加成功！！")
def user_del(user_del_name):
	user_del_sh='userdel %s'%user_del_name
	if os.system(user_del_sh)==0:
                print("删除成功！！")
        else:
                print("删除失败！！")
def menu_options():
	option=raw_input('请输入：\n  1.添加\n  2。删除\n')
	if option.isdigit():
		option=int(option)
		if option==1:
			user_add_name=raw_input("请输入用户名")
			user_add_password=raw_input("请输入密码")
			user_add(user_add_name,user_add_password)
		elif option==2:
			user_del_name=raw_input("请输入用户名")
			user_del(user_del_name)
	else:
		print("请输入·数字")

