def main():
    subCode = "0"
    subList = []
    while subCode != "":
        subCode = input("Enter subject code: ").upper()
        if subCode != "":
            while len(subCode) != 6:
                print("Invalid subject code")
                subCode = input("Enter subject code: ").upper()
            subList.append(subCode)
        else:
            print(f"You do these {len(subList)} subjects:")
    print_subjects(subList)
    print(is_cool(subList))

def print_subjects(subList):
    for x in range(len(subList)):
        print(subList[x])

def is_cool(subList):
    if "CP1401" in subList:
        return "You are cool!"
    else:
        return "You aren't cool :("

main()