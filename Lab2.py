class Car:
    def __init__(self, make, model, year, fuel_efficiency, speed):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_efficiency = fuel_efficiency
        self.speed = speed


class TaxiPark:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def calculate_fleet_cost(self):
        total_cost = sum(car.price for car in self.cars)
        return total_cost

    def sort_cars_by_fuel_efficiency(self):
        self.cars.sort(key=lambda x: x.fuel_efficiency)

    def find_car_by_speed_range(self, min_speed, max_speed):
        return [car for car in self.cars if min_speed <= car.speed <= max_speed]


# Примеры объектов
car1 = Car("Toyota", "Camry", 2022, 30, 120)
car2 = Car("Honda", "Civic", 2021, 35, 110)
car3 = Car("Ford", "Focus", 2020, 25, 130)

taxi_park = TaxiPark()
taxi_park.add_car(car1)
taxi_park.add_car(car2)
taxi_park.add_car(car3)

taxi_park.sort_cars_by_fuel_efficiency()
print([car.make for car in taxi_park.cars])

selected_cars = taxi_park.find_car_by_speed_range(110, 120)
print([car.model for car in selected_cars], '\n')


class MobilePlan:
    def __init__(self, name, data_limit, minutes, monthly_fee):
        self.name = name
        self.data_limit = data_limit
        self.minutes = minutes
        self.monthly_fee = monthly_fee


class MobileCompany:
    def __init__(self):
        self.plans = []

    def add_plan(self, plan):
        self.plans.append(plan)

    def calculate_total_customers(self):
        total_customers = sum(plan.customers for plan in self.plans)
        return total_customers

    def sort_plans_by_monthly_fee(self):
        self.plans.sort(key=lambda x: x.monthly_fee)

    def find_plan_by_data_range(self, min_data, max_data):
        return [plan for plan in self.plans if min_data <= plan.data_limit <= max_data]


# Примеры объектов
plan1 = MobilePlan("Basic Plan", 5, 100, 20)
plan2 = MobilePlan("Premium Plan", 10, 500, 40)
plan3 = MobilePlan("Ultra Plan", 20, 1000, 60)

mobile_company = MobileCompany()
mobile_company.add_plan(plan1)
mobile_company.add_plan(plan2)
mobile_company.add_plan(plan3)

mobile_company.sort_plans_by_monthly_fee()
print([plan.name for plan in mobile_company.plans])

selected_plans = mobile_company.find_plan_by_data_range(5, 15)
print([plan.name for plan in selected_plans], '\n')


class Coffee:
    def __init__(self, name, price, volume, state):
        self.name = name
        self.price = price
        self.volume = volume
        self.state = state


class CoffeeVan:
    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.coffees = []

    def add_coffee(self, coffee):
        if self.budget >= coffee.price and self.capacity >= coffee.volume:
            self.coffees.append(coffee)
            self.budget -= coffee.price
            self.capacity -= coffee.volume

    def sort_coffees_by_value(self):
        self.coffees.sort(key=lambda x: x.price / x.volume, reverse=True)

    def find_coffee_by_quality_range(self, min_quality, max_quality):
        return [coffee for coffee in self.coffees if min_quality <= coffee.state <= max_quality]


# Примеры объектов
coffee1 = Coffee("Arabica", 10, 0.5, 1)
coffee2 = Coffee("Robusta", 8, 0.6, 2)
coffee3 = Coffee("Instant", 5, 0.4, 3)

coffee_van = CoffeeVan(2, 15)
coffee_van.add_coffee(coffee1)
coffee_van.add_coffee(coffee2)
coffee_van.add_coffee(coffee3)

coffee_van.sort_coffees_by_value()
print([coffee.name for coffee in coffee_van.coffees])

selected_coffees = coffee_van.find_coffee_by_quality_range(1, 2)
print([coffee.name for coffee in selected_coffees], '\n')


class Toy:
    def __init__(self, name, category, size):
        self.name = name
        self.category = category
        self.size = size


class GameRoom:
    def __init__(self, budget):
        self.budget = budget
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

    def sort_toys_by_size(self):
        self.toys.sort(key=lambda x: x.size)

    def find_toys_by_size_range(self, min_size, max_size):
        return [toy for toy in self.toys if min_size <= toy.size <= max_size]


# Примеры объектов
toy1 = Toy("Car", "Small", 5)
toy2 = Toy("Doll", "Medium", 3)
toy3 = Toy("Ball", "Large", 7)

game_room = GameRoom(15)
game_room.add_toy(toy1)
game_room.add_toy(toy2)
game_room.add_toy(toy3)

game_room.sort_toys_by_size()
print([toy.name for toy in game_room.toys])

selected_toys = game_room.find_toys_by_size_range(4, 6)
print([toy.name for toy in selected_toys], '\n')


class Tax:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount


class TaxPayer:
    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.taxes = []

    def add_tax(self, tax):
        self.taxes.append(tax)

    def calculate_total_taxes(self):
        total_taxes = sum(tax.amount for tax in self.taxes)
        return total_taxes

    def sort_taxes_by_amount(self):
        self.taxes.sort(key=lambda x: x.amount)

    def find_taxes_by_amount_range(self, min_amount, max_amount):
        return [tax for tax in self.taxes if min_amount <= tax.amount <= max_amount]


# Примеры объектов
tax1 = Tax("Income", 5000)
tax2 = Tax("Property", 200)
tax3 = Tax("Gift", 1000)

taxpayer = TaxPayer("John Doe", 15000)
taxpayer.add_tax(tax1)
taxpayer.add_tax(tax2)
taxpayer.add_tax(tax3)

taxpayer.sort_taxes_by_amount()
print([tax.source for tax in taxpayer.taxes])

selected_taxes = taxpayer.find_taxes_by_amount_range(500, 1500)
print([tax.source for tax in selected_taxes], '\n')


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.is_blocked = False

    def block_account(self):
        self.is_blocked = True

    def unblock_account(self):
        self.is_blocked = False


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def calculate_total_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        return total_balance

    def calculate_positive_negative_balance(self):
        positive_balance = sum(account.balance for account in self.accounts if account.balance > 0)
        negative_balance = sum(account.balance for account in self.accounts if account.balance < 0)
        return positive_balance, negative_balance


# Примеры объектов
account1 = BankAccount("12345", 5000)
account2 = BankAccount("67890", -2000)
account3 = BankAccount("54321", 10000)

bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)

total_balance = bank.calculate_total_balance()
print(f"Total balance: {total_balance}")

positive_balance, negative_balance = bank.calculate_positive_negative_balance()
print(f"Positive balance: {positive_balance}, Negative balance: {negative_balance}\n")


class TourPackage:
    def __init__(self, name, package_type, transport, meals, days, price):
        self.name = name
        self.package_type = package_type
        self.transport = transport
        self.meals = meals
        self.days = days
        self.price = price


class TravelAgency:
    def __init__(self):
        self.packages = []

    def add_package(self, package):
        self.packages.append(package)

    def sort_packages_by_price(self):
        self.packages.sort(key=lambda x: x.price)

    def find_packages_by_criteria(self, criteria):
        return [package for package in self.packages if criteria(package)]


# Примеры объектов
package1 = TourPackage("Beach Vacation", "Relaxation", "Flight", "All-Inclusive", 7, 1500)
package2 = TourPackage("City Tour", "Sightseeing", "Bus", "Breakfast", 5, 800)
package3 = TourPackage("Mountain Adventure", "Adventure", "Hiking", "No Meals", 10, 1200)

travel_agency = TravelAgency()
travel_agency.add_package(package1)
travel_agency.add_package(package2)
travel_agency.add_package(package3)

travel_agency.sort_packages_by_price()
print([package.name for package in travel_agency.packages])

selected_packages = travel_agency.find_packages_by_criteria(lambda x: x.price <= 1000 and x.days >= 7)
print([package.name for package in selected_packages], '\n')


class Loan:
    def __init__(self, bank, loan_type, interest_rate, max_amount):
        self.bank = bank
        self.loan_type = loan_type
        self.interest_rate = interest_rate
        self.max_amount = max_amount


class Bank:
    def __init__(self, name):
        self.name = name
        self.loans = []

    def add_loan(self, loan):
        self.loans.append(loan)

    def find_loan(self, loan_type):
        return next((loan for loan in self.loans if loan.loan_type == loan_type), None)


# Примеры объектов
loan1 = Loan("Bank A", "Home Loan", 5.0, 50000)
loan2 = Loan("Bank B", "Auto Loan", 4.5, 25000)
loan3 = Loan("Bank C", "Personal Loan", 6.0, 10000)

bank_a = Bank("Bank A")
bank_a.add_loan(loan1)

bank_b = Bank("Bank B")
bank_b.add_loan(loan2)

bank_c = Bank("Bank C")
bank_c.add_loan(loan3)

selected_loan = bank_a.find_loan("Home Loan")
print(f"{selected_loan.bank}: {selected_loan.loan_type}, Interest Rate: {selected_loan.interest_rate}\n")


class InsurancePolicy:
    def __init__(self, policy_type, coverage_amount, premium):
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
        self.premium = premium


class InsuranceDerivative:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def calculate_total_premium(self):
        total_premium = sum(policy.premium for policy in self.policies)
        return total_premium

    def sort_policies_by_risk_reduction(self):
        self.policies.sort(key=lambda x: x.coverage_amount)

    def find_policy_by_criteria(self, criteria):
        return [policy for policy in self.policies if criteria(policy)]


# Примеры объектов
policy1 = InsurancePolicy("Life Insurance", 100000, 1000)
policy2 = InsurancePolicy("Auto Insurance", 50000, 500)
policy3 = InsurancePolicy("Home Insurance", 200000, 1500)

insurance_derivative = InsuranceDerivative()
insurance_derivative.add_policy(policy1)
insurance_derivative.add_policy(policy2)
insurance_derivative.add_policy(policy3)

total_premium = insurance_derivative.calculate_total_premium()
print(f"Total Premium: {total_premium}")

insurance_derivative.sort_policies_by_risk_reduction()
print([policy.policy_type for policy in insurance_derivative.policies])

selected_policies = insurance_derivative.find_policy_by_criteria(lambda x: x.coverage_amount >= 50000)
print([policy.policy_type for policy in selected_policies])
