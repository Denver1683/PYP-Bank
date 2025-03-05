import random
from database import save_users

def generate_unique_account_number(users):
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if account_number not in users:
            return account_number

def is_username_taken(username, users):
    return any(user_data['username'] == username for user_data in users.values())

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

def signup(users):
    print("\n📝 Sign Up Form (Leave blank to cancel)")
    name = input("Enter full name: ").strip()
    if name == "":
        print("Returning to main menu...")
        return
    
    while True:
        username = input("Enter a username for login: ").strip()
        if username == "":
            print("Returning to main menu...")
            return
        if is_username_taken(username, users):
            print("❌ Username already taken. Please choose another one.")
            continue
        break
    
    id_number = input("Enter your ID number: ").strip()
    if id_number == "":
        print("Returning to main menu...")
        return
    
    while True:
        phone = input("Enter phone number: ").strip()
        if phone == "":
            print("Returning to main menu...")
            return
        if not is_valid_phone(phone):
            print("❌ Invalid phone number. Only numbers are allowed.")
            continue
        break
    
    while True:
        email = input("Enter email: ").strip()
        if email == "":
            print("Returning to main menu...")
            return
        if not is_valid_email(email):
            print("❌ Invalid email format. Must contain '@'.")
            continue
        break
    
    while True:
        dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
        if dob == "":
            print("Returning to main menu...")
            return
        if not is_valid_dob(dob):
            print("❌ Invalid date format or invalid date. Ensure it's YYYY-MM-DD and valid.")
            continue
        break
    
    address = input("Enter your address: ").strip()
    if address == "":
        print("Returning to main menu...")
        return
    
    password = input("Enter password: ").strip()
    if password == "":
        print("Returning to main menu...")
        return
    
    while True:
        pin = input("Enter 6-digit PIN: ").strip()
        if pin == "":
            print("Returning to main menu...")
            return
        if not pin.isdigit() or len(pin) != 6:
            print("❌ Invalid PIN. Must be exactly 6 digits.")
            continue
        break
    
    account_number = generate_unique_account_number(users)
    users[account_number] = {
        "name": name,
        "username": username,
        "id_number": id_number,
        "phone": phone,
        "email": email,
        "dob": dob,
        "address": address,
        "password": password,
        "pin": pin,
        "balance": 0,
        "history": [],
        "approved": False
    }
    
    save_users(users)
    print(f"✅ Signup successful! Your account number is {account_number}. Please wait for admin approval.")
    input("Press Enter to return to the main menu...")

def login(users):
    username = input("Enter username: ").strip()
    for account_number, details in users.items():
        if details.get("username") == username:
            if not details.get("approved", False):
                print("❌ Your account is pending admin approval. Please wait for approval.")
                return None
            
            password = input("Enter password: ").strip()
            if details.get("password") == password:
                print("✅ Login successful!")
                return account_number
            else:
                print("❌ Invalid password.")
                return None
    print("❌ Username not found.")
    return None


