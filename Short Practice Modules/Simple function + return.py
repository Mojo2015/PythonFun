#Simple Function

def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

input_age = int(input("How old are you? "))
my_limit = allowed_dating_age(input_age)
print("You can date girls", my_limit, "or older")
