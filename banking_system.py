from auth import signup, login
from transactions import deposit, withdraw, transfer, check_balance, transaction_history, change_pin, change_password
from admin import admin_menu
from superuser import superuser_menu
from database import load_users, save_users, load_admins, save_admins

# Main Menu
def main():
    users = load_users()
    admins = load_admins()
    
    while True:
        print("\n🏦 Welcome to the PYP Banking System")
        print("1. Sign Up (Pending Admin Approval)")
        print("2. Login")
        print("3. Admin Login")
        print("4. Superuser Login")
        print("5. Forgot Username/Password")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            signup(users)
            users = load_users()  # Reload users to reflect changes after signup
        elif choice == "2":
            account_number = login(users)
            if account_number:
                user_menu(account_number, users)
        elif choice == "3":
            admin_menu(users)
        elif choice == "4":
            superuser_menu(admins)
        elif choice == "5":
            forgot_credentials(users)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Forgot Username/Password Menu
def forgot_credentials(users):
    print("\n🔍 Forgot Username/Password")
    print("1. Forgot Username")
    print("2. Forgot Password")
    print("3. Go Back")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        id_number = input("Enter your ID number: ").strip()
        password = input("Enter your password: ").strip()
        for acc, details in users.items():
            if details["id_number"] == id_number and details["password"] == password:
                print(f"✅ Your username is: {details['username']}")
                return
        print("❌ No matching user found.")
    elif choice == "2":
        username = input("Enter your username: ").strip()
        id_number = input("Enter your ID number: ").strip()
        for acc, details in users.items():
            if details["username"] == username and details["id_number"] == id_number:
                new_password = input("Enter new password: ").strip()
                users[acc]["password"] = new_password
                save_users(users)
                print("✅ Password successfully reset.")
                return
        print("❌ No matching user found.")
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")

# Logged-in user menu
def user_menu(account_number, users):
    if account_number not in users:
        print("❌ Error: Account not found.")
        return
    
    if not users[account_number]['approved']:
        print("❌ Your account is pending admin approval. Please wait for approval.")
        return
    
    while True:
        print(f"\nWelcome, {users[account_number]['name']}!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Balance History")
        print("6. Change PIN")
        print("7. Change Password")
        print("8. Logout")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            deposit(account_number, users)
        elif choice == "2":
            withdraw(account_number, users)
        elif choice == "3":
            transfer(account_number, users)
        elif choice == "4":
            check_balance(account_number, users)
        elif choice == "5":
            transaction_history(account_number, users)
        elif choice == "6":
            change_pin(account_number, users)
        elif choice == "7":
            change_password(account_number, users)
        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
