# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
#       有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ord() : 返回单字符在ASCII中对应的整数
for a in range(ord('x'),ord('z') + 1):
    for b in range(ord('x'),ord('z') + 1):
        if a != b:
            for c in range(ord('x'),ord('z') + 1):
                if (a != c) and (b != c):
                    if (a != ord('x')) and (c != ord('x')) and (c != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(a),chr(b),chr(c)))