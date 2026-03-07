
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_email(cls, email):
        name = email.split("@")[0]
        return cls(name)

p = Person.from_email("aju@test.com")

print(p)
print(p.__class__)
print(p.__dict__)
print(p.name)