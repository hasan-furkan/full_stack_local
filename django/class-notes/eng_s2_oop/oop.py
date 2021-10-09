import os
os.system('cls' if os.name == 'nt' else 'clear')


def printtype(data):
    for i in data:
        print(i, type(i))


test = [123, 'Henry', [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x: x]
# printtype(test)

# defining classes


# class Person:
#     name = 'Barry'
#     age = 44


# # making instance
# person1 = Person()
# person2 = Person()

# # print(person1.name)
# # print(person2.name)

# Person.job = 'teacher'

# # print(person1.job)

# # class attributes ve instance attributes
# Person.name = 'Victor'
# person1.name = 'Rafe'

# person2.salary = 5000
# print(person1.name)
# print(person2.name)
# print(person2.salary)

# # SELF keyword
# class Person:
#     name = 'Barry'
#     age = 44

#     def test(self):
#         print('test')

#     def get_details(self):
#         print('name: ', self.name, 'age: ',
#               self.age, 'location :', self.location)

#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location


# person1 = Person()
# person1.test()
# # Person.test(person1)
# person1.set_details('Henry', 39, 'Ankara')
# person1.get_details()

# Static Method

class Person:
    name = 'Barry'
    age = 44

    def get_details(self):
        print('name: ', self.name, 'age: ',
              self.age, 'location :', self.location)

    def set_details(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
