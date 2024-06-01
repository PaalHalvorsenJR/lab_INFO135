class Employee:
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def get_fullname(self):
        print(f"{self.f_name} {self.l_name}")

    def print_email(self):
        print(f"{self.f_name}.{self.l_name}@company.com")

    def increase_salary(self, rate):
        new_salary = (self.salary * rate) + self.salary
        print(new_salary)
        

paal = Employee("paal", "halvorsen", 10000)

paal.get_fullname()
paal.print_email()
paal.increase_salary(0.03)