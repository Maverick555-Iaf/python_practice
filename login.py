# Program 4: Login System
print("Login System")
print("────────────")

CORRECT_USERNAME = "SUBHODIP"
CORRECT_PASSWORD = "sdg55" 

attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\n✅ Login successful! Welcome admin.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"\n❌ Wrong credentials. {attempts} attempts left.\n")
        else:
            print("\n🔒 Account locked. Too many failed attempts.")