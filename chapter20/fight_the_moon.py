#-*- coding:utf-8 -*-

# __filename__ = "fight_the_moon.py"
# __author__ = "薯条社区"
# __date__ = "2019-06-03"

import random  # 导入random模块
import time  # 导入time模块，使用模块中的sleep方法来模拟倒计时

'''
    定义字典变量来保存春丽和神月卡琳的格斗技，
    键为招数名称，值为招数对应的伤害值
    其中超必杀的键值表示超必杀最多使用的次数
    超必杀的伤害统一为20
'''

karin_kungfu = {
                            "原地蹲防": 0,
                            "失误": 0,
                            "红莲拳": 5,
                            "红莲崩掌": 10,
                            "红莲歼破 ": 15,
                            "暴血连段": 15,
                            "红莲奥义": 15,
                            "回血": 10,
                            "超必杀-神月流 霸道六式": 3
                        }

chunli_kungfu = {
                            "原地蹲防": 0,
                            "失误": 0,
                            "龙星落": 5,
                            "气功拳": 5,
                            "旋转踢": 10,
                            "百裂脚": 10,
                            "霸山天升脚": 10,
                            "超必杀-千翼气功掌": 2
                        }


def main():
    '''
    :return:void
    '''
    karin = 100  # 定义整型变量karin,用来保存神月卡琳的血量
    chunli = 100  # 定义整型变量chunli，用来保存春丽的血量

    # 对战倒计时
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(0.2)
    print("Fight!")

    # 定义整型变量super_harms 来保存超必杀懂得伤害值
    super_harms = 20

    # 循环语句，不断重复执行下面的代码
    while True:
        # 春丽或神月卡琳其中一人血量为0时就退出循环
        if chunli <= 0 or karin <= 0:
            break
        # 1. 先执行字典的keys方法，获取字典的键名对象{键1, 键2}
        # 2. 然后使用list类型来进行显示类型转换，将键值对象转换为列表[键1, 键2]
        # 3. 最后执行random模块的choice方法随机获取键名

        chunli_strategy = random.choice(list(chunli_kungfu.keys()))
        karin_strategy = random.choice(list(karin_kungfu.keys()))

        # 随机获取0到11之间的数字，在与2进行取模运算
        random_key = random.randint(0, 11) % 2

        # random_key为偶数时表示春丽先发起攻击，否则表示神月卡琳先发起攻击
        if random_key == 0:
            if chunli_strategy != "失误" and karin_strategy != "失误":
                print("-- 春丽对神月卡琳使用了{0}, 神月卡琳使用{1}进行了回击".
                      format(chunli_strategy, karin_strategy))
            elif chunli_strategy == "失误":
                print("-- 春丽攻击神月卡琳产生了{0}, 神月卡琳使用{1}进行了回击".
                      format(chunli_strategy, karin_strategy))
            else:
                print("-- 春丽对神月卡琳使用了{0}, 神月卡琳在回击中产生了{1}".
                      format(chunli_strategy, karin_strategy))
        else:
            if chunli_strategy != "失误" and karin_strategy != "失误":
                print("-- 神月卡琳对春丽使用了{1}, 春丽使用{0}进行了回击".
                      format(chunli_strategy, karin_strategy))
            elif karin_strategy == "失误":
                print("-- 神月卡琳攻击春丽时产生了{1}, 春丽使用{0}进行了回击".
                      format(chunli_strategy, karin_strategy))
            else:
                print("-- 神月卡琳对春丽使用了{1}, 春丽在回击中产生了{0}".
                      format(chunli_strategy, karin_strategy))


        # 这里使用了in操作符 来判断元素是否在列表中
        if chunli_strategy == "原地蹲防" or karin_strategy in ["原地蹲防", "回血"]:
            continue     # continue语句表示跳过接下来的代码，继续下一轮循环

        if chunli_strategy.find("超必杀") != -1:
            harm = super_harms - karin_kungfu[karin_strategy]
            karin -= harm
            chunli_kungfu[chunli_strategy] -= 1
            if chunli_kungfu[chunli_strategy] == 0:
                # 表示已使用完超必杀次数，使用字典的pop方法将键进行删除
                chunli_kungfu.pop(chunli_strategy)

        elif karin_strategy.find("超必杀") != -1:
            harm = super_harms - chunli_kungfu[chunli_strategy]
            chunli -= harm
            karin_kungfu[karin_strategy] -=1
            if karin_kungfu[karin_strategy] == 0:
                # 表示已使用完超必杀次数，使用字典的pop方法将键进行删除
                karin_kungfu.pop(karin_strategy)
            print("神月卡琳(女王三段笑):Ah~~ho~ho~ho~ho~")
        else:
            harm = chunli_kungfu[chunli_strategy] - karin_kungfu[karin_strategy]
            if harm > 0:
                karin -= harm
            elif harm < 0:
                chunli += harm
                print("神月卡琳(女王三段笑):Ah~~ho~ho~ho~ho~")

        print("*---春丽的血量:{0}, 神月卡琳的血量:{1}---*\n\n".format(chunli, karin))
        time.sleep(3)

    if chunli <=0:
        print("春丽被神月卡琳击败，奄奄一息，擂台上再次响起了神月卡琳标志性的女王三段笑:"
              "Ah~~ho~ho~ho~ho~\n卡琳随后纵身而去！")
    else:
        print("神月卡琳被春丽击倒在地，春丽突然一跃而起，飞向擂台下的幕后黑手......")

if __name__ == "__main__":
    main()