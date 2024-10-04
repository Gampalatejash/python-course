class animal:
    def sound(self):
        return 'some sound'
class dog(animal):
    def high(self):
        return 'bow'
class bulldog(dog):
    def breed(self):
        return 'bow bow'

b=bulldog()
print(b.sound())

    
print(b.high())
print(b.breed())