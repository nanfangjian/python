#!/usr/bin/python
#coding=utf-8
import os,time
files=raw_input("请输入要备份的文件:")
target_dir="/backup/%s"%(time.strftime('%Y%m%d'))
tar_backup_name="%s/%s.tar.gz"%(target_dir,time.strftime('%H%M%S'))
cmd_backup="tar -czf  %s %s &>/dev/null"%(tar_backup_name,files)
#判断路径是否存在
flag=1
for file in files.split(' '):
    if os.path.exists(file):
        pass
    else:
        print('%s %s 文件不存在,未备份成功'%(time.ctime(),file))
#判断根备份目录是否存在
if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        if os.system(cmd_backup)==0:
            print('备份成功')
            print('%s'%files)
        else:
            print('备份失败')
            flag=0
else:
        if os.system(cmd_backup)==0:
            print('备份成功')
        else:
            print('备份失败')
            flag=0
#判断是否备份部分文件
if os.path.exists(tar_backup_name) & flag==0:
        print('%s 已经创建,未全部备份成功.'%tar_backup_name)