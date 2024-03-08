import os

def get_email_parts(email):
    parts = email.split('@')
    if len(parts) == 2:
        username, rest = parts
        domain, extension = rest.split('.')
        return username, domain, extension
    else:
        return None
   
def main():
    while True:
        os.system('cls')
        user_email = input("Enter your email address: ")

        if '@' in user_email and '.' in user_email:
            username, domain, extension = get_email_parts(user_email)
            
            if username and domain and extension:
                print(f"\nUsername: {username}")
                print(f"Domain: {domain}")
                print(f"Extension: {extension}")
                break
            else:
                print("Invalid email address format. Please try again.")
        else:
            print("Invalid email address format. Please include '@' and '.'.")

if __name__ == "__main__":
    main()
