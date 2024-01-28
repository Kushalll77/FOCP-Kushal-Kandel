#Create function that takes 3 parameters
def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()
    
    with open('passwd.txt', 'w') as file:
        for line in lines:
            fields = line.split(':')
            if fields[0] == username and fields[2].strip() == current_password:
                file.write(f'{fields[0]}:{fields[1]}:{new_password}\n')
                print("Your password has been changed.")
            else:
                file.write(line)

if __name__ == "__main__":
    user_to_change = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")
    
    if new_password == confirm_password:
        change_password(user_to_change, current_password, new_password)
    else:
        print("Passwords do not match. No change made.")