'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：你的初始资金为100 每猜一次减10  资金为0时或者猜成功游戏 结束
    猜大 如果你输入的数字和随机数对比 大于随机数  打印一句话为  猜大了
    猜小 如果你输入的数字和随机数对比 小于随机数  打印一句话为  猜小了
'''
import random
number = 1
levelnum = 10
randomNumber = random.randint(0, 15)
guessNumber = 0
print("--------------hi!这是一个猜数字的游戏哦------------")
tryNumber = 10
level = 100
def Game():
    global tryNumber
    global guessNumber
    while tryNumber < level and guessNumber != randomNumber:
        guessNumber = input("你好，请输入你猜到的数字(0-15)：")
        if not str.isdigit(guessNumber):
            print("输入格式有误,请输入零到15的整数.")
        if str.isdigit(guessNumber):
         guessNumber = int(guessNumber)
         if guessNumber > 15:
          print("太大了，不是这个哦！是0-15之间的数字哦")
         if guessNumber < randomNumber:
          print("猜小了 你还剩" + str(level-tryNumber) + "元")
         elif guessNumber > randomNumber:
          print("猜大了 你还剩" + str(level-tryNumber) + "元")
        tryNumber = tryNumber + 10
Game()
if guessNumber != randomNumber and tryNumber > 10:
    strrandom = str(randomNumber)
    print("哈哈 你的钱用完了哦，其实这个数字是" + strrandom )
while guessNumber == randomNumber :
    print("你好厉害 恭喜你 ")
    break




