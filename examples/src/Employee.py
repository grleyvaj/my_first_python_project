class Employee:

    # definir e inicializar los atributos q va a tener la clase
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def get_salary(self) -> int:
        return self.salary


emp = Employee("Gloria", 100)
print(emp.name)
print(emp.salary)
