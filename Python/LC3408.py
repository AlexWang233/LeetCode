class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskMap = {}
        self.pq = []
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, priority)
        heappush(self.pq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.taskMap:
            userId, _ = self.taskMap[taskId]
            self.taskMap[taskId] = (userId, newPriority)
            heappush(self.pq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]

    def execTop(self) -> int:
        while self.pq:
            priority, taskId = heappop(self.pq)
            priority, taskId = -priority, -taskId
            if taskId in self.taskMap and self.taskMap[taskId][1] == priority:
                userId, _ = self.taskMap[taskId]
                del self.taskMap[taskId]
                return userId
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()