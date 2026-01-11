# 🏦 ATM Management System using Python & MySQL

A **console-based ATM application** developed using **Python** and **MySQL**, simulating real ATM operations such as balance inquiry, deposit, withdrawal, mini statement, and PIN change with secure database handling.

---

## 📌 Features

- 🔐 Secure Login using Account Number & PIN  
- 💰 Check Account Balance  
- ➕ Deposit Money  
- ➖ Withdraw Money (with balance validation)  
- 📄 Mini Statement (last 5 transactions)  
- 🔑 Change ATM PIN  
- 🗄️ MySQL Database Integration  
- 🧾 Transaction History Storage  

---

## 🛠️ Technologies Used

- **Python 3**
- **MySQL**
- **mysql-connector-python**
- **SQL**

---

## 🗂️ Database Structure

### 📋 `users` Table
```sql
CREATE TABLE users (
    accnumber VARCHAR(20) PRIMARY KEY,
    pin VARCHAR(10),
    balance DOUBLE
);

📋 transactions Table
sql
Copy code
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    accnumber VARCHAR(20),
    transaction_type VARCHAR(20),
    amount DOUBLE,
    trans_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

⚙️ Installation & Setup

1️⃣ Install Required Package
bash
Copy code
pip install mysql-connector-python

2️⃣ Configure Database
Create a database named atm_db

Create users and transactions tables

Insert sample user data

sql
Copy code
INSERT INTO users VALUES ('7315262049', '242506', 10000);
3️⃣ Update Database Credentials
Edit these values in the Python file if needed:

python
Copy code
host="localhost"
user="root"
password="2452"
database="atm_db"
▶️ How to Run
bash
Copy code
python atm.py
Follow on-screen instructions to operate the ATM system.

📸 Sample Operations
Login Authentication

Deposit & Withdraw with real-time balance update

Mini Statement showing last 5 transactions

Secure PIN change

🚀 Future Enhancements
🔐 Password hashing for PIN security

🖥️ GUI using Tkinter or Web App with Flask

📊 Full transaction history view

👥 Admin panel for account management

👨‍💻 Author
Rubeshkanna Ravichandran
📊 Data Analyst Student
🐍 Python | 🗄️ MySQL | 📈 Power BI
