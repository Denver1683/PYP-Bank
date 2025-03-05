from database import save_users
from datetime import datetime

def is_valid_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return False
        return True
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        return False

def verify_pin(account_number, users):
    pin_attempt = input("Enter your 6-digit PIN: ").strip()
    if not pin_attempt.isdigit() or len(pin_attempt) != 6:
        print("❌ Invalid PIN format. Must be 6 digits.")
        return False
    if pin_attempt != users[account_number]["pin"]:
        print("❌ Incorrect PIN.")
        return False
    return True

def log_transaction(account_number, users, transaction_type, amount, other_account=None):
    transaction_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type if not other_account else f"{transaction_type} {'from' if 'In' in transaction_type else 'to'} {other_account}",
        "amount": amount,
        "balance": users[account_number]["balance"]
    }
    users[account_number].setdefault("history", []).append(transaction_entry)
    save_users(users)

def deposit(account_number, users):
    if not verify_pin(account_number, users):
        return
    amount = input("Enter deposit amount: ")
    if is_valid_amount(amount):
        amount = float(amount)
        users[account_number]["balance"] += amount
        log_transaction(account_number, users, "Deposit", amount)
        print(f"✅ Deposited {amount} successfully! New balance: {users[account_number]['balance']}")

def withdraw(account_number, users):
    if not verify_pin(account_number, users):
        return
    amount = input("Enter withdrawal amount: ")
    if is_valid_amount(amount):
        amount = float(amount)
        if users[account_number]["balance"] >= amount:
            users[account_number]["balance"] -= amount
            log_transaction(account_number, users, "Withdraw", amount)
            print(f"✅ Withdrawn {amount} successfully! New balance: {users[account_number]['balance']}")
        else:
            print("❌ Insufficient balance.")

def transfer(account_number, users):
    if not verify_pin(account_number, users):
        return
    recipient_account = input("Enter recipient account number: ").strip()
    if recipient_account not in users or recipient_account == account_number:
        print("❌ Invalid recipient.")
        return
    
    amount = input("Enter transfer amount: ")
    if is_valid_amount(amount):
        amount = float(amount)
        if users[account_number]["balance"] >= amount:
            users[account_number]["balance"] -= amount
            users[recipient_account]["balance"] += amount
            log_transaction(account_number, users, "Transfer Out", amount, recipient_account)
            log_transaction(recipient_account, users, "Transfer In", amount, account_number)
            print(f"✅ Transferred {amount} to {recipient_account}! New balance: {users[account_number]['balance']}")
        else:
            print("❌ Insufficient balance.")

def check_balance(account_number, users):
    if not verify_pin(account_number, users):
        return
    print(f"💰 Your current balance ({account_number}): {users[account_number]['balance']}")

def transaction_history(account_number, users):
    if not verify_pin(account_number, users):
        return
    transactions = users[account_number].get("history", [])
    if not transactions:
        print("No transactions found for this account.")
        return
    
    print("\n📜 Transaction History:")
    print("{:<20} {:<30} {:<10} {:<10}".format("Date", "Type", "Amount", "Balance"))
    print("-"*70)
    
    for txn in transactions:
        if isinstance(txn, dict) and all(key in txn for key in ["date", "type", "amount", "balance"]):
            print("{:<20} {:<30} {:<10} {:<10}".format(txn["date"], txn["type"], txn["amount"], txn["balance"]))
        else:
            print("⚠️ Invalid transaction log detected, skipping entry.")

def change_pin(account_number, users):
    old_pin = input("Enter current PIN: ").strip()
    if old_pin != users[account_number]["pin"]:
        print("❌ Incorrect PIN.")
        return
    
    new_pin = input("Enter new 6-digit PIN: ").strip()
    if not new_pin.isdigit() or len(new_pin) != 6:
        print("❌ Invalid PIN format. Must be 6 digits.")
        return
    
    users[account_number]["pin"] = new_pin
    save_users(users)
    print("✅ PIN changed successfully.")

def change_password(account_number, users):
    old_password = input("Enter current password: ").strip()
    if old_password != users[account_number]["password"]:
        print("❌ Incorrect password.")
        return
    
    new_password = input("Enter new password: ").strip()
    users[account_number]["password"] = new_password
    save_users(users)
    print("✅ Password changed successfully.")
