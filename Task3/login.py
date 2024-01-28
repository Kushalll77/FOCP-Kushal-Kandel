def login(username, password):
    with open('passwd.txt', 'r') as file:
        for line in file:
            fields = line.split(':')
            if fields[0] == username and fields[2].strip() == password:
                return True
    return False

if __name__ == "__main__":
    login_username = input("User:     ")
    login_password = input("Password: ")
    
    if login(login_username, login_password):
        print("Access granted.")
    else:
        print("Access denied.")