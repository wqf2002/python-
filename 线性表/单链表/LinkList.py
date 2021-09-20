from Node import Node
from abstract import IList


class LinkList(IList):
    def __init__(self):
        self.head = Node()  # 构造函数初始化头节点

    def create(self, l, order):
        if order:
            self.create_tail(l)
        else:
            self.create_head(l)

    def create_tail(self, l):
        for item in l:
            self.insert(self.length(), item)

    def create_head(self, l):
        for item in l:
            self.insert(0, item)

    def clear(self):
        """将线性表置成空表"""
        self.head.data = None
        self.head.next = None

    def isEmpty(self):
        """判断线性表是否为空表"""
        return self.head.next is None

    def length(self):
        """返回线性表长度"""
        p = self.head.next
        length = 0
        while p is not None:
            p = p.next
            length += 1
        return length

    def get(self, i):
        """读取并返回线性表中的第i个数据元素"""
        p = self.head.next  # p指向单链表的首结点
        j = 0
        # 从首结点开始向后查找，直到p指向第i个结点或者p为None
        while j < i and p is not None:
            p = p.next
            j += 1
        if j > i or p is None:  # i不合法时抛出异常
            raise Exception("第%s个数据元素不存在" % i)
        return p.data

    def insert(self, i, x):
        """插入x作为第i个元素"""
        p = self.head
        j = -1
        while p is not None and j < i - 1:
            p = p.next
            j += 1
        if j > i - 1 or p is None:
            raise Exception("插入位置不合法")
        s = Node(x, p.next)
        p.next = s

    def remove(self, i):
        """删除第i个元素"""
        pass

    def indexOf(self, x):
        """返回元素x首次出现位序号"""
        pass

    def display(self):
        """输出线性表中各个数据元素的值"""
        p = self.head.next
        while p is not None:
            print(p.data, end='')
            p = p.next
