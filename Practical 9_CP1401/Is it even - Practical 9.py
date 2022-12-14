def main():
    print_hyphens()
    age = int(input("Age: "))
    if is_even(age):
        print("Your age is even!")
    else:
        print("Your age is not even!")