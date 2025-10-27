def atm(accnumber, accpin):
    tries = 0
    transactions = []
    balance = 10000.0
    current_pin = "242506"

    while tries < 2:
        if accnumber == "7315262049" and accpin == current_pin:
            print("Successfully logged in")

            while True:
                print("1. Account Balance")
                print("2. Deposit Money")
                print("3. Withdraw")
                print("4. Mini Statement")
                print("5. Change PIN")
                print("6. Exit")

                choice = input("Enter choice: ")

                if choice == "1":
                    print("Your balance is:", balance)

                elif choice == "2":
                    amount = input("Enter deposit amount: ")
                    if amount.isdigit():
                        amount = int(amount)
                        balance += amount
                        transactions.append("Deposited " + str(amount))
                        print("Deposited", amount)
                        print("Your balance is:", balance)
                    else:
                        print("Invalid amount")

                elif choice == "3":
                    amount = input("Enter withdraw amount: ")
                    if amount.isdigit():
                        amount = int(amount)
                        if amount <= balance:
                            balance -= amount
                            transactions.append("Withdraw " + str(amount))
                            print("Withdrawn", amount)
                            print("Your balance is:", balance)
                        else:
                            print("Insufficient balance")
                    else:
                        print("Invalid amount")

                elif choice == "4":
                    print("Mini Statement")
                    if transactions:
                        for t in transactions[-5:]:
                            print(t)
                    else:
                        print("No transactions yet")

                elif choice == "5":
                    pin = input("Enter current PIN: ")
                    if pin == current_pin:
                        new_pin = input("Enter new PIN: ")
                        confirm = input("Confirm new PIN: ")
                        if new_pin == current_pin:
                             print("PIN already exists.")
                        if new_pin == confirm:
                            current_pin = new_pin
                            print("PIN successfully changed")
                        else:
                            print("PINs do not match.")
                    else:
                        print("Invalid")

                elif choice == "6":
                    print("Thank you for transactions")
                    return

                else:
                    print("Invalid choice")

            break  

        else:
            print("user invalid")
            accnumber=input("Enter accnumber again: ")  
            accpin = input("Enter pin again: ")  
            tries += 2

    else:
        print("Login failed")


def va():
    print("Welcome to ATM")
    accnumber = input("Enter Account Number: ")
    accpin = input("Enter PIN: ")
    atm(accnumber, accpin)


va()
