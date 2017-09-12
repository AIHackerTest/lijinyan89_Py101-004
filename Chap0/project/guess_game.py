import random

correct_num = int(random.randint(0,20))
print ("这是一个猜数字游戏。")
count = 0

while count < 10:
    guess_num = int(input("请随机输入一个20以内的数字："))
    count += 1

    if guess_num == correct_num:
        print ("恭喜您，猜对了！")
        break

    if guess_num < 0 or guess_num >= 20:
        print ("输入数字不符合要求。请输入20以内的数字。")

    if guess_num < correct_num:
        print ("您输入的数字小于正确数字")


    if guess_num > correct_num:
        print ("您输入的数字大于正确数字")

if guess_num == correct_num:
    print ("正确数字是 %d" % correct_num)
else:
    print ("你没有猜对数字，正确数字是 :", correct_num)
