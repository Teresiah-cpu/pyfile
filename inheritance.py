class Animal:  #parent/super/base class

    isMammal = True
    gender = 'male'
    age = 2

    def movement(self):
        print("Animal is moving")

#child class/subclass/derived class
class Cow(Animal):
    def moow(self):
        print("Cow is mooing")

class Cat (Animal):
    def moow(self):
        print("Cat is mooing")
    def meow(self):
        print("Cat is meowing")

mycow = Cow()
mycow.moow()

mycat = Cat()
mycat.meow()