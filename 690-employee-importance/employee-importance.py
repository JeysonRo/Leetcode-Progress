"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        table = {}

        for employee in employees:
            table[employee.id] = employee
        
        def dfs(id):
            employee = table[id]
            total_importance = 0
            if len(employee.subordinates) == 0:
                return employee.importance
            else:
                for i in employee.subordinates:
                    total_importance += dfs(i)
                return total_importance + employee.importance
        
        return dfs(id)
            