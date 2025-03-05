# superuser.py (Superuser Management)
from database import load_admins, save_admins

def superuser_menu(admins):
    admins = load_admins()
    print("\n🔐 Superuser Login")
    username = input("Enter superuser username: ").strip()
    password = input("Enter superuser password: ").strip()
    
    if username != "superadmin" or password != "superpassword":
        print("❌ Incorrect superuser credentials.")
        return
    
    while True:
        print("\n🛠 Superuser Panel")
        print("1. Create Admin Account")
        print("2. Delete Admin Account")
        print("3. View All Admins")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            create_admin(admins)
        elif choice == "2":
            delete_admin(admins)
        elif choice == "3":
            view_admins(admins)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def create_admin(admins):
    print("\n📝 Create Admin Account (Leave blank to cancel)")
    
    username = input("Enter new admin username: ").strip()
    if username == "":
        print("Returning to superuser menu...")
        return
    if username in admins:
        print("❌ Username already exists.")
        return
    
    name = input("Enter full name: ").strip()
    if name == "":
        print("Returning to superuser menu...")
        return
    id_number = input("Enter ID number: ").strip()
    if id_number == "":
        print("Returning to superuser menu...")
        return
    phone = input("Enter phone number: ").strip()
    if phone == "":
        print("Returning to superuser menu...")
        return
    email = input("Enter email: ").strip()
    if email == "":
        print("Returning to superuser menu...")
        return
    dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
    if dob == "":
        print("Returning to superuser menu...")
        return
    address = input("Enter address: ").strip()
    if address == "":
        print("Returning to superuser menu...")
        return
    password = input("Enter admin password: ").strip()
    if password == "":
        print("Returning to superuser menu...")
        return
    
    admins[username] = {
        "name": name,
        "id_number": id_number,
        "phone": phone,
        "email": email,
        "dob": dob,
        "address": address,
        "password": password,
        "role": "admin"
    }
    save_admins(admins)  # Ensure the updated dictionary is saved
    print(f"✅ Admin account '{username}' created successfully.")

def delete_admin(admins):
    print("❌ Press ENTER to go back.")
    username = input("Enter admin username to delete: ").strip()
    if username not in admins or admins[username].get("role") != "admin":
        print("❌ Admin not found.")
        return
    
    del admins[username]
    save_admins(admins)
    print(f"✅ Admin account '{username}' deleted successfully.")

def view_admins(admins):
    print("❌ Press ENTER to go back.")
    print("\n📋 List of Admins:")
    if not admins:
        print("No admins found.")
        return

    print(f"{'Username':<15}{'Full Name':<20}{'ID Number':<15}{'Phone':<15}{'Email':<25}{'DOB':<12}{'Address'}")
    print("-" * 110)

    for admin, details in admins.items():
        print(f"{admin:<15}{details.get('name', 'N/A'):<20}{details.get('id_number', 'N/A'):<15}"
              f"{details.get('phone', 'N/A'):<15}{details.get('email', 'N/A'):<25}{details.get('dob', 'N/A'):<12}"
              f"{details.get('address', 'N/A')}")

