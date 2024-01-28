def add_user(username, real_name, password):
    with open('passwd.txt', 'a') as file:
        file.write(f'{username}:{real_name}:{password}\n')
    print("User Created.")

if __name__ == "__main__":
    new_username = input("Enter new username: ")
    new_real_name = input("Enter real name: ")
    new_password = input("Enter password: ")
    
    with open('passwd.txt', 'r') as file:
        existing_users = [line.split(':')[0] for line in file.readlines()]
        
    if new_username in existing_users:
        print("Cannot add. Most likely username already exists.")
    else:
        add_user(new_username, new_real_name, new_password)