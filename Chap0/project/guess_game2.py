import random

def guess_game():
    correct_num = random.randint(0, 20)
    count = 0
    print ("这是一个猜数字游戏,你最多有10次猜测机会")

    for count in range(1,11):
        guess_num = int(input("请输入一个20以内的数字："))
        
        count += 1

        if  guess_num < 0 or guess_num >= 20 :
            print ("您输入的内容不符合要求。")

        if guess_num ==correct_num:
            print ("恭喜你，猜对了！")
            break

        if guess_num > correct_num:
                print ("大于正确数字")

        if guess_num < correct_num:
                print ("小于正确数字。")

    if guess_num == correct_num:
        print ("正确数字是 %d" % correct_num )
    else:
        print ("您已经猜了10次，正确数字是 %d" % correct_num)

game = guess_game()
game
