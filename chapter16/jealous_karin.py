# -*- coding:utf-8 -*-

# __filename__ = " jealous_karin.py.py"
# __author__ = "薯条社区"
# __date__ = "2019-05-26"

import random  # 导入random模块, 用来获取随机数
import time  # 导入time模块, 来进行倒计时的模拟


#  定义letters变量，用来保存神月卡琳写给春丽的一封信
# 春丽只学过一天的html
# 她只知道在a标签的mailto中可以写邮箱地址

letters = '''
给庶民春丽的一封信:

我的神月流格斗技无懈可击。

我是神月大家族的karin,  你上次与维加的街霸挑战赛，一切费用由我们神月集团进行赞助，
我们已经看到了你的不凡实力。维加在饮弹之前，向我们透露了你父亲的一个不为人知的秘密，
这个秘密事关你父亲的荣誉！
来吧，在街霸擂台挑战赛中将我打败！

破解系统中的密码，找到我信件中的邮箱地址，你才有资格在擂台上对本小姐进行挑战。
你只有十次的机会破解密码，如果失败，我会将你父亲的秘密公告天下。

<address>
Written by <a href="mailto:street_fighter@karin.com">karin</a>.<br> 
Visit us at:<br>
Box 564, california<br>
USA
</address>
'''

# 定义reply变量，用来保存春丽给神月的回信
reply = '''
我已破解了系统的密码:{0}, 这是你信中的邮箱地址:{1}。
如你所说，我是一个庶民，但高贵的你也只有靠口舌才能彰显你的高贵。
神月贱人，我不会让已安睡的父亲再次承受不白之冤，
为了父亲的荣誉，我会在街霸挑战赛中将你打败！
'''

def main():
    '''
    :return:void
    '''

    # 使用print函数来打印letters的内容，来模拟打开信件的动作
    print(letters)
    time.sleep(2)

    # 使用random模块的randint函数来获取从0到100之间的一个随机数，来作为系统密码
    the_correct_code = random.randint(0, 5)
    # 使用time模块中sleep函数来模拟倒计时效果
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("-*-###   你好, 庶民春丽，我们赐给你十次机会来破解密码!   ###-*-")

    # 定义count变量来保存破解密码的次数
    count = 0

    # 定义code变量, 用来保存春丽输入的数字密码

    while True:
        code = input("* 请输入你的数字密码:__\b\b")
        '''
             读者在输入时必须输入有效的数字，否则会抛出异常
            对于异常的处理，笔者会在后续的教程中进行介绍
        '''

        code = int(code)
        if code == the_correct_code:
            print("春丽，你成功的破解了数字密码！")
            break  # 执行break退出循环
        elif code > the_correct_code:
            print("春丽，你输入的数字密码太大了")
        else:
            print("春丽，你输入的数字密码太小了")
        count += 1  # 每破解一次密码，count的值递增1
        if count == 10:
            break   # 破解10次以后，执行break退出循环


    if code == the_correct_code:

        mailto_index = letters.find('mailto:')  # 计算字符串 mailto: 在letters中的起始索引
        quote_index = letters.find('"', mailto_index) # 计算信件中邮箱地址后面的" 在letters中的位置索引
        karin_mail = letters[mailto_index+7:quote_index]  # 对letters变量使用切片操作,来截取信件中的邮箱地址

        # 使用format来对春丽回信的内容进行格式化
        print(reply.format(code, karin_mail))
    else:
        print("可怜的春丽，我们已经将秘密公告天下，你的父亲将受世人唾弃！")

    time.sleep(3)

if __name__ == "__main__":
    main()
