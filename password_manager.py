master_password = input("Enter your master password: ")


def view():
    
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            data, pwd = data.split("-")
            print(f"Username: {data}, Password: {pwd}")


def add():

    name = input("Include Account Name: ")
    password = input("Enter Password: ")

    with open("password.txt", "a") as f:
        f.write(name + ' - ' + password + '\n')


while True:
    mode = input("Choose add/view whether to add a new password or view existing ones or press Q for quit: ").lower()

    if mode == "view":
        view()

    if mode == "add":
        add()

    if mode == "q":
        break
