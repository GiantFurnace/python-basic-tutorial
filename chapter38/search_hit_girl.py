# -*- coding:utf-8 -*-

# __filename__ = "search_hit_girl.py"
# __author__ = "薯条社区"
# __date__ = "2019-07-04"

# 导入math模块，用来计算对数
import math

# 定义web_page系列变量来表示网页的内容
web_page1 = '''
超杀女hit girl，漫画《海扁王》中的暴力萝莉角色，她是大老霸——Big Daddy的女儿。
Big Daddy是一个一心要找黑帮老大复仇的离职警察，
从超杀女很小的时候就训练她各种战斗技巧，带着她四处打击犯罪团伙。
在Big Daddy去世以后，我们的hit girl更加坚定了对除暴的志向。
'''

web_page2 = '''
在《海扁王》中，年仅13岁的天才童星科洛·莫瑞兹扮演的血腥暴力“超杀女”hit girl是个
擅长使用各种兵器的11岁小女孩，
从小接受父亲“大老爸”的近身枪击（当然有穿防弹衣）、徒手战斗、刀械枪支等训练，
加上“大老爸”带着她四处打击犯罪，小小年纪便累积不少实战经验，成了杀人不眨眼的顶尖杀手。
她的主要武器是蝴蝶刀与武士刀，以研究各类武器为乐，对枪械更是了若指掌
'''

web_page3 = '''
扮演超杀女的科洛·莫瑞兹1997年2月10日出生于美国的佐治亚州，8岁便开始涉足影坛。
科洛年纪虽小，作品却不少，她的好莱坞生涯始于2003年，那年他们家搬到了洛杉矶。
'''


# 定义的分词器函数
def cut(text):
    '''
    :param text:待分词的文本
    :return:返回分词结果词典，分词数
    '''
    words = {}
    words_length = 0
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
                words_length += 1
                words[word] = 1 if word not in words else words[word] + 1
                text = text[index:]
                word_not_in_dictionary = False
                break

        if word_not_in_dictionary:
            # 如果匹配失败，则将文本的起始位置向前移动一个位置，重复进行上述的分词步骤
            text = text[1:]

    return words, words_length


# 此函数为构建倒排索引表
def build_inverse_index_table():
    '''
    :return:返回倒排索引表
    '''

    inverse_index_table = {}
    web_pages_length = len(WEB_PAGES)

    '''
    在for循环中逐一遍历列表中的网页，内置函数enumerate可以返回列表的索引和值
    假设列表为['a','b','c'] 
    那么在for循环中通过enumerate函数遍历出的为如下索引值对:
    索引0，值'a',索引1，值'b'，索引2，值'c'，其它的同理
    '''
    for index, web_page in enumerate(WEB_PAGES):
        # 对web_page进行分词
        terms, terms_length = cut(web_page)
        for term in terms:
            # 计算term的tf值
            tf = round(terms[term] / terms_length, 4)
            page = {"content": web_page, "tf": tf}
            if term not in inverse_index_table:
                inverse_index_table[term] = [page]
                continue
            # 如果term已存在于倒排表中，那么当前的term肯定是其它网页的term
            # 其它网页的term被添加进列表中，方便后续计算tf-idf
            inverse_index_table[term].append(page)

    for _, pages in inverse_index_table.items():
        terms_in_docs_length = len(pages)
        for page in pages:
            # 计算term的idf和tf-idf值
            page["idf"] = round(math.log10(web_pages_length / terms_in_docs_length)
                                , 4)
            page["tfidf"] = page["tf"] * page["idf"]

    return inverse_index_table


# 定义搜索函数
def search(text, inverse_index_table):
    '''
    :param text: 搜索串，在实际情况中，需要对搜索串再进行分词，这里只是举个简单的例子
    :param inverse_index_table: 倒排索引表
    :return: 返回已搜索到的内容
    '''

    contents = []
    pages = inverse_index_table.get(text, [])

    if pages:
        pages = sorted(pages, key=lambda page: page["tfidf"], reverse=True)
        for page in pages:
            contents.append(page["content"])

    return contents


if __name__ == "__main__":

    # 在__main__中定义的变量，在其它函数中可以直接引用

    # 定义词典，用来保存分词的词语，读者也可以自行扩充其它的词语
    DICTIONARY = {"小女孩", "海扁王", "科洛·莫瑞兹",
                  "超杀女", "蝴蝶刀", "武士刀", "枪械",
                  "暴力萝莉", "杀人不眨眼", "hit girl"}

    # 词典中最常的词为"hit girl",长度为8
    # 读者可以自行写个函数，来计算集合中最长词语的宽度，这留作课后习题

    WEB_PAGES = [web_page1, web_page2, web_page3]
    THE_MAX_LENGTH_OF_WORD = 8

    inverse_index_table = build_inverse_index_table()
    contents = search("hit girl", inverse_index_table)

    print("搜索到的内容:")
    for _ in contents:
        print("{}".format(_))
