from sys import argv
import re
import sys

script, filename = argv

txt = open(filename, 'r')
print ("这是一个天气查询系统。" )
weather = txt.read()
wea = re.split(r'[,\s]',weather)

d = {}

for i in range(0, len(wea), 2):
    d[wea[i]] = wea[i+1]

city = str(0)
result =str(0)

history= []
while True:
    city = str(input("请输入指令或您要查询的城市名："))
    result = d.get(city, "没有您要查询的城市信息，请您输入附近的城市")
    print (result)

    if city == "help":
        print ("""
        输入城市名，查询该城市的天气；
        输入help，获取帮助信息；
        输入history，获取查询历史；
        输入quit，退出天气查询系统。
        """)

    if city in d:
        history.append(city + ":" + result)

    if city == "history":
        print (history)

    if city == "quit":
        break
