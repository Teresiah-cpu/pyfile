#Class is a blueprint of an object
#Object is an instance of a class
class Employee:
    def __init__(self,name,gender,position):
        self.name = name
        self.gender = gender
        self.position = position

    def movement(self):
        print("employee is walking")

#creating an object
employee1 = Employee("John","Male",1)
print(employee1.name, employee1.gender, employee1.position)

employee2 = Employee("Mary","Female",2)
print(employee2.name, employee2.gender, employee2.position)

employee3 = Employee("Jane","Female",3)
print(employee3.name, employee3.gender, employee3.position)

employee1.movement()
