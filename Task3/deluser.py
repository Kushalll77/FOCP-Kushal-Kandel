def delete_user(username):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()
    
    with open('passwd.txt', 'w') as file:
        for line in lines:
            if not line.startswith(username + ":"):
                file.write(line)
    
    print("User Deleted.")

if __name__ == "__main__":
    delete_username = input("Enter username: ")
    delete_user(delete_username)