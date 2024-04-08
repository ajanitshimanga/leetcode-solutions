from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Circular and square sandwiches for lunch, 0 and 1 respectively.
        Students in a QUEUE.
        Each student has a preference and only 1 sandwich per student.
        Sandwiches are in a STACK.
        For each student in the queue, they look at the top of the stack, grab it if they like it.
        If they don't like it, they will go to the back of the queue.
        stack and queue implementation
        """
        
        studentsQueue = deque(students)
        sandwichesStack = sandwiches[::-1]
        
        numStudentsEaten = 0
        
        countPeoplePassingTopSandwich = 0
        
        while len(studentsQueue) and len(sandwichesStack):
            
            student = studentsQueue.popleft()
            sandwich = sandwichesStack[-1]

            if countPeoplePassingTopSandwich >= len(students):
                break

            if student == sandwich:
                sandwichesStack.pop(-1)
                numStudentsEaten += 1
                countPeoplePassingTopSandwich = 0
            else:
                studentsQueue.append(student)
                countPeoplePassingTopSandwich += 1
                
        return len(students) - numStudentsEaten
