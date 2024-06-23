def MedianFinderLinear():
    """
    6-21-24
    Linear approach
    """
    class MedianFinder:

        def __init__(self):
            self.node = []

        def addNum(self, num: int) -> None:
            if len(self.node) == 0:
                self.node.append(num)
                return

            for i in range(len(self.node)):
                if self.node[i] > num:
                    self.node = self.node[:i] + [num] + self.node[i:]
                    return

            self.node.append(num)

        def findMedian(self) -> float:
            if len(self.node) % 2:
                return self.node[(len(self.node)-1) // 2]
            else:
                l = (len(self.node)-1) // 2
                r = l+1
                return (self.node[l] + self.node[r]) / 2

    return MedianFinder()


def MedianFinderBinary():
    """
    6-21-24
    Binary Search
    """
    class MedianFinder:

        def __init__(self):
            self.node = []

        def addNum(self, num: int) -> None:
            if len(self.node) == 0:
                self.node.append(num)
                return

            l, r = 0, len(self.node) - 1

            while l <= r:
                m = (l+r)//2
                if self.node[m] > num:
                    r = m - 1
                else:
                    l = m + 1
            self.node = self.node[:l] + [num] + self.node[l:]

        def findMedian(self) -> float:
            if len(self.node) % 2:
                return self.node[(len(self.node)-1) // 2]
            else:
                l = (len(self.node)-1) // 2
                r = l+1
                return (self.node[l] + self.node[r]) / 2

    return MedianFinder()

# def MedianFinder():
#     class MedianFinder:

#         def __init__(self):

#         def addNum(self, num: int) -> None:

#         def findMedian(self) -> float:

#     return MedianFinder()
