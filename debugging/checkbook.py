#!/usr/bin/python3

class Checkbook:
    """
    Function description:
        A simple checkbook that tracks a balance and supports deposits,
        withdrawals, and displaying the current balance.

    Parameters:
        None (balance starts at 0.0)

    Returns:
        None
    """

    def __init__(self):
        """
        Function description:
            Initialize a new checkbook with a balance of 0.0.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
            Add money to the balance and display the updated balance.

        Parameters:
            amount (float): The amount of money to add (should be >= 0).

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
            Remove money from the balance if sufficient funds exist,
            and display the updated balance.

        Parameters:
            amount (float): The amount of money to withdraw (should be >= 0).

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
            Print the current balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def read_amount(prompt):
    """
    Function description:
        Read a monetary amount from user input safely.
        Keeps asking until the user enters a valid number.

    Parameters:
        prompt (str): The prompt shown to the user.

    Returns:
        float: A valid numeric amount entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value (e.g., 10 or 10.50).")


def main():
    """
    Function description:
        Run the interactive checkbook program. The user can deposit,
        withdraw, display balance, or exit.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            amount = read_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = read_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
