from database import load_admins, save_users, load_users
from datetime import datetime

def is_valid_phone(phone):
    return phone.isdigit()

def is_valid_email(email):
    return "@" in email

def is_valid_dob(dob):
    try:
        year, month, day = map(int, dob.split("-"))
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        
        # Days in each month
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        
        # Check for leap year
        if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            month_days[2] = 29
        
        return day <= month_days[month]
    except ValueError:
        return False

def admin_menu(users):
    admins = load_admins()
    username = input("Enter admin username: ").strip()
    if username not in admins:
        print("❌ Admin username not found.")
        return
    
    password = input("Enter admin password: ").strip()
    if password != admins[username]['password']:
        print("❌ Incorrect password.")
        return
    
    while True:
        print("\n🔧 Admin Panel")
        print("1. Approve Pending Accounts")
        print("2. View All Accounts")
        print("3. Edit User Details")
        print("4. Check Transaction History")
        print("5. Delete User Account")
        print("6. Logout")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            approve_accounts(users)
        elif choice == "2":
            view_accounts(users)
        elif choice == "3":
            edit_user_details(users)
        elif choice == "4":
            check_transaction_history(users)
        elif choice == "5":
            delete_user_account(users)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def edit_user_details(users):
    print("❌ Press ENTER to go back.")
    username = input("Enter username to edit: ").strip()
    account_number = None
    for acc, details in users.items():
        if details.get("username") == username:
            account_number = acc
            break
    
    if not account_number:
        print("❌ Username not found.")
        return
    
    user = users[account_number]
    print("\n📋 Customer Details:")
    print(f"Account No.: {account_number}\nFull Name: {user['name']}\nID Number: {user['id_number']}\nPhone: {user['phone']}\nEmail: {user['email']}\nDOB: {user['dob']}\nAddress: {user['address']}\n{'-'*50}\n")
    
    print("1. Edit Address")
    print("2. Edit Date of Birth")
    print("3. Edit ID Number")
    print("4. Edit Password")
    print("5. Edit Phone Number")
    print("6. Edit Email")
    print("7. Edit PIN")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        new_value = input("Enter new address (Leave blank to cancel): ").strip()
        if new_value:
            users[account_number]['address'] = new_value
    elif choice == "2":
        while True:
            new_value = input("Enter new date of birth (YYYY-MM-DD, Leave blank to cancel): ").strip()
            if new_value == "":
                return
            if not is_valid_dob(new_value):
                print("❌ Invalid date format or invalid date. Ensure it's YYYY-MM-DD and valid.")
                continue
            users[account_number]['dob'] = new_value
            break
    elif choice == "3":
        new_value = input("Enter new ID number (Leave blank to cancel): ").strip()
        if new_value:
            users[account_number]['id_number'] = new_value
    elif choice == "4":
        new_value = input("Enter new password (Leave blank to cancel): ").strip()
        if new_value:
            users[account_number]['password'] = new_value
    elif choice == "5":
        while True:
            new_value = input("Enter new phone number (Leave blank to cancel): ").strip()
            if new_value == "":
                return
            if not is_valid_phone(new_value):
                print("❌ Invalid phone number. Only numbers are allowed.")
                continue
            users[account_number]['phone'] = new_value
            break
    elif choice == "6":
        while True:
            new_value = input("Enter new email (Leave blank to cancel): ").strip()
            if new_value == "":
                return
            if not is_valid_email(new_value):
                print("❌ Invalid email format. Must contain '@'.")
                continue
            users[account_number]['email'] = new_value
            break
    elif choice == "7":
        while True:
            new_value = input("Enter new PIN (Leave blank to cancel): ").strip()
            if new_value == "":
                return
            if not new_value.isdigit() or len(new_value) != 6:
                print("❌ Invalid PIN. Must be exactly 6 digits.")
                continue
            users[account_number]['pin'] = new_value
            break
    else:
        print("Invalid choice.")
        return
    
    save_users(users)
    print("✅ User details updated successfully.")

def approve_accounts(users):
    print("❌ Press ENTER to go back.")
    print("\nPending Accounts:")
    pending_accounts = {acc: details for acc, details in users.items() if not details.get('approved', False)}
    if not pending_accounts:
        print("No pending accounts.")
        return
    
    for acc, details in pending_accounts.items():
        print(f"Account No.: {acc}\nFull Name: {details['name']}\nID Number: {details['id_number']}\nPhone: {details['phone']}\nEmail: {details['email']}\nDOB: {details['dob']}\nAddress: {details['address']}\n{'-'*50}")
    
    account_number = input("Enter account number to approve: ").strip()
    if account_number in pending_accounts:
        users[account_number]['approved'] = True
        save_users(users)
        print(f"✅ Account {account_number} approved.")
    else:
        print("❌ Invalid account number.")

def view_accounts(users):
    print("❌ Press ENTER to go back.")
    print("\n📋 List of All Accounts:")
    if not users:
        print("No accounts found.")
        return
    
    for acc, details in users.items():
        status = "Approved" if details.get('approved', False) else "Pending"
        print(f"Account No.: {acc}\nFull Name: {details['name']}\nPhone: {details['phone']}\nEmail: {details['email']}\nDOB: {details['dob']}\nAddress: {details['address']}\nStatus: {status}\n{'-'*50}")

def check_transaction_history(users):
    print("❌ Press ENTER to go back.")
    account_number = input("Enter account number to view transactions: ").strip()
    if account_number not in users:
        print("❌ Account not found.")
        return
    
    transactions = users[account_number].get("history", [])
    if not transactions:
        print("No transactions found for this account.")
        return
    
    print("\nTransaction History:")
    print("{:<20} {:<15} {:<10} {:<10}".format("Date", "Type", "Amount", "Balance"))
    print("-"*60)
    for txn in transactions:
        if isinstance(txn, dict) and all(key in txn for key in ["date", "type", "amount", "balance"]):
            print("{:<20} {:<15} {:<10} {:<10}".format(txn["date"], txn["type"], txn["amount"], txn["balance"]))
        else:
            print("⚠️ Invalid transaction data found.")

def delete_user_account(users):
    print("❌ Press ENTER to go back.")
    account_number = input("Enter account number to delete: ").strip()
    if account_number not in users:
        print("❌ Account not found.")
        return
    
    user = users[account_number]
    print("\nUser Details:")
    print(f"Account No.: {account_number}\nFull Name: {user['name']}\nID Number: {user['id_number']}\nPhone: {user['phone']}\nEmail: {user['email']}\nDOB: {user['dob']}\nAddress: {user['address']}\n{'-'*50}")
    
    confirm = input(f"Are you sure you want to delete account {account_number}? (yes/no): ").strip().lower()
    if confirm == "yes":
        del users[account_number]
        save_users(users)
        print(f"✅ Account {account_number} deleted successfully.")
    else:
        print("Deletion cancelled.")
