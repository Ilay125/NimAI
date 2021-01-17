class Nim:
    def __init__(self, length):
        self.length = length

    def getMatches(self):
        return "|" * self.length

    def isValid(self, move):
        return move == 1 or (move == 2 and self.length >= 2)

    def updateMatches(self, move):
        if self.isValid(move):
            self.length -= move

    def compMove(self):
        if self.length >= 2:
            return 2
        return 1

    def isWinner(self):
        return self.length == 0
