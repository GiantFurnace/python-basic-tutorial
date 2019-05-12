# __filename__ = "love_and_hate.py"
# __author__ = "薯条社区"
# __date__ = "2019-05-11"

def main():

    love = 100  # 对你的爱意百分百
    while True: # 不断重复执行下面的代码
        answer = input("你还爱我吗?\n") # 执行input函数获得键盘的输入内容
        if answer != "爱":   # "!="其逻辑意义为"不等于"， 初学者意会即可
            love -= 10       # 不爱就减10分
            print("你没以前爱我了，你对我的爱意只剩 {}".format(love))
            if love <=50:
                print("你知道英语中的分手怎么拼吗？b-r-e-a-k! up !!!")
                break  # python中使用break退出循环 
        else:
            print("你对我还有爱意，不要嫌我啰嗦！")

    print("绵绵恨意，滔滔不息因你而起，take my breath away!")

if __name__ == "__main__":
    main()