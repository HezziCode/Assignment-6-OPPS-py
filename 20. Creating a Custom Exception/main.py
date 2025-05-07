class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Sorry, age must be at least 18.")
    else:
        print("You are eligible")

try:
    user_age = int(input("\nEnter Your Age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(e)
except:
    print("You can use number only")