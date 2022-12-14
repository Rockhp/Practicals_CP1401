def main():
    spd_mph = get_mph_speed()
    spd_kph = convert_mph_kph(spd_mph)
    lim_kph = get_kph_limit()
    diff = calculate_diff(spd_kph, lim_kph)
    fine = determine_fine(diff)
    demerit = determine_demerit(diff)
    if diff <= 0:
        print("You did not break the speed limit, no fine for you!")
    else:
        print(
            f"You were going {diff:.2f} kph over the speed limit, you will be fined ${fine} and you'll get {demerit} demerit points")


def get_mph_speed():
    spd_mph = int(input("Enter your speed in mph: "))
    while spd_mph < 0:
        print("Error! Invalid speed")
        spd_mph = int(input("Enter your speed in mph: "))
    return spd_mph


def convert_mph_kph(spd_mph):
    return spd_mph / 0.6214


def get_kph_limit():
    lim_kph = int(input("Enter speed limit in kph: "))
    while lim_kph < 0:
        print("Error! Invalid speed")
        lim_kph = int(input("Enter speed limit in kph: "))
    return lim_kph


def calculate_diff(spd_kph, lim_kph):
    return spd_kph - lim_kph


def determine_fine(diff):
    if diff < 13:
        return 177
    elif diff <= 20:
        return 266
    elif diff <= 30:
        return 444
    elif diff <= 40:
        return 622
    else:
        return 1245


def determine_demerit(diff):
    if diff < 13:
        return 1
    elif diff <= 20:
        return 3
    elif diff <= 30:
        return 4
    elif diff <= 40:
        return 6
    else:
        return 8


main()