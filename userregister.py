#!/usr/bin/python
#coding=utf-8
'''userregister

userregister python script
'''
user_list=[]
select_choice=""
def show_menu():
    global  select_choice
    print('1.请输入内容')
    print('2.请选择用户')
    print('3显示出所有用户')
    print('4.exit')
    select_choice=raw_input('请选择:')
def menu_one():
    global user_list
    user_id=raw_input('请输入 id')
    user_name=raw_input('请输入 name')
    if len(user_name)==0: #注意什么都不输入是len()==0
        user_name = "dd"
    user_phone_number=raw_input('请输入 phone_number')
    user_address=raw_input('请输入 address')
    user_info={'user_id':user_id,'user_name':user_name,'user_phone_number':user_phone_number,'user_address':user_address}
    user_list.append(user_info)
def input_choice(select_choice):
    if select_choice.isdigit():
        select_choice = int(select_choice)
        if select_choice == 1:
            menu_one()
        if select_choice == 2:
            pass
        if select_choice == 3:
            print user_list
        if select_choice == 4:
            exit()
    else:
        print('输入错误,请输入数字选项')
def main():
    while True:
        show_menu()
        input_choice(select_choice)

main()
print __doc__


