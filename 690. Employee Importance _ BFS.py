"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
## time, space - O(N)
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_dct = {}
        for emp in employees:
            emp_dct[emp.id] = [emp.importance, emp.subordinates]
        curr, res = [id], 0
        while curr:
            nxt_lvl = []
            for i in curr:
                res += emp_dct[i][0]
                nxt_lvl.extend(emp_dct[i][1])
            curr = nxt_lvl
        return res