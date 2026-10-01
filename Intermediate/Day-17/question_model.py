class Question:

    #initialize question class
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer

    def getText(self):
        return self.text

    def getAnswer(self):
        return self.answer