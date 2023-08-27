# 682. Baseball Game [Easy]

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
#     Record a new score of x.
# '+'.
#     Record a new score that is the sum of the previous two scores.
# 'D'.
#     Record a new score that is the double of the previous score.
# 'C'.
#     Invalidate the previous score, removing it from the record.
    
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0
        for i in range(len(operations)):
            if operations[i] == "+" and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            
            elif operations[i] == "C" and len(stack) != 0:
                stack.pop()
            
            elif operations[i] == "D" and len(stack) !=0:
                stack.append(stack[-1]*2)

            else:
                stack.append(int(operations[i]))
        
        return sum(stack)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# 20. Valid Parentheses [Easy]

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '(': ')', '[': ']'}
        
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack or brackets[stack.pop()] != char:
                return False
            
        return not stack
