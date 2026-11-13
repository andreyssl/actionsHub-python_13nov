def greet_user(user_name):
    # TODO: greet the user with the correct greeting
    print("Hello", user_name)


if __name__ == "__main__":
    # ask sure their name and store it in a variable
    name = input("What is your name? ")

    # call the function to greet the user (don't forget to pass the name variable as an argument)
    greet_user(name)