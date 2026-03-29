from heapq import *
from collections import *
class EventManager:
    

    def __init__(self, events: list[list[int]]):
        self.d=defaultdict(int)
        self.h=[] 
        heapify(self.h)
        for i in events:
            self.d[i[0]] = -i[1]
            heappush(self.h, (-i[1], i[0]))
        
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        heappush(self.h, (-newPriority, eventId))
        self.d[eventId]=-newPriority
   

    def pollHighest(self) -> int:
        if not self.h:
            return -1

        while self.h:
            l=heappop(self.h)
            if self.d[l[1]] == l[0]:
                del self.d[l[1]]
                return l[1]
        return -1
            
       
        

