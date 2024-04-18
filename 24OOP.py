class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Lion(Animal):
    def speak(self):
        return "Roar!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

lion = Lion("King", 5)
bird = Bird("JackSparrow", 2)

print(lion.speak())
print(bird.speak())
print ("========================")
class Animal2:
   def __init__(self, name2, age2, sound2):
      self.name2 = name2
      self.age2 = age2
