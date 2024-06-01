class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greets(self, other_person):
        print(f"{self.name}: Hello, {other_person.name} ")
    
alice = Person("Alice", 23)
bob = Person("Bob", 55) 

alice.greets(bob)
