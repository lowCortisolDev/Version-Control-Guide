def greet(name):
    return f"Hello, {name}! Welcome to Git."

def main():
    user_name = "Merge User"
    print(greet(user_name))

#New features
def greet_with_age(name, age):  #Greet using name and age
    return f"Hello, {name}! You are {age} years old. Welcome to Git."

def get_user_info():    #Gets use info
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

def main_with_user_input():    #New main function
    user_name, user_age = get_user_info()
    print(greet_with_age(user_name, user_age))

if __name__ == "__main__":
    main()
    main_with_user_input()