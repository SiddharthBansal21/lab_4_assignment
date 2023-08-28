class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter.")

    def display_employees(self):
        for employee in self.employees:
            print(employee)

if __name__ == "__main__":
    employee_db = EmployeeDatabase()

    employee_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Sort by:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice: "))
    
    employee_db.sort_employees(choice)
    employee_db.display_employees()
