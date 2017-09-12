
# 0.怎样学习python


```python
（1）安装环境
（2）入门教材
（3）学习方法
（4）重要概念
```

# 1.安装环境


```python
(1)设备为Windows7 32位系统，Python版本可以安装2或3。（由于教材使用《奔办法学Python》，该书使用Python2，可先下载，使用Python2.）
(2)在Python官网下载Python2.7.4。
(3)将Python安装到内含版本号的路径，例如Python2.7.4版本安装到 C:\Python27\。
(4)修改PATH环境变量。在powershell下输入
   【Environment】::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User"),重启powershell或计算机让路径生效。
   （$符号按 SHIFT+4，我输入时找了很久）在电脑 开始-程序 中就可找到Windows Powershell.
(5)终端暂且用powershell,编辑器使用notepad。初步入门后终端可用cmd,编辑器用atom。
```

# 2.入门教材 


```python
（1）《与孩子一起学编程》
这是写给孩子看的Python编程书，非常浅显易懂，是爸爸和孩子的对话，有很多图片，对很细小的术语也有详细解释。立刻进入gui写游戏，生动有趣。
（2）《笨办法学Python》，按照书中要求把每一个练习输入notepad中，在powershell上运行，附加练习也要认真做。
编程就像学习语言.乐器一样，需要不断的练习.实践，在做中学，而不能仅仅看书，看视频。
不懂的代码写注释，新的知识点在Google上查。
（3）《Python简明教程》
（4）mit公开课 《计算机科学与Python编程导论》，学习计算思维；哈佛大学公开课《计算机科学CS50》
除编程教材之外可以看看跟计算机.编程.互联网有关的一些科普书，如《黑客与画家》.《浪潮之巅》.《信息简史》《编码.隐匿在计算机软硬件背后的语言》.《黑客.计算机革命的英雄》《大教堂与集市》
```

# 3.学习方法


```python
（1）多写代码
（2）遇到问题Google,
（3）善于记录。运用jupyter notebook 记录。
（4）找到同伴，相互交流请教。
```

# 4.重要概念

## （0）重要概念


```python
1.常量与变量   2.注释.交互.转义字符.   3 函数.模块.参数.解包   4.控制流 if语句.while循环.for循环    5.复杂数据类型  列表.字典.类
```

## （1）常量与变量

### 1.0 常量与常量类型


```python
常量：如 1, 1.23这样的数与 'This is a string.'"It's a string"这样的字符串 都是常量，它们的意义不会改变。

数：即数字，数据类型分为int（整数）与float（浮点数）。1,2，-1,都为整数；1.5,-2.9,3.1415都为浮点数。

字符串：由单引号或双引号括起来的文字。如“I have a computer.” 'There are 8 trees.' 。数字引号括起来也成了字符串，
如 4 是数， “4”是字符串。
```

### 1.1 变量
变量：变量相当于一个标签，它所指向的内容可以发送变化。
变量名由字母和下划线和数字构成，数字不能放在开头，不能有空格。如string ，this_is_a_number, apples_10。
我们可以给变量赋值。如 string = "Mary has a little lamb." ,string = "Hurry up",string这个变量的内容发生了改变。又如 this_is_a_number = 12,
apples_10 = "cheep"。

赋值：用“=”将等号右边的内容（如数字，字符串）与等号左边的变量名相关联，如 name = "Paul" ,number = 10 。
## (2)交互.注释.转义字符

### 2.0 交互



### 2.1 注释


```python

```

### 2.2 转义字符


```python

```

## （3）函数.模块.参数.解包

### 3.0 函数


```python

```

### 3.1 模块


```python

```

### 3.2 参数


```python

```

### 3.3 解包


```python

```


```python

```

## （4）控制流 if语句.while循环.for循环


```python

```


```python

```

## （5）复杂数据类型  列表.字典.类


```python

```


```python

```
