def main():
    numMin = int(input("Minimum number: "))
    numMax = int(input("Maximum number: "))
    while numMax <= numMin:
        print(f"Your maximum must be greater than {numMin}")
        numMax = int(input("Maximum number: "))
    numList = []
    gen_list(numMin, numMax, numList)
    print(numList)

def gen_list(numMin, numMax, numList):
    for x in range(numMin, numMax+1):
        numList.append(x)

main()