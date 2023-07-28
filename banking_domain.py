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


if __name__ == "__main__":
    # Create a Customer object
    customer1 = Customer("C1001", "John Doe", "123 Main Street", "john.doe@example.com")

    # Create an Account object
    account1 = Account("IFSC123", "MyBank", "MainBranch", "New York", "A12345", customer1, 5000)

    # Get Account Information
    account1.getAccountInfo()

    # Deposit
    account1.deposit(2000, 'true')

    # Withdraw
    account1.withdraw(500)

    # Get Balance
    account1.getBalance()

    # Create a SavingsAccount object
    savings_account1 = SavingsAccount("IFSC456", "MyBank", "Branch2", "Chicago", "A67890", customer1, 3000, 1000)

    # Get Savings Account Information
    savings_account1.getAccountInfo()

    # Deposit into Savings Account
    savings_account1.deposit(2000, 'true')

    # Withdraw from Savings Account
    savings_account1.withdraw(500)

    # Get Savings Account Balance
    savings_account1.getBalance()
