__author__ = 'SebastianA'

class CPRGenerator:

    def __init__(self, DateOfBirth, Gender):
        self.dateOfBirth = DateOfBirth
        self.gender = Gender

        self.CPRPossibilites = [[1, 2, 3, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.CPRList = []


    def searchCPRPossibilities(self, depth = 0, partialCPR = ""):

        if self.gender is "Male":
            self.CPRPossibilites[3] = [1, 3, 5, 7, 9]
        elif self.gender is "Female":
            self.CPRPossibilites[3] = [0, 2, 4, 6, 8]

        for i in self.CPRPossibilites[depth]:

            if depth < 3:
                nextPartialCPR = str(partialCPR) + "" + str(self.CPRPossibilites[depth][i])
                nextDepth = depth + 1
                self.searchCPRPossibilities(nextDepth, nextPartialCPR)
            else:
                validCPR = str(partialCPR) + "" + str(self.CPRPossibilites[2][i])

                if self.isCPRValid(validCPR):
                    self.CPRList.append(self.dateOfBirth + "-" + validCPR)

        return self.CPRList

    def isCPRValid(self, CPR):
        fullCPR = self.dateOfBirth + CPR
        factors = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
        return sum(int(digit) * factor for digit, factor in zip(fullCPR, factors)) % 11 == 0


print(CPRGenerator("240788", "Male").searchCPRPossibilities())
