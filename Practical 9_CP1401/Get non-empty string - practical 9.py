def main():
    name = ""
    name = get_name(name)
    birth_place = ""
    birth_place = get_birthplace(birth_place)
    print(f"Hi {name} from {birth_place}!")

def get_name(name):
    return str(input("What is your name? ")).title()

def get_birthplace(birth_place):
    return str(input("What is your birthplace? ")).title()

main()