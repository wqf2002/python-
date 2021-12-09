from SeqList import SeqList

# 1.从键盘输入10个整数，建立一个有序的顺序表listA，输出顺序表的长度并遍历输出顺序表。

# 方法一
listA = SeqList(15)
print("Please enter ten numbers：")
n = 0
while n != 10:
    itemA = int(input())
    listA.insert_rear(itemA)
    n += 1
listA.length()
listA.display()

# 方法二
# listA = SeqList(15)
# num = input("Please enter ten numbers,split with 'space':")
# num_list = num.split()
# while len(num_list) != 10:
#     num = input("The number of elements is insufficient. Please re-enter：")
#     num_list = num.split()
# for item in num_list:
#     listA.insert_rear(item)
# listA.length()
# listA.display()

# 2.键盘输入一个数，检查顺序表listA中是否存在，若不存在则插入到顺序表中，然后输出之。
keyboard_num = int(input("Please enter a number："))
position = listA.search(keyboard_num)
if position is None:
    print("There is no such number，add this number into list.")
    listA.insert_rear(keyboard_num)
    print(listA.get(listA.curLen - 1))
else:
    print("This number is exist.")
listA.display()

# 3.从键盘输入10个整数，建立一个有序的顺序表listB，输出顺序表的长度并遍历输出顺序表。
listB = SeqList(15)
print("Please enter ten numbers：")
n = 0
while n != 10:
    itemB = int(input())
    listB.insert_rear(itemB)
    n += 1
listB.length()
listB.display()

# 4.键盘输入一个数，检查顺序表中是否存在，若存在则删除它，然后输出之。
keyboard_num = int(input("Please enter a number："))
position = listB.search(keyboard_num)
if position is None:
    print("There is no such number.")
else:
    print("This number is exist,delete it from list.")
    listB.delete(position)
listB.display()

# 5.合并两表listA和listB为listC并保持listC依然有序，要求输出listC。
listC = SeqList(40)
for i in range(listA.curLen):
    if listB.search(listA.listItem[i]) is None:
        listC.insert_front(listA.listItem[i])
for j in range(listB.curLen):
    listC.insert_front(listB.listItem[j])
listC.display()


