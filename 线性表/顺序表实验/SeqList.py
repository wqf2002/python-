class SeqList:
    def __init__(self, maxsize):
        self.curLen = 0
        self.maxSize = maxsize
        self.listItem = [None] * self.maxSize

    def is_empty(self):
        return self.curLen == 0

    def length(self):
        """求顺序表的长度"""
        print("list length is:", self.curLen - 1)

    def clear(self):
        """清空顺序表"""
        self.curLen = 0

    def get(self, i):
        """返回顺序表指定位置上的元素"""
        if i < 0 or i > self.curLen - 1:
            raise Exception("i is not exist")
        return self.listItem[i - 1]

    def insert_front(self, x):
        """在顺序表的表头插入元素"""
        if self.curLen == self.maxSize:
            raise Exception("list max")
        for j in range(self.curLen, 0, -1):
            self.listItem[j] = self.listItem[j - 1]
        self.listItem[0] = x
        self.curLen += 1
        print(x, "Front inserted successfully")

    def insert_rear(self, x):
        """在顺序表的表尾插入元素"""
        if self.curLen == self.maxSize:
            raise Exception("list max")
        self.listItem[self.curLen] = x
        self.curLen += 1
        print(x, "Rear inserted successfully.")

    def insert(self, i, x):
        """在顺序表的任意位置插入元素"""
        if self.curLen == self.maxSize:
            raise Exception("list max")
        if i < 0 or i > self.curLen:
            raise Exception("insert location illegal")
        for j in range(self.curLen, i - 1, -1):
            self.listItem[j] = self.listItem[j - 1]
        self.listItem[i] = x
        self.curLen += 1
        print("Successfully inserted", x, "at", i)

    def deleteFront(self):
        """删除顺序表的表头元素，返回删除元素"""
        print("head delete", self.listItem[0])
        for j in range(0, self.curLen):
            self.listItem[j - 1] = self.listItem[j]
        self.curLen -= 1

    def delete_rear(self):
        """删除顺序表的表尾元素，返回删除元素"""
        print("rear delete", self.listItem[self.curLen])
        self.curLen -= 1

    def delete(self, i):
        """删除任意位置上的元素，返回删除元素"""
        if i < 0 or i > self.curLen - 1:
            raise Exception("delete location illegal")
        else:
            print(self.listItem[i], "has been delete.")
            for j in range(i, self.curLen):
                self.listItem[j] = self.listItem[j + 1]
            self.curLen -= 1

    def search(self, x):
        """查找指定的元素，返回其在线性表中的位置"""
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i

    def display(self):
        """正向输出顺序表的所有元素"""
        print("display result is:")
        for i in range(self.curLen):
            print(self.listItem[i], end=' ')

    def redisplay(self):
        """逆向输出顺序表所有元素"""
        print("redisplay result is:")
        for i in range(self.curLen, 0, -1):
            print(self.listItem[i], end=' ')

    def max_list(self):
        """求出顺序表中的最大值"""
        ordinary_list = []
        for i in range(self.curLen):
            ordinary_list.append(self.listItem[i])
        max_num = ordinary_list[1]
        for num in ordinary_list:
            if num > max_num:
                max_num = num
        print("Max number is:", max_num)
