# reading the original .txt file
with open("audit.txt") as file:
    # find usernames and passwords
    passwords = [line.split(':')[1].strip() for line in file if line.startswith("Password")]
    file.seek(0) # moving the cursor back to the start
    usernames = [line.split(':')[1].strip() for line in file if line.startswith("Username")]

    # aggregate usernames and passwords into a dictionary
    accounts = {}
    for i in range(len(usernames)):
        accounts[usernames[i]] = passwords[i]

# writing usernames and passwords into a new file
with open("accounts.txt", "w") as file:
    for key,value in accounts.items():
        file.write(key + ": ")
        file.write(value + "\n")
    