class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, *scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores[0]

    def calculate(self):
        grade = sum(self.scores)/len(self.scores)
        
        if grade <= 100 and grade >= 90:
            return 'O'
        elif grade < 90 and grade >= 80:
            return 'E'
        elif grade < 80 and grade >= 70:
            return 'A'
        elif grade < 70 and grade >= 55:
            return 'P'
        elif grade < 55 and grade >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()