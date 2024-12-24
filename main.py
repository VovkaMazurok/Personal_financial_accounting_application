from datetime import datetime
import pathlib

class DataBalance:
    def __init__(self, balance, file):
        self.balance = balance
        self.file = file

    @staticmethod
    def get_balance(file):
        """Метод для отримання балансу з файлу"""
        parent_directory = pathlib.Path(__file__).resolve().parent
        open_file = parent_directory.joinpath(file)
        return open_file.read_text()

    @staticmethod
    def update_file_balance(balance, file="balance.txt"):
        """Метод для оновлення балансу в файлі"""
        parent_directory = pathlib.Path(__file__).resolve().parent
        open_file = parent_directory.joinpath(file)
        open_file.write_text(str(balance))
        print(f'Your balance is: {balance}')
        print('----------------------------------------')


class AccountTransactions:
    def __init__(self, data, sum_transaction, name_transaction):
        self.data = data


    @staticmethod
    def transaction_record(data, file="account_info.csv"):
        """Метод для запису транзакцій в файл"""
        parent_directory = pathlib.Path(__file__).resolve().parent
        open_file = parent_directory.joinpath(file)
        with open_file.open("a", encoding="utf-8") as f:
            f.write(data + "\n")

    @staticmethod
    def log_transaction(operation_type, sum_transaction, name_transaction, file="account_info.csv"):
        """Логування однієї транзакцію з записом у файл."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction_record = f"{timestamp} | {operation_type}: {sum_transaction} - {name_transaction}"
        AccountTransactions.transaction_record(transaction_record, file)


class BalanceOperations:

    def __init__(self, sum_transaction, my_balance):
        self.sum_transaction = sum_transaction
        self.my_balance = my_balance
    @staticmethod
    def add(sum_transaction, my_balance):
        """Метод для додавання суми транзакції до балансу"""
        return sum_transaction + my_balance

    @staticmethod
    def sub(sum_transaction, my_balance):
        """Метод для віднімання суми транзакції від балансу"""
        return sum_transaction - my_balance


class UserInterface:

    @staticmethod
    def display_menu():
        print("Select an operation:\n1-transaction\n2-balance statement\n3-transaction histori\n4-Exit")
    @staticmethod
    def get_user_choice():
        try:
            choice = int(input('Enter a choice: \n'))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, 3 or 4).")
            return None

    @staticmethod
    def select_transaction_type():
        try:
            operation = int(input('Select an operation:\n1-receipt\n2-debit\nEnter a number: \n'))
            if operation not in [1, 2]:
                raise ValueError
            return operation
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            return None


def main():

    while True:
        UserInterface.display_menu()
        choice = UserInterface.get_user_choice()
        if choice is None:
            continue

        if choice == 1:
            my_balance = DataBalance.get_balance(file="balance.txt")



            operation = UserInterface.select_transaction_type()
            sum_transaction = int(input("Enter the sum: "))
            name_transaction = input("Enter the name of the transaction: ")
            if operation is None:
                continue

            if operation == 1:
                new_balance = BalanceOperations.add(int(my_balance), sum_transaction)
                AccountTransactions.log_transaction("receipt", sum_transaction, name_transaction)

            elif operation == 2:
                new_balance = BalanceOperations.sub(int(my_balance), sum_transaction)
                AccountTransactions.log_transaction("debit", sum_transaction, name_transaction)
            DataBalance.update_file_balance(new_balance)

        elif choice == 2:
            print(f'Your balance is: {DataBalance.get_balance(file="balance.txt")}')
            print('----------------------------------------')

        elif choice == 3:
            print(f'Your transaction is:\n{DataBalance.get_balance(file="account_info.csv")}\n')
            print('----------------------------------------')

        elif choice == 4:
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
