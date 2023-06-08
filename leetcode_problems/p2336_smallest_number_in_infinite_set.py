# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:
#   SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
#   int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#   void addBack(int num) Adds a positive integer num back into the infinite set,
#       if it is not already in the infinite set.
# ---------------------------
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.


class SmallestInfiniteSet:

    def __init__(self):
        pass

    def popSmallest(self) -> int:
        pass

    def addBack(self, num: int) -> None:
        pass


test1 = [[], [2], [], [], [], [1], [], [], []]
test1_out = [None, None, 1, 2, 3, None, 1, 4, 5]
