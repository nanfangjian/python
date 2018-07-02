#!/usr/bin/python
#coding=utf-8
'''Monitoring host status  moduleA

练习：
	1.编写一个A模块实现监控cpu的使用情况、内存的使用、磁盘的使用情况（/分区和/boot分区）
		例如：一旦内存的使用率超过6提醒，输出警告（自己定义）0%给予
			一旦内存的使用率超过80%给予提醒，输出“内存不足”
			cpu的使用率超过80%给予提醒，输出文字（自己定义）
			显示输出具体的使用率，可以告诉用户
'''
import  os,commands
CPU_IDLE=80
MEM_PERCENT=80
def cpu_info():
    cpu_idle=commands.getoutput("top -n 1 |awk -F ',' '/^%Cpu/{print $4}'|sed -r 's/\x1B[\[|\(]([0-9]{1,2}(;[0-9]{1,2})?)?[m|K|B]//g'|cut -d 'i' -f 1")
    cpu_idle=float(cpu_idle)
    if cpu_idle<CPU_IDLE:
        print('cpu负载过高(%d)!!剩余%s'%(CPU_IDLE,cpu_idle))
    else:
        print('cpu负载正常(%d),剩余%s'%(CPU_IDLE,cpu_idle))
def mem_info():
	mem_percent=commands.getoutput("free -h | grep '^Mem' | awk '{print $7/$2*100}'")
	mem_percent=float(mem_percent)
	if mem_percent<MEM_PERCENT:
		print('内存过低(%d)!!剩余%s'%(MEM_PERCENT,mem_percent))
	else:
		print('内存正常(%d)!!剩余%s'%(MEM_PERCENT,mem_percent))
