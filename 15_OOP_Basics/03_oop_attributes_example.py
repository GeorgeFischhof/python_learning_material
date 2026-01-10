class Employee:
    employees = list()  # one shared list for all instances
    # class attribute, exist as a singleton, also can be accessed form instances

    def __init__(self, name: str):
        self.name = name

        # Instance delegates shared responsibility to the class
        type(self).add_employee_to_list(name)
        # type(self) is the current class without hardcoding it,
        # this works correctly even if Employee is subclassed later

    @classmethod
    def add_employee_to_list(cls, name: str):
        # We use a classmethod here because the list of employees belongs to the class,
        # not to any single employee

        cls.employees.append(name)
        # "cls" refers to the class (Employee) (convention only)
        # This method modifies shared (class-level) state


alex = Employee("Alex")
john = Employee("John")

print(f"{Employee.employees=}")
print(f"{alex.employees=}")
print(f"{john.employees=}")
# All three refer to the same singleton list
