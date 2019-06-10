#-*- coding:utf-8 -*-

# __filename__ = "secret_of_chinatown.py"
# __author__ = "薯条社区"
# __date__ = "2019-06-10"

import random  # 导入random模块，来获取随机数


# 在python中使用def来定义函数
# 初学者简单的吧函数理解为输入到输出的转换即可
# 在后续的教程中会对函数进行详细讲解
# 定义bubble_sort函数，来实现冒泡排序,函数的输入是一个列表类型

def bubble_sort(kungfu_codes):
    '''
    :param kungfu_codes: 这里的kungfu_codes是函数的输入，表示师傅刚拳的奥义密码
    :return: 将师傅刚拳的奥义密码排序，然后获取最大的奥义密码
    '''

    # 执行python的内置函数len来获取列表的长度
    kungfu_codes_size = len(kungfu_codes)

    # 列表一共有kungfu_codes_size个元素，那么最多进行kungfu_codes_size-1轮比较

    # 定义变量compare_loops来保存比较的轮数
    compare_loops = 0

    #  compare_loops < kungfu_codes_size-1的比较操作会转换为一个布尔类型
    #  compare_loops >= kungfu_codes_size-1是会自动退出循环
    while compare_loops < kungfu_codes_size-1:

        # 定义变量index用来保存气泡的索引，索引值会不断递增
        # 这样才能实现相邻气泡比较的逻辑
        index = 0

        # 这里的compare_loops表示比较轮数，在第一轮比较完后，在
        # 剩下的元素中只要比价kungfu_codes_size-1-compare_loops次，
        # 读者可以按照教程中的内容自行进行推导

        while index < (kungfu_codes_size-1-compare_loops):
            # 相邻气泡两两进行比较
            if kungfu_codes[index] > kungfu_codes[index+1]:
                # 如果当前气泡大于前面的气泡，则相互交换位置
                kungfu_codes[index], kungfu_codes[index+1] = kungfu_codes[index+1], kungfu_codes[index]
            index += 1

        compare_loops += 1


def main():
    '''
    :return:void
    '''

    # 在后续教程中在介绍循环控制结构的时候，届时会再对列表推导式进行讲解
    # 这里使用列表推导式来生成一个从0到1000的随机数列表，列表一共有10个元素
    kungfu_codes = [random.randint(0, 1000) for index in range(10)]

    print("师傅遗留的刚拳奥义值分布:", kungfu_codes)
    # 执行bubble_sort对列表进行升序排序
    bubble_sort(kungfu_codes)
    print("隆利用冒泡排序成功地在一纳秒内理清了杂乱的奥义分布:", kungfu_codes)
    the_secret_code = kungfu_codes[-1] #获取列表倒数第一个数，即为最大的数
    print("最大的刚拳奥义值:{}".format(the_secret_code))

if __name__ == "__main__":
    main()