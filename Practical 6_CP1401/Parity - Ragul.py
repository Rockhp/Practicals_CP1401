"""Parity"""

def main():
    num = int(input("Enter the number: "))
    odd = is_odd(num)
    print(f"Is odd? {odd} (expected {num % 2})")


def display_parity(num):
    print(num % 2)


def get_parity(num):
    return num % 2


def is_odd(num):
    parity = get_parity(num)
    if parity == 0:
        return False
    else:
        return True


main()