from LinkList import LinkList

L = LinkList()
for i in range(26):
    L.insert(i, (chr(ord('a') + i)))
print(L.length())
while True:
    i = int(input("请输入需要查询元素的位序号：\n"))
    if -1 < i < 26:
        print("第%s个元素为：%s" % (i, L.get(i-1)))
    else:
        print("位置非法")
