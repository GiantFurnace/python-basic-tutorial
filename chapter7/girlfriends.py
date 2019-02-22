# -*- coding:utf-8 -*-
# 必须加上 # -*- coding:utf-8 -*- 这样程序文件中才能识别中文字符
# __date__ = 2019-02-12
# __author__ = 侠影七三

# if关键字声明了一个语句块，首行必须顶格，末尾以":"结束
if __name__ == "__main__":
    
	# 定义了一个多行字符串变量love_story, 与父级的if语句必须有2个或4个空格的缩进
	love_story_of_xiaoming = '''
	小明出生于1990年，他在12岁的时候就不好好读书玩早恋,谈了一个比他
   	小1岁的女朋友，15岁那年他们分手后小明耐不住寂寞又谈了个比他大5岁的女朋友，
   	后来我听村里那条悲伤地快断气的单身狗说，小明在读大学时又处了1个女朋友，
   	她的名字叫翠花!
   	'''

	# 定义了1个字符串变量 answer,与上文的love_story变量处于同一层次，保持相同的缩进
	answer = "小明一共谈了%d个女朋友,小明第一次谈女朋友时是%d年，小明最后那个女朋友的名字叫%s"
	
	# 定义了1个整型变量保存字符串count函数的返回值，保持相同的缩进，下文不再赘述
	girlfriends_count = love_story_of_xiaoming.count("女朋友")
	born_date_index = love_story_of_xiaoming.find("1990")
	age_index = love_story_of_xiaoming.find("12")
	
	# 使用int() 将数字字符串转换为整型变量
	first_love_year = int(love_story_of_xiaoming[born_date_index:born_date_index+4])\
					  +int(love_story_of_xiaoming[age_index:age_index+2])
	
	last_girlfriend_index = love_story_of_xiaoming.find("翠花")
	last_girlfriend_name = love_story_of_xiaoming[last_girlfriend_index:last_girlfriend_index+2]
	
	# 对answer字符串变量进行格式化输出
	print(answer % (girlfriends_count, first_love_year, last_girlfriend_name))
	
	
	
	
	
	
