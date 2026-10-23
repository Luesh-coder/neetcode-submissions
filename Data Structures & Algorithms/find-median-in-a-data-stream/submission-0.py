class MedianFinder:
    """
    initialize:
        create an empty list named data
    
    addNum:
        append to the list
    
    findMedian:
        sort the list
        obtain length of list

        if n is odd:
            return middle of list
        
        if n is even:
            return the average of two middle elements
    """
    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        return (self.data[n // 2] if (n & 1) else
                (self.data[n // 2] + self.data[n // 2 - 1]) / 2)
        