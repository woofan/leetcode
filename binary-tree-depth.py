import copy
def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    temp = copy.deepcopy(board)
    for i in temp:
        i.append(0)
        i.insert(0,0)
    pass

a = [1,2,3]
a.insert(0,0)
print(a)