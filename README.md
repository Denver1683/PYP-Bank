# PYP Banking System

## Overview
PYP Bank is a **Python-based banking system** that offers essential banking features such as:
- User account creation and management (admin approval required)
- Deposits, withdrawals, and transfers
- Balance checks and transaction history
- Secure authentication via PIN and password
- Admin and superuser functionalities for account moderation
- Forgot username/password recovery system

This project is for **educational and personal use only** and should not be redistributed or used for commercial purposes without authorization.

## Features
### User Features
✅ **Sign Up** (Pending Admin Approval)
✅ **Login using username and password**
✅ **Deposit, Withdraw, and Transfer funds**
✅ **Check Balance and Balance History**
✅ **Change PIN and Password**
✅ **Forgot Username/Password Recovery**

### Admin Features
✅ **Approve Pending Accounts**
✅ **View All Accounts**
✅ **Edit User Details**
✅ **Check Transaction History**
✅ **Delete User Accounts**

### Superuser Features
✅ **Create and Manage Admin Accounts**
✅ **View All Admins**
✅ **Delete Admin Accounts**

## Installation & Setup
### Prerequisites
- Python 3.x installed on your system

### Installation Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/Denver1683/PYP-bank.git
   ```
2. Navigate to the project folder:
   ```sh
   cd pyp-banking-system
   ```
3. Run the banking system:
   ```sh
   python banking_system.py
   ```

## File Structure
```
├── banking_system.py   # Main program
├── auth.py             # User authentication & signup
├── transactions.py     # Transaction handling
├── admin.py           # Admin functionalities
├── superuser.py       # Superuser functionalities
├── database.py        # Data storage (JSON-based)
├── users.json         # Stores user data (auto generate)
├── admins.json        # Stores admin data (auto generate)
├── README.md          # Documentation
```

## Usage
### Running the System
Launch the **banking_system.py** file to start the program:
```sh
python banking_system.py
```
Follow the on-screen prompts to **sign up**, **log in**, and perform banking transactions.

### Recovering Forgotten Credentials
If a user forgets their username or password, they can retrieve or reset them via the **Forgot Username/Password** menu:
1. **Forgot Username**: Requires ID number and password.
2. **Forgot Password**: Requires username and ID number.

## Security Measures
- **PIN Authentication**: Required for deposits, withdrawals, transfers, and balance checks.
- **Admin Approval**: New users require admin approval before logging in.
- **Superuser Protection**: Superuser accounts manage admin accounts but do not interact with users directly.

## License
This project is for personal and educational use only. Commercial use is **prohibited** without explicit authorization.


