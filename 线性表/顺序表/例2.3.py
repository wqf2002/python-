from SqList import SqList

L = SqList(200)
for i in range(26):
    L.insert(i, (chr(ord('a') + i)))
while True:
    i = int(input("请输入需要查询元素的位序号：\n"))
    if 0 < i < 25:
        print("第%s个元素的直接前驱为：%s" % (i, L.get(i - 1)))
        print("第%s个元素的直接后驱为：%s" % (i, L.get(i + 1)))
    elif i == 0:
        print("第%s个元素的直接前驱不存在" % (i,))
        print("第%s个元素的直接后驱为：%s" % (i, L.get(i + 1)))
    elif i == 25:
        print("第%s个元素的直接前驱为：%s" % (i, L.get(i - 1)))
        print("第%s个元素的直接后驱不存在" % (i,))
    else:
        print("位置非法")
