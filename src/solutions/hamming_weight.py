class Solution:
    def hammingWeight(self, n: int) -> int:
        answerSum = 0
        for val in bin(n)[2:]:
            if int(val):
                answerSum += 1
        return answerSum
