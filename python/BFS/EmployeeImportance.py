'''
690. Employee Importance

You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this employee and all their subordinates.

 

Example 1:


Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Example 2:


Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
'''

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
        imp_sum = 0
        imp_dict = defaultdict(int)
        sub_dict = defaultdict(list)
        for employee in employees:
            imp_dict[employee.id] = employee.importance
            sub_dict[employee.id].append(employee.subordinates)
        
        queue = deque()
        visited = set()
            
        queue.append(id)
        visited.add(id)
            
        while queue:
            curr = queue.popleft()
            imp_sum += imp_dict[curr]
            for subordinates in sub_dict[curr]:
                for subordinate in subordinates:
                    if subordinate in visited:
                        continue
                    else:
                        queue.append(subordinate)
                        visited.add(subordinate)
                    
        return imp_sum
            
                
                
        
        
        