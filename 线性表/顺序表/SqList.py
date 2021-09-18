from abstract import IList


class SqList(IList):
    def __init__(self, maxsize=100):
        self.curLen = 0  # 顺序表当前长度
        self.maxSize = maxsize  # 顺序表最大长度
        self.listItem = [None] * self.maxSize  # 顺序表储存空间

    def clear(self):
        """将线性表置成空表"""
        self.curLen = 0

    def isEmpty(self):
        """判断线性表是否为空表"""
        return self.curLen == 0

    def length(self):
        """返回线性表长度"""
        return self.curLen

    def get(self, i):
        """读取返回线性表中第i个数据元素"""
        if i < 0 or i > self.curLen - 1:
            raise Exception("第i个元素不存在")
        return self.listItem[i]

    def insert(self, i, x):
        """插入x作为第i个元素"""
        if self.curLen == self.maxSize:
            raise Exception("顺序表满")
        if i < 0 or i > self.curLen:
            raise Exception("插入位置非法")
        for j in range(self.curLen, i - 1, -1):
            self.listItem[j] = self.listItem[j - 1]
        self.listItem[i] = x
        self.curLen += 1

    def remove(self, i):
        """删除第i个元素"""
        if i < 0 or i > self.curLen - 1:
            raise Exception("删除位置非法")
        for j in range(i, self.curLen):
            self.listItem[j] = self.listItem[j + 1]
            self.curLen -= 1

    def indexOf(self, x):
        """返回元素x首次出现的位序号"""
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        """输出线性表中各个数据元素值"""
        for i in range(self.curLen):
            print(self.listItem[i], end='')
