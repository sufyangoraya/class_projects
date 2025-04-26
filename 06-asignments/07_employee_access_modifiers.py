class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public
        self._salary = salary      # protected
        self.__ssn = ssn            # private

# Example
emp = Employee("Ahmed", 50000, "123-45-6789")
print(emp.name)          # accessible
print(emp._salary)       # accessible (but not recommended)
# print(emp.__ssn)       # Error: private attribute
print(emp._Employee__ssn) # Accessing private using name mangling
