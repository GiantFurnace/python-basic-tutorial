#-*- coding:utf-8 -*-

# __filename__ = "hit_girl.py"
# __author__ = "薯条社区"
# __date__ = "2019-06-26"


# 定义sentence变量，内容引用自百度百科，我们在代码中会将这段描述进行分词
sentence = '''
在《海扁王》中，年仅13岁的天才童星科洛·莫瑞兹扮演的血腥暴力“超杀女”是个擅长使
用各种兵器的11岁小女孩，从小接受父亲“大老爸”的近身枪击（当然有穿防弹衣）、
徒手战斗、刀械枪支等训练，加上“大老爸”带着她四处打击犯罪，
小小年纪便累积不少实战经验，成了杀人不眨眼的顶尖杀手。
她的主要武器是蝴蝶刀与武士刀，以研究各类武器为乐，对枪械更是了若指掌
'''


# 定义的分词器函数
def cut(text):
    '''
    :param text:待分词的文本
    :return:返回分词列表
    '''
    words = []

    # 将text变量作为判断条件，如果text为空值，则停止循环
    # 在循环中会不断将text变量进行切片
    while text:
        # 定义word_not_in_dictionary布尔类型变量，用来判断是否分词成功
        word_not_in_dictionary = True
        # 执行range函数会生成一个整数序列，
        # 读者可以查阅官方文档，来了解range函数的用法
        # 这里的range函数为生成一个倒排序列，比如6,5,4,3,2,1
        for index in range(THE_MAX_LENGTH_OF_WORD, 0, -1):
            # 对文本按最大宽度进行切片
            word = text[:index]
            # 如果切片分出来的词语在词典集合中，就保存到列表words变量中，并且退出for循环
            # 在集合中进行快速查找
            if word in DICTIONARY:
                words.append(word)
                text = text[index:]
                word_not_in_dictionary = False
                break

        if word_not_in_dictionary:
            # 如果匹配失败，则将文本的起始位置向前移动一个位置，重复进行上述的分词步骤
            text = text[1:]

    return words



if __name__ == "__main__":

    # 在__main__中定义的变量，在其它函数中可以直接引用

    # 定义词典，用来保存分词的词语，读者也可以自行加入其它的词语
    DICTIONARY = {"小女孩","海扁王", "科洛·莫瑞兹",
                  "超杀女", "蝴蝶刀", "武士刀", "枪械",
                  "暴力萝莉","杀人不眨眼"}

    # 词典中最常的词为"科洛·莫瑞兹",长度为6
    # 读者可以自行写个函数，来计算集合中最常词语的宽度，这留作课后习题

    THE_MAX_LENGTH_OF_WORD = 6

    # 执行cut函数，来对文本进行分词
    words = cut(sentence)
    print(words)