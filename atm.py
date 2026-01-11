import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="2452",  
    database="atm_db"
)

cursor = db.cursor()


def atm(accnumber, accpin):
    tries = 0

    while tries < 3:
        cursor.execute(
            "SELECT pin, balance FROM users WHERE accnumber=%s",
            (accnumber,)
        )
        user = cursor.fetchone()

        if user and accpin == user[0]:
            print("\n✅ Successfully logged in")

            while True:
                print("\n1. Account Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Mini Statement")
                print("5. Change PIN")
                print("6. Exit")

                choice = input("Enter choice: ")

                # 1️⃣ Balance
                if choice == "1":
                    cursor.execute(
                        "SELECT balance FROM users WHERE accnumber=%s",
                        (accnumber,)
                    )
                    balance = cursor.fetchone()[0]
                    print("💰 Balance:", balance)

                # 2️⃣ Deposit
                elif choice == "2":
                    amount = input("Enter deposit amount: ")
                    if amount.isdigit():
                        amount = float(amount)
                        cursor.execute(
                            "UPDATE users SET balance = balance + %s WHERE accnumber=%s",
                            (amount, accnumber)
                        )
                        cursor.execute(
                            "INSERT INTO transactions (accnumber, transaction_type, amount) VALUES (%s,%s,%s)",
                            (accnumber, "Deposit", amount)
                        )
                        db.commit()
                        print("✅ Deposited:", amount)
                    else:
                        print("❌ Invalid amount")

                # 3️⃣ Withdraw
                elif choice == "3":
                    amount = input("Enter withdraw amount: ")
                    if amount.isdigit():
                        amount = float(amount)
                        cursor.execute(
                            "SELECT balance FROM users WHERE accnumber=%s",
                            (accnumber,)
                        )
                        balance = cursor.fetchone()[0]

                        if amount <= balance:
                            cursor.execute(
                                "UPDATE users SET balance = balance - %s WHERE accnumber=%s",
                                (amount, accnumber)
                            )
                            cursor.execute(
                                "INSERT INTO transactions (accnumber, transaction_type, amount) VALUES (%s,%s,%s)",
                                (accnumber, "Withdraw", amount)
                            )
                            db.commit()
                            print("✅ Withdrawn:", amount)
                        else:
                            print("❌ Insufficient balance")
                    else:
                        print("❌ Invalid amount")

                # 4️⃣ Mini Statement
                elif choice == "4":
                    print("\n📄 Mini Statement")
                    cursor.execute(
                        "SELECT transaction_type, amount, trans_time FROM transactions WHERE accnumber=%s ORDER BY id DESC LIMIT 5",
                        (accnumber,)
                    )
                    records = cursor.fetchall()
                    if records:
                        for r in records:
                            print(r)
                    else:
                        print("No transactions yet")

                # 5️⃣ Change PIN
                elif choice == "5":
                    old_pin = input("Enter current PIN: ")
                    if old_pin == accpin:
                        new_pin = input("Enter new PIN: ")
                        confirm = input("Confirm new PIN: ")
                        if new_pin == confirm:
                            cursor.execute(
                                "UPDATE users SET pin=%s WHERE accnumber=%s",
                                (new_pin, accnumber)
                            )
                            db.commit()
                            accpin = new_pin
                            print("✅ PIN changed successfully")
                        else:
                            print("❌ PIN mismatch")
                    else:
                        print("❌ Wrong PIN")

                # 6️⃣ Exit
                elif choice == "6":
                    print("🙏 Thank you for using ATM")
                    return

                else:
                    print("❌ Invalid choice")

        else:
            print("❌ Invalid account or PIN")
            accnumber = input("Enter Account Number again: ")
            accpin = input("Enter PIN again: ")
            tries += 1

    print("🚫 Login failed")


def va():
    print("🏦 Welcome to ATM")
    accnumber = input("Enter Account Number: ")
    accpin = input("Enter PIN: ")
    atm(accnumber, accpin)

va()
