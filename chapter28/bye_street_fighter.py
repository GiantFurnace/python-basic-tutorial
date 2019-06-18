#-*- coding:utf-8 -*-

# __filename__ = "bye_street_fighter.py"
# __author__ = "薯条社区"
# __date__ = "2019-06-18"

import random  # 导入random模块，来获取随机数


# 冒泡排序函数
def bubble_sort(street_fighters):
    '''
    :param street_fighters: 这里的street_fighters是函数的输入，保存的是街霸英雄
    :return: void
    '''

    # 执行python的内置函数len来获取列表的长度
    fighters_size = len(street_fighters)


    # 定义变量compare_loops来保存比较的轮数
    compare_loops = 0

    while compare_loops < fighters_size-1:

        # 定义变量index用来保存气泡的索引，索引值会不断递增
        # 这样才能实现相邻气泡比较的逻辑
        index = 0

        while index < (fighters_size-1-compare_loops):
            # 相邻气泡两两进行比较,这里实际比较的是街霸英雄的武力值
            if street_fighters[index][0] > street_fighters[index+1][0]:
                # 如果当前气泡大于前面的气泡，则相互交换位置
                street_fighters[index], street_fighters[index+1] = street_fighters[index+1], street_fighters[index]
            index += 1

        compare_loops += 1

# 定义的二分查找函数
def binary_search(street_fighters, harm):
    '''
    :param street_fighters: 已排序的列表
    :param harm: 待查的伤害值
    :return: 返回伤害值所对应的街霸英雄
    返回值是一个元组类型，格式举例：
    (88, {"name": "春丽"})
    '''

    # 执行python的内置函数len来获取列表的长度
    fighters_size = len(street_fighters)


    start_index = 0
    end_index = fighters_size -1

    # 将起始位置的索引与结束位置的索引相加，再与2进行整除，可得到中间位置的索引
    index = (start_index + end_index) // 2

    # 在循环中会不断更新中间位置index的值，起始位置的值，结束位置的值
    # 如果起始索引start_index的值比结束索引的值还大，说明已经查完了所有区间
    # start_index 与 end_index进行关系运算的结果会转换为一个布尔类型
    # 布尔值为真，则继续执行循环里的代码，布尔值为假，则退出循环

    while start_index <= end_index:
        # 如果中间位置的值等于待查的值，则直接返回
        if street_fighters[index][0] == harm:
            # 在函数中使用return来返回值
            return street_fighters[index]

        # 如果中间位置的值大于待查找的值
        elif street_fighters[index][0] > harm:
            # 那么从左半段开始查起, 此时结束位置的索引变为中间位置的索引
            end_index = index - 1
            # 更新中间位置的索引
            index = (start_index + end_index) // 2
        else:
            # 否则从右半段开始查起，此时起始位置的索引变为中间位置的索引
            start_index = index + 1
            index = (start_index + end_index) // 2

    # 退出循环时表示未查到，返回None值
    return None


def main():
    '''
    :return:void
    '''

    # 定义一个列表，列表中的元素是元组
    # 元组中第一个元素是街霸英雄的武力值，第二个元素是一个字典
    # 字典的键名是name, 键值是街霸英雄的姓名

    street_fighters = [
                        (98, {"name": "隆"}),
                        (95, {"name": "刚拳"}),
                        (99, {"name": "豪鬼"}),
                        (90, {"name": "维加"}),
                        (88, {"name": "春丽"}),
                        (85, {"name": "神月卡琳"}),
                        (87, {"name": "巴洛克"})
                    ]

    # 使用冒泡排序，将列表按升序进行排序
    bubble_sort(street_fighters)
    harm = 88
    # 使用二分查找算法，查找伤害值为85的街霸英雄
    hero = binary_search(street_fighters, harm)

    if hero:
        print("伤害值{}对应的英雄是{}".format(harm, hero[1]["name"]))

if __name__ == "__main__":
    main()