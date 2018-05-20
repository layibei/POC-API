# !/usr/bin/python3



def login(users_ku):
    lock_list = []  # 锁定用户库，3次登录失败进入的小黑屋

    median = []  # 登录失败的录入中间列表，如果用count数出3次，进入锁定

    while True:

        name = input('输入你的用户名：')

        psw = input('请输入你的密码：')

        if name in lock_list:  # 判断用户是否进入小黑屋

            print('此账号锁定，不能再用此账号登陆')

            continue

        if [name, psw] in users_ku:  # 判断用户输入的合法性

            print('登录成功')

            break

        else:

            median.append(name)  # 用户名录入

            print('账号或者密码输入错误,请重新输入')

        if median.count(name) == 3:  # 同用户3次登录失败进入的小黑屋

            lock_list.append(name)  # 进入小黑屋


if __name__ == '__main__':
    # 用户验证密码库

    users_ku = [['name1', 'psw1'], ['name2', 'psw2']]

    login(users_ku)