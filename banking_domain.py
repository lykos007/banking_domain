class Bank:
    def __init__(self, ifsc_code, bank_name, branch_name, location):
        self.IFSC_Code = ifsc_code
        self.bankname = bank_name
        self.branchname = branch_name
        self.loc = location

class Customer:
    def __init__(self, customer_id, cust_name, address, contact_details):
        self.CustomerID = customer_id
        self.custname = cust_name
        self.address = address
        self.contactdetails = contact_details

class Account(Bank):
    def __init__(self, ifsc_code, bank_name, branch_name, location, account_id, customer_obj, balance):
        super().__init__(ifsc_code, bank_name, branch_name, location)
        self.AccountID = account_id
        self.Cust = customer_obj
        self.balance = balance

    def getAccountInfo(self):
        print("Account Information:")
        print("Account ID:", self.AccountID)
        print("IFSC Code:", self.IFSC_Code)
        print("Bank Name:", self.bankname)
        print("Branch Name:", self.branchname)
        print("Location:", self.loc)
        print("Customer ID:", self.Cust.CustomerID)
        print("Customer Name:", self.Cust.custname)
        print("Customer Address:", self.Cust.address)
        print("Customer Contact Details:", self.Cust.contactdetails)
        print("Account Balance:", self.balance)

    def deposit(self, amount, is_savings):
        if is_savings == 'true':
            self.balance += amount
            print("Deposit Successful.")
        else:
            print("Invalid account type for deposit.")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    def getBalance(self):
        print("Current Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, ifsc_code, bank_name, branch_name, location, account_id, customer_obj, balance, min_balance):
        super().__init__(ifsc_code, bank_name, branch_name, location, account_id, customer_obj, balance)
        self.SMinBalance = min_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.SMinBalance:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance. Minimum Balance not maintained.")


class BankApplication:
    def run(self):
        print("Welcome to the Bank Application!")
        self.create_customer()
        self.create_account()
        self.perform_transactions()

    def create_customer(self):
        print("\nCreating Customer...")
        customer_id = input("Enter Customer ID: ")
        cust_name = input("Enter Customer Name: ")
        address = input("Enter Customer Address: ")
        contact_details = input("Enter Customer Contact Details: ")
        self.customer = Customer(customer_id, cust_name, address, contact_details)

    def create_account(self):
        print("\nCreating Account...")
        ifsc_code = input("Enter IFSC Code: ")
        bank_name = input("Enter Bank Name: ")
        branch_name = input("Enter Branch Name: ")
        location = input("Enter Location: ")
        account_id = input("Enter Account ID: ")
        balance = float(input("Enter Initial Balance: "))
        account_type = input("Enter Account Type (Savings or Checking): ")

        if account_type.lower() == 'savings':
            min_balance = float(input("Enter Minimum Balance for Savings Account: "))
            self.account = SavingsAccount(ifsc_code, bank_name, branch_name, location, account_id, self.customer, balance, min_balance)
        elif account_type.lower() == 'current':
            self.account = Account(ifsc_code, bank_name, branch_name, location, account_id, self.customer, balance)
        else:
            print("Invalid account type. Creating a normal Account.")
            self.account = Account(ifsc_code, bank_name, branch_name, location, account_id, self.customer, balance)

    def perform_transactions(self):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Get Account Information")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                is_savings = input("Is it a Savings Account? (true/false): ")
                self.account.deposit(amount, is_savings)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                self.account.withdraw(amount)
            elif choice == 3:
                self.account.getAccountInfo()
            elif choice == 4:
                print("Exiting Bank Application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bank_app = BankApplication()
    bank_app.run()
