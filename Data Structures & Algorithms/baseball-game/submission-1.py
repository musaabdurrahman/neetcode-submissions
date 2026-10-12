class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []
        for element in operations:
            if element == "+":
                record.append(record[-1]+record[-2])
            elif element == "D":
                record.append(2*record[-1])
            elif element == "C":
                record.pop()
            else:
                record.append(int(element))
        
        sum = 0
        for element in record:
            sum = sum + int(element)
        return sum