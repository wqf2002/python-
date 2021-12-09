from SeqList import SeqList

design_list = SeqList(20)
d_list = [12, 43, 64, 76, 44, 86, 97, 88, 45, 7, 35, 99, 0, 65]
for item in d_list:
    design_list.insert_front(item)
design_list.display()
design_list.max_list()
