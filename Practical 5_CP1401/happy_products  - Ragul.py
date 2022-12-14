Menu = ['(I)nstructions', '(C)alculate', '(Q)uit']
print(*Menu, sep="\n")
choice = str(input("Choice: ")).lower()
while choice != "i" and choice != "c" and choice != "q":
    print("Invalid choice")
    choice = str(input("Choice: ")).lower()


if choice == "i":
    print("Enter the number of products you want to buy and your chosen price. "
          "If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")

elif choice == "c":
    number_of_products = int(input("Number of products: "))
    while number_of_products < 0:
        print("Invalid Entry")
        number_of_products = int(input("Number of products: "))
    price = float(input("Price: "))
    if number_of_products <= 5:
        print(number_of_products, "x $", price, "products = $", number_of_products * price)
    if number_of_products > 5:
        print(number_of_products, "x $", price, "products = $", (number_of_products*price) * 0.9)

elif choice == "q":
    print("Farewell")