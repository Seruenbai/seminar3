class MyQueue:
    def__init__(self):
        self.qList=list()
    def isEmpty(self):
        return len(self)==0
    def__len__(self):
        return len(self._qList)
    def enqueue(self,item):
        self.qList.append(item)
    def dequeue(self):
        assert not self.isEmpty(),"Cannot dequeue from an empty queue"
        return self.qList.pop(0)
    def printer(self):
return self.qList
