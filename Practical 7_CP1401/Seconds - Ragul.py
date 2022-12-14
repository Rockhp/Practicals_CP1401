def main():
    sec = 1
    while sec >= 0:
        sec = int(input("Enter seconds: "))
        if sec >= 0:
            minute = get_minutes(sec)
            second = get_seconds(sec)
            print(f"{sec} seconds is {minute}m {second}s")
        else:
            print("End program")


def get_minutes(sec):
    return sec // 60


def get_seconds(sec):
    return sec % 60


main()