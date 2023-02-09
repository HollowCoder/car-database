class Lane:
    def __init__(self):
        self.lane = []

    def enqueue(self, vehicle):
        self.lane.append(vehicle)
    
    def dequeue(self):
        if len(self.lane) < 1:
            return None
        return self.lane.pop(0)
    
    def display(self):
        print(self.lane)
    
    def size(self):
        return len(self.lane)