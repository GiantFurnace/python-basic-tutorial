#-*- coding:utf-8 -*-

# __filename__ = "ko_street_fighter.py"
# __author__ = "薯条社区"
# __date__ = "2019-05-16"

import random  # 导入random模块
import time  # 导入定时器, 本节程序代码使用定时器来实现倒计时效果

'''
下文中的strategies 使用直接定义法来定义一个列表，保存系统随机出的格斗策略
'''

strategies = ["原地蹲防", "失误", "暴血连段", "失误", "伤害修正", "鬼步", "失误", "波升", "回血", "必杀"]
chunli_kungfu = ["气功拳", "旋转踢", "百裂脚", "霸山天升脚"]


def main():
    '''
    :return:void
    '''
    fighter = 100  # 定义整型变量fighter,用来保存街霸的血量
    chunli = 100  # 定义整型变量chunli，用来保存春丽的血量

    # 对战倒计时
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(0.2)
    print("Fight!")


    while True:  # 循环语句，不断重复执行下面的代码
        if fighter <= 0 or chunli <= 0:  # 春丽或boss其中一人血量为0时就退出战斗
            break

        # 执行input函数获得键盘的输入内容
        kungfu = input("\n#--输入以下数字指令来挑战街霸维加:\n<0>气功拳 <1>旋转踢 <2>百裂脚 <3>霸山天升脚\n")
        kungfu = int(kungfu)  # 对输入的字符串类型转换为整型，读者在输入时必须输入有效的数字，否则会抛出异常
                                        # 对于异常的处理，笔者会在后续的教程中进行介绍

     
        is_valid_attack = True  # 定义布尔类型变量is_valid_attack 用来判断春丽是否采取了有效个攻击
        if kungfu >= 0 and kungfu <= 4:
            print("你对街霸使出了{}".format(chunli_kungfu[kungfu]))
        else:
            is_valid_attack = False  # 输入的指令错误，攻击无效
            print("春丽，这是在战斗，请输入正确的战斗指令！")


        strategy = random.choice(strategies)  # 使用random模块中的choice函数，来随机选择列表里的值
        if strategy == "失误":
            print("街霸在对战中反击失误!")
        else:
            print("街霸在对战中对你使用了{}".format(strategy))

        time.sleep(2)

        if strategy in ["原地蹲防", "回血", "鬼步"]:  # 使用in运算符来查找strategey是否在列表中
            if strategy == "回血" and fighter < 100:
                fighter += 5
        elif strategy == "失误" and is_valid_attack:
            fighter -= 10  # 复合运算符
        elif strategy == "伤害修正":
            fighter -= 5  # 复合运算符
        elif strategy == "必杀":
            chunli -= 20  # 复合运算符
        else:
            chunli -= 10

        print("\n-*- 春丽现在的血量:{0}  维加现在的血量:{1} -*-".format(chunli, fighter))

    if chunli <= 0:
        print("春丽，你战败了！")
    else:
        print("维加，我今天终于把你打败，父亲泉下有知，可以瞑目了！")


if __name__ == "__main__":
    main()
