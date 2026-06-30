class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, s):
        self.scores.append(s)
    
    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

student = Student("Hammad")
student.add_score(85)
student.add_score(90)
student.add_score(78)
student.add_score(68)

print(f"{student.name} average score: {student.average():.2f}")