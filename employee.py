"""
Creating Employee classes for employee,
developers, and Managers
"""


class Employee:
    """Employee class"""
    no_of_employees = 0
    raise_pay = 1.04

    def __init__(self, first, last, role, pay, expertise=None,):
        """
        Initialize the employee class
        """
        self.first = first
        self.last = last
        self.role = role
        self.expertise = expertise
        self.pay = pay
        self.name = first + ' ' + last
        Employee.no_of_employees += 1

    def email(self):
        """
        Create employee's email address
        """
        return f"{self.first}.{self.last}@company.com"

    def full_name(self):
        """
        Get employee's full name
        """
        return self.first.upper() + ' ' + self.last.upper()

    def apply_raise(self):
        """
        Apply pay raise to an employee
        """
        self.pay = self.raise_pay * self.pay

    # create a class method to increase the raise amount
    @classmethod
    def pay_raise(cls, amt):
        """
        Increase the raise amount
        """
        cls.raise_pay = amt

    def __str__(self):
        """
        modify str to return the employee and employee's email
        """
        return f"{self.full_name()} - {self.email()}"


class Manager(Employee):
    """
    Manager class that can also add and
    remove employees
    """

    def __init__(self, first, last, pay, role="Manager", employees=None):
        """
        Manager inherits from the Employee class
        and adds any employees if any
        """
        super().__init__(first, last, role, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


class Developer(Employee):
    """
    Developers calss to create programmer
    employees
    """

    def __init__(self, first, last, role, pay, language):
        """
        Developer class inherits from the Employee class
        """
        super().__init__(first, last, role, pay)
        self.expertise = language
