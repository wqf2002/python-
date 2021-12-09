from SeqList import SeqList
from random import randint

_list = SeqList(100)
for _i in range(10):
    a = randint(0, 100)
    _list.insert_rear(a)
print(_list.length())
print(_list.display())
for i in range(_list.curLen):
    if _list.listItem[i] == 30:
        print("30 is exist.")
        break
else:
    print("30 is not exist.")
print(_list.get(6))
_list.insert_front("29")
_list.insert_front("77")
print(_list.length())
_list.redisplay()
_list.deleteFront()
_list.delete_rear()
_list.delete(6)
_list.display()
