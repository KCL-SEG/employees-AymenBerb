"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from calendar import monthcalendar


class Employee:
    def __init__(self, name, contractType, bonusType) -> None:
        self.name = name
        self.contractType = contractType
        self.bonusType = bonusType
    
    def get_pay(self) -> int:
        salary = self.contractType.get_pay()

        if self.bonusType:
            salary += self.bonusType.get_bonus()

        return salary

    def __str__(self) -> str:
        if self.bonusType:
            return self.name + " works on a " + self.contractType.get_string() + self.bonusType.get_string() + ".  Their total pay is " + str(Employee.get_pay(self)) + "."
        else:
            return self.name + " works on a " + self.contractType.get_string() + ".  Their total pay is " + str(Employee.get_pay(self)) + "."


class Contract:
    def __init__(self) -> None:
        pass

class MonthlyContract(Contract):
    def __init__(self, salary) -> None:
        super().__init__()
        self.salary = salary

    def get_pay(self) -> int:
        return self.salary

    def get_string(self):
        return "monthly salary of " + str(self.get_pay())

class HourlyContract(Contract):
    def __init__(self, hourlyWage, hoursWorked) -> None:
        super().__init__()
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked
    
    def get_pay(self) -> int:
        return self.hourlyWage * self.hoursWorked
    
    def get_string(self):
        return "contract of " + str(self.hoursWorked) + " hours at " + str(self.hourlyWage) + "/hour"


class Bonus:
    def __init__(self) -> None:
        pass

class FixedBonus(Bonus):
    def __init__(self, fixedAmount) -> None:
        super().__init__()
        self.fixedAmount = fixedAmount
    
    def get_bonus(self):
        return self.fixedAmount
    
    def get_string(self):
        return " and receives a bonus commission of " + str(self.fixedAmount)


class VariableBonus(Bonus):
    def __init__(self, commissionPerContract, numOfContract) -> None:
        super().__init__()
        self.commissionPerContract = commissionPerContract
        self.numOfContract = numOfContract

    def get_bonus(self):
        return self.commissionPerContract * self.numOfContract
    
    def get_string(self):
        return " and receives a commission for " + str(self.numOfContract) + " contract(s) at " + str(self.commissionPerContract) + "/contract"


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000), None)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100), None)
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), VariableBonus(200, 4))
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), VariableBonus(220, 3))
print(str(jan))
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), FixedBonus(1500))
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), FixedBonus(600))
print(str(ariel))
