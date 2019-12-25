import sys

import requests


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


# you have to run this code in Terminal, using right click and select "Run python file in Terminal"
firstName = input("First Name?")
lastName = input("Last Name?")

emp_1 = Employee(firstName, lastName, 120000)
# emp_2 = Employee("Aarib", "Habib", 120000)

print(emp_1.email)
# print(emp_2.email)


# print(sys.version)
# print(sys.executable)

# r = requests.get("https://www.mtpeter.com/tubing")
# print(f"Status Code: {r.status_code}")

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))
