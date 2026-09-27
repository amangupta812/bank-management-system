# 🏦 Bank Management System

A modular **Bank Management System built with Python, SQLite, and Tkinter**. The application provides customer management, bank account operations, deposits, withdrawals, transfers, transaction history, and role-based authentication through Admin and Customer dashboards.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- Admin and Customer login
- Password hashing using SHA-256
- Role-based access
- Customer login linked to the corresponding customer record
- Separate Admin and Customer dashboards
- Default Admin account for the demo version

### 👤 Customer Management
- Register new customers
- Automatically generate Customer IDs
- Store customer information
- Connect customers with authentication credentials

### 💳 Account Management
- Create bank accounts
- Automatically generate Account Numbers
- Support for Savings and Current accounts
- Initial account deposit
- Balance management

### 💰 Banking Operations
- Deposit money
- Withdraw money
- Check account balance
- Transfer money between accounts
- Insufficient-balance protection

### 📋 Transaction History
- Record deposits
- Record withdrawals
- Record transfers
- Record initial account deposits
- View transaction history
- Display transactions using Tkinter `Treeview`

### 🔄 Database Transactions
- Commit successful operations
- Roll back failed operations
- Keep account balance and transaction records consistent
- Record both sides of account transfers

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| SQLite | Relational database |
| Tkinter | Desktop GUI |
| hashlib | Password hashing |
| Git | Version control |
| GitHub | Source code hosting |

The project primarily uses Python's standard library, keeping the application lightweight and easy to run.

---

# 📚 Development Phases

The project was developed incrementally instead of building everything inside a single Python file.

---

## Phase 1 — Project Foundation

The first phase established the basic structure of the Bank Management System.

### Implemented

- Python project structure
- SQLite database connection
- Database initialization
- Basic customer management
- Modular separation of functionality

Initial architecture:

```text
bank-management-system/
│
├── main.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── customers/
│   ├── __init__.py
│   └── customer.py
│
└── accounts/
    ├── __init__.py
    └── account.py
```

---

## Phase 2 — Customer Management

The second phase expanded customer functionality.

### Implemented

- Customer registration
- Customer information storage
- Automatic Customer ID generation
- Input validation
- Database error handling

Customer records are stored separately from bank account records so that one customer can later be associated with banking accounts.

---

## Phase 3 — Bank Account Management

The third phase introduced actual bank accounts.

### Implemented

- Bank account creation
- Automatic Account Number generation
- Savings account support
- Current account support
- Initial deposit
- Account balance storage
- Customer-to-account relationship

The basic relationship became:

```text
Customer
   │
   └── Bank Account
          │
          └── Balance
```

---

## Phase 4 — Banking Transactions

The fourth phase introduced the core banking operations.

### Implemented

#### Deposit

```text
Account Balance
      +
Deposit Amount
      ↓
New Balance
```

#### Withdrawal

```text
Account Balance
      -
Withdrawal Amount
      ↓
New Balance
```

The system also validates that a withdrawal cannot exceed the available account balance.

#### Account-to-Account Transfer

```text
Account A
   │
   │ ₹ Amount
   ↓
Account B
```

Transfers update both accounts and record the corresponding transaction information.

---

## Phase 5 — Transaction History

Phase 5 introduced transaction tracking.

The system records:

- Deposits
- Withdrawals
- Transfers
- Initial account deposits

A transaction contains information such as:

```text
Transaction ID
Transaction Type
Amount
Transaction Date
Description
Account Number
```

### Transaction History Example

```text
ID    Type          Amount       Description
---------------------------------------------------------
4     Transfer      ₹2500.00     Transfer to account 100002
3     Withdrawal    ₹1500.00     Cash withdrawal
2     Deposit       ₹2000.00     Cash deposit
1     Deposit       ₹5000.00     Initial account deposit
```

Transactions can be displayed through a Tkinter `Treeview`.

### Initial Deposit Consistency

When an account is created with an initial deposit, that deposit is also recorded as a transaction.

```text
Create Account
      │
      ├── accounts table
      │       balance = ₹5000
      │
      └── transactions table
              Deposit = ₹5000
```

This keeps the account balance and transaction history consistent.

---

# 🔐 Phase 6 — Authentication & Role-Based Dashboards

Phase 6 introduced the authentication and access-control layer.

The application no longer starts directly inside the banking interface.

Instead:

```text
                    BANK MANAGEMENT SYSTEM
                             │
                             ▼
                       LOGIN SCREEN
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
             ADMIN                    CUSTOMER
                │                         │
                ▼                         ▼
       ADMIN DASHBOARD          CUSTOMER DASHBOARD
```

The goal of this phase was to introduce authenticated users and separate access levels.

---

## Phase 6.1 — Users Table

A new `users` table was introduced.

```text
users
--------------------------------
user_id
username
password_hash
role
customer_id
```

Example:

```text
1 | admin | <hashed password> | admin    | NULL
2 | aman  | <hashed password> | customer | 1
3 | john  | <hashed password> | customer | 2
```

The `customer_id` connects a customer login with the corresponding customer record.

This allows the system to determine which customer is currently logged in.

---

## Phase 6.2 — Password Hashing

Passwords are not stored directly as plain text.

The authentication layer converts a password into a hash before storing it.

```text
Password
   │
   ▼
SHA-256
   │
   ▼
Password Hash
   │
   ▼
Database
```

The authentication module provides:

```python
hash_password()
create_user()
login()
```

This introduces an important security concept while keeping the implementation lightweight for an educational project.

---

## Phase 6.3 — Default Admin Account

The application creates a default administrator account if one does not already exist.

Demo credentials:

```text
Username: admin
Password: admin123
Role:     admin
```

This is intended only for the student/demo version. A production implementation should use secure, configurable credentials instead of hard-coded credentials.

---

## Phase 6.4 — Customer Login Credentials

Customer registration was extended to include:

```text
Name
Phone
Address
Date of Birth
Username
Password
```

The customer and user records are connected:

```text
Register Customer
       │
       ├───────────────┐
       ▼               ▼
 customers table    users table
       │               │
       └────customer_id┘
```

Both database operations are committed together so that a failed user creation does not leave an incomplete customer record.

---

## Phase 6.5 — Login Interface

A dedicated login window was introduced.

```text
┌────────────────────────────────────┐
│      BANK MANAGEMENT SYSTEM        │
│                                    │
│ Username:  [_______________]       │
│ Password:  [_______________]       │
│                                    │
│             [ LOGIN ]              │
└────────────────────────────────────┘
```

The login process:

```text
Enter Credentials
       │
       ▼
Authenticate User
       │
       ├───────────────┐
       ▼               ▼
     ADMIN          CUSTOMER
       │               │
       ▼               ▼
Admin Dashboard   Customer Dashboard
```



---

## Phase 6.6 — Admin Dashboard

The Admin dashboard provides access to management functionality.

Current structure:

```text
┌─────────────────────────────┐
│       Admin Dashboard       │
├─────────────────────────────┤
│                             │
│   Register Customer         │
│   Create Bank Account       │
│   Transaction History       │
│                             │
│   Logout                    │
│                             │
└─────────────────────────────┘
```

The Admin role is intended for management operations such as customer, account, and transaction administration.

---

## Phase 6.7 — Customer Dashboard

The Customer dashboard provides banking operations for the authenticated customer.

Planned interface:

```text
┌─────────────────────────────┐
│      Customer Dashboard     │
├─────────────────────────────┤
│                             │
│   My Account                │
│   Deposit Money             │
│   Withdraw Money            │
│   Transfer Money            │
│   Transaction History       │
│                             │
│   Logout                    │
│                             │
└─────────────────────────────┘
```

The important part of this phase is that the dashboard receives the authenticated user's information, including:

```python
user["customer_id"]
```

This can then be used to restrict operations to the currently authenticated customer's records rather than allowing arbitrary account access.

---

# 🏗️ Current Architecture

The project currently follows a modular architecture:

```text
                    ┌─────────────┐
                    │  Tkinter UI │
                    └──────┬──────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
        Authentication              Banking Modules
             │                           │
             ▼                           ▼
          auth/              customers / accounts /
                             transactions
             │                           │
             └─────────────┬─────────────┘
                           │
                           ▼
                    database/db.py
                           │
                           ▼
                       SQLite
```

This structure keeps the GUI, authentication, business operations, and database access separated instead of placing all functionality inside `main.py`.

---

# 📁 Project Structure

```text
bank-management-system/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── auth/
│   ├── __init__.py
│   └── authentication.py
│
├── customers/
│   ├── __init__.py
│   └── customer.py
│
├── accounts/
│   ├── __init__.py
│   └── account.py
│
├── transactions/
│   ├── __init__.py
│   └── transaction.py
│
└── gui/
    ├── __init__.py
    ├── login_gui.py
    ├── admin_dashboard.py
    ├── customer_dashboard.py
    ├── customer_gui.py
    ├── account_gui.py
    ├── deposit_gui.py
    ├── withdrawal_gui.py
    ├── balance_gui.py
    ├── transfer_gui.py
    └── transaction_gui.py
```

---

# 🗄️ Database Relationships

```text
                 ┌──────────────┐
                 │    users     │
                 └──────┬───────┘
                        │
                  customer_id
                        │
                        ▼
                 ┌──────────────┐
                 │  customers   │
                 └──────┬───────┘
                        │
                   customer_id
                        │
                        ▼
                 ┌──────────────┐
                 │   accounts   │
                 └──────┬───────┘
                        │
                  account_number
                        │
                        ▼
                 ┌──────────────┐
                 │ transactions │
                 └──────────────┘
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/bank-management-system.git
```

## 2. Navigate to the project

```bash
cd bank-management-system
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the application

```bash
python main.py
```

The application initializes the database, creates the default administrator if necessary, and opens the login screen.

---

# 🔑 Demo Login

```text
Username: admin
Password: admin123
```

> **Security note:** This credential is intended only for the educational/demo version. Do not use it for a real banking application.

---

# 🧪 Testing

The project has been developed with manual testing around the major workflows.

Important test cases include:

### Authentication

- Valid Admin login
- Invalid password
- Invalid username
- Customer login
- Invalid customer credentials

### Customer Management

- Register customer
- Generate Customer ID
- Duplicate username handling

### Accounts

- Create account
- Generate Account Number
- Initial deposit
- Savings account
- Current account

### Transactions

- Deposit
- Withdrawal
- Insufficient balance
- Transfer
- Invalid account
- Transaction history
- Account with no transactions

---

# 📊 Feature Status

| Feature | Status |
|---|---|
| Customer Registration | ✅ |
| Automatic Customer ID | ✅ |
| Bank Account Creation | ✅ |
| Automatic Account Number | ✅ |
| Savings Account | ✅ |
| Current Account | ✅ |
| Initial Deposit | ✅ |
| Deposit | ✅ |
| Withdrawal | ✅ |
| Balance Checking | ✅ |
| Account Transfer | ✅ |
| Transaction Recording | ✅ |
| Transaction History | ✅ |
| Initial Deposit History | ✅ |
| User Authentication | ✅ |
| Password Hashing | ✅ |
| Admin Role | ✅ |
| Customer Role | ✅ |
| Admin Dashboard | ✅ |
| Customer Dashboard Structure | ✅ |
| Customer-specific Access Control | 🔄 |
| Automated Tests | 🔄 |
| Logging | 🔄 |
| GUI Improvements | 🔄 |

---

# 🔒 Security Note

This project is an **educational portfolio project** and is not intended for production banking use.

The project demonstrates concepts such as password hashing, authentication, role-based access, database transactions, and input validation.

A production banking system would require significantly stronger security controls, including secure password hashing, encryption, session management, auditing, secrets management, monitoring, and extensive security testing.

---

# 🧠 Concepts Demonstrated

This project demonstrates practical software development concepts including:

- Python modular programming
- GUI development with Tkinter
- SQLite database design
- CRUD operations
- SQL queries
- Foreign-key relationships
- Database transactions
- Commit and rollback
- Input validation
- Exception handling
- Password hashing
- Authentication
- Role-based authorization
- Separation of concerns
- Git and GitHub workflow

---

# 🚧 Future Improvements

Planned improvements include:

- Complete customer-specific account access
- Improve the Tkinter UI
- Add automated unit tests
- Add application logging
- Improve password security
- Move configuration and credentials outside source code
- Add better session/logout handling
- Add reporting functionality
- Add API/backend version
- Add deployment support

---

# 👨‍💻 Author

Aman Kumar

Python Developer | Backend & Platform Engineering Enthusiast

---

## ⭐ Project

If you find this project useful, feel free to ⭐ the repository and explore the source code.
