#/usr/bin/python
#coding=utf-8
#author:nan 2018/7/7
import os
import  time
import commands
#首先进行备份
def back_up_ip():
    backup_dir_name="backup%s"%(time.strftime('%Y%m%d-%H:%M:%S'))
    cmd='mkdir  %s && cp /etc/sysconfig/network-scripts/ifcfg-en* %s'%(backup_dir_name,backup_dir_name)
    if os.system(cmd)==0:
        print('执行备份成功')
    else:
        print('执行失败')
        return 'gg'
#找到最后备份的文件夹,进行还原
def back_up_file():
    cmd='cp -f $(find . -type d -name back\* | sort -r | tail -1)/* /etc/sysconfig/network-scripts/ <<EOF\ny\nEOF\n'
    if os.system(cmd)==0:
        print('恢复备份成功')
    else:
        print('恢复备份失败')
        return 'gg'
#定义更改配置文件信息
def change_ifcfg():
    BOOTPROTO=raw_input('请输入:BOOTPROTO=')
    DEVICE=raw_input('请输入:DEVICE=')
    ONBOOT=raw_input('请输入:ONBOOT=')
    IPADDR=raw_input('请输入:IPADDR=')
    NETMASK=raw_input('请输入:NETMASK=')
    ifcfg_str="TYPE=Ethernet\nNAME=%s\nBOOTPROTO=%s\nDEVICE=%s\nONBOOT=%s\nIPADDR=%s\nNETMASK=%s\n"%(DEVICE,BOOTPROTO,DEVICE,ONBOOT,IPADDR,NETMASK)
    return  ifcfg_str
def menu():
    print('菜单:')
    print('1.修改ip')
    print('2.恢复ip')
    print('3.备份ip')
    print('4.退出')
def select_option1():
    while True:
        ens=raw_input('请输入请选择网卡:\n%s\n'%commands.getoutput("ifconfig -a | grep ens |cut -d ':' -f1"))
        if len(ens)!=0 :
            ifcfg_str=change_ifcfg()#注意:ens输入为空时会出现Failed to start LSB: Bring up/down networking
            break
             #该错误貌似也会出现在NetManger开启的时候
    ens_path='/etc/sysconfig/network-scripts/ifcfg-%s'%ens
    f=open(ens_path,'w+')
    f.write(ifcfg_str)
    f.close()
    if os.system('service network restart')==0:
        print('修改成功!')
    else:
        back_up_file()
        os.system('service network restart')
def select_option():
    option=raw_input('请输入:')
    if option.isdigit():
        option=int(option)
        if option==1:
            select_option1()
        elif option==2:
            back_up_file()
            os.system('service network restart')
        elif option==3:
            back_up_ip()
        elif option==4:
            exit()
    else:
        print('请输入正确的选项:')
def main():
    menu()
    select_option()
main()


